from urllib.parse import urlparse
import random
import re


SHORTCODE_LENGTH = 6
GENERATE_TRIES = 10

def sanitize_url(url: str):
    parsed_url = urlparse(url)
    return parsed_url.geturl()

def generate_shortcode():
    shortcode = ""
    valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
    for _ in range(SHORTCODE_LENGTH):
        shortcode += random.choice(valid_chars)

def validate_shortcode(shortcode: str):
    has_correct_characters = bool(re.match('^[a-zA-Z0-9_]+$', shortcode))
    has_correct_legth = len(shortcode) == SHORTCODE_LENGTH
    return has_correct_legth and has_correct_characters
