from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel
from db import setup_db
import re
from utils import sanitize_url, generate_shortcode, SHORTCODE_LENGTH


pg = setup_db()
app = FastAPI()

class ShortenRequest(BaseModel):
    url: str | None = None
    shortcode: str | None = None

@app.post("/shorten")
def create_short_url(shorten_request: ShortenRequest):
    if shorten_request.url is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Url not present")

    url = sanitize_url(shorten_request.url)
    shortcode = shorten_request.shortcode

    with pg.cursor() as cur:
        if shorten_request.shortcode is None:
            while shortcode is None:
                shortcode = generate_shortcode(SHORTCODE_LENGTH)
                try:
                    cur.execute('INSERT INTO urls (url, shortcode) VALUES (%s, %s)', (url, shortcode))
                except:
                    shortcode = None
        else:
            # validate received shortcode
            is_alphanumeric_underscore = bool(re.match('^[a-zA-Z0-9_]+$', shorten_request.shortcode))
            if len(shorten_request.shortcode) != SHORTCODE_LENGTH or not is_alphanumeric_underscore:
                raise HTTPException(status_code=status.HTTP_412_PRECONDITION_FAILED, detail="The provided shortcode is invalid")

            try:
                cur.execute('INSERT INTO urls (url, shortcode) VALUES (%s, %s)', (url, shortcode))
            except:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Shortcode already in use")

        pg.commit() 
        return { "shortcode": shortcode }

@app.get("/{shortcode}")
def read_shortcode(shortcode: str, response: Response):
    with pg.cursor() as cur:
        cur.execute('''
                    UPDATE urls
                    SET redirect_count = redirect_count + 1,
                        last_redirect = current_timestamp
                    WHERE shortcode = %s
                    RETURNING url
                    ''', (shortcode,))

        row = cur.fetchone()
        if row is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Shortcode not found")
        pg.commit()
        response.status_code = status.HTTP_302_FOUND
        response.headers['Location'] = row[0]

@app.get("/{shortcode}/stats")
def read_stats(shortcode: str):
    with pg.cursor() as cur:
        cur.execute('''
                    SELECT created, last_redirect, redirect_count
                    FROM urls
                    WHERE shortcode = %s
                    ''', (shortcode,))

        row = cur.fetchone()
        if row is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Shortcode not found")

        created, last_redirect, redirect_count = row
        stats = {
            "created": created.isoformat(),
            "lastRedirect": last_redirect.isoformat() if last_redirect is not None else None,
            "redirectCount": redirect_count
        }
        return stats

@app.get("/")
def read_root():
    return "url shortener"
