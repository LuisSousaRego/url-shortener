from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ShortenRequest(BaseModel):
    url: str
    shortcode: str | None = None

@app.post("/shorten")
def create_short_url(shorten_request: ShortenRequest):
    return shorten_request

@app.get("/{shortcode}")
def read_item(shortcode: str):
    return shortcode

@app.get("/{shortcode}/stats")
def read_item(shortcode: str):
    return shortcode

@app.get("/")
def read_root():
    return "url shortener"

