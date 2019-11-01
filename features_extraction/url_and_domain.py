# This file is responsible to extract URL and domain based features from the given URL.

import re

from common import utils

def isDomainHavingNonAscii(url: str) -> bool:
    """Return True if the domain of the given url contains ASCII characters only"""
    domain = utils.getDomainFromUrl(url)
    return not utils.isAscii(domain)

def isShortUrl(url: str) -> bool:
    """Return True if the given url is a short URL"""
    # Reference of the list:
    # https://github.com/philomathic-guy/Malicious-Web-Content-Detection-Using-Machine-Learning/blob/master/patterns.py
    shortUrlList = r"bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|" \
                r"yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|" \
                r"short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|" \
                r"doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|db\.tt|" \
                r"qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|q\.gs|is\.gd|" \
                r"po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|x\.co|" \
                r"prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|" \
                r"tr\.im|link\.zip\.net"
    return re.search(shortUrlList, url)