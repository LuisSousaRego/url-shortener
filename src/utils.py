from urllib.parse import urlparse, urlunparse
import random
import re

SHORTCODE_LENGTH = 6
GENERATE_TRIES = 10

def sanitize_url(url: str):
    parsed_url = urlparse(url)
    sanitized_url = urlunparse((
                        parsed_url.scheme,
                        parsed_url.netloc,
                        parsed_url.path,
                        '',
                        '',
                        ''
                    ))
    return sanitized_url

def generate_shortcode():
    shortcode = ""
    valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
    for _ in range(SHORTCODE_LENGTH):
        shortcode += random.choice(valid_chars)
    return shortcode

def validate_shortcode(shortcode: str):
    has_correct_characters = bool(re.match('^[a-zA-Z0-9_]+$', shortcode))
    has_correct_length = len(shortcode) == SHORTCODE_LENGTH
    return has_correct_length and has_correct_characters
