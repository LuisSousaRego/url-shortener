from urllib.parse import urlparse

def sanitize_url(url):
    parsed_url = urlparse(url)
    return parsed_url.geturl()