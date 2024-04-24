from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class ShortenRequest(BaseModel):
    url: str | None = None
    shortcode: str | None = None

@app.post("/shorten")
def create_short_url(shorten_request: ShortenRequest):
    if shorten_request.url is None:
        raise HTTPException(status_code=400, detail="Url not present")
    
    # if shorten_request.shortcode is invalid:
    #     raise HTTPException(status_code=412, detail="The provided shortcode is invalid")


    # if shorten_request.shortcode is alreadyinuse:
        # raise HTTPException(status_code=409, detail="Shortcode already in use")

    return shorten_request

@app.get("/{shortcode}")
def read_shortcode(shortcode: str):
    # if shortcode is notfound:
    #     raise HTTPException(status_code=404, detail="Shortcode not found")

    return shortcode

@app.get("/{shortcode}/stats")
def read_stats(shortcode: str):
    # if shortcode is notfound:
    #     raise HTTPException(status_code=404, detail="Shortcode not found")

    return shortcode + ' stats'

@app.get("/")
def read_root():
    return "url shortener"

