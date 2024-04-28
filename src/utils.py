from urllib.parse import urlparse
import random


SHORTCODE_LENGTH = 6

def sanitize_url(url: str):
    parsed_url = urlparse(url)
    return parsed_url.geturl()

def generate_shortcode(length: int):
    shortcode = ""
    valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
    for _ in range(length):
        shortcode += random.choice(valid_chars)
