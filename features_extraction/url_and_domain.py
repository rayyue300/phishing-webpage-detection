# This file is responsible to extract URL and domain based features from the given URL.

import re
from bs4 import BeautifulSoup
from googlesearch import search

from common import utils

def isDomainHavingNonAscii(url: str) -> int:
    """Return 1 if the domain of the given url contains ASCII characters only"""
    domain = utils.getDomainFromUrl(url)
    return 1 if not utils.isAscii(domain) else 0

def isShortUrl(url: str) -> int:
    """Return 1 if the given url is a short URL"""
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
    return 1 if re.search(shortUrlList, url) else 0

def isDeepLevelSubdomain(url: str) -> int:
    """
    Return the no. of levels of subdomain of the given url
    e.g. abcbank.com.somedomain.com returns 2
    """
    domain = utils.getDomainFromUrl(url)
    return utils.getSubdomainFromDomain(domain).count('.')+1

def isLowAlexaRank(url: str) -> int:
    """
    Return the Alexa rank number of the given url
    e.g. google.com returns 1
    """
    # The API is the one used in the Alexa toolbar
    APIURL = "http://data.alexa.com/data?cli=10&dat=s&url="
    try:
        apiResult = utils.getHttpResponse(APIURL+url)
        rank = int(BeautifulSoup(apiResult, "xml").find("REACH")['RANK'])
    except:
        return -1
    return rank

def isNotIndexedByGoogle(url: str) -> int:
    """
    Return 1 if searching 'site:url' in Google returns NO results
    Return 0 if there are results but the domains are not matched
    Return -1 if there are results and the domains are matched

    Remarks: 
    This feature is not accurate because it's using domain instead of url.
    The url from google may have slight difference with the given url.
    (e.g. 'https://abc.com/' VS 'https://www.abc.com')
    """
    try:
        domain = utils.getDomainFromUrl(url)
        results = search(query="site:"+domain, stop=5)
        
        noOfResults = 0

        for result in results:
            noOfResults += 1
            if utils.getDomainFromUrl(str(result))==domain:
                return -1
        
        if noOfResults == 0:
            return 1
        return 0
    except:
        return -1