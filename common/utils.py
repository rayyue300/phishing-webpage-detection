from urllib.parse import urlparse
import tldextract
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def isAscii(s: str) -> bool:
    """Return True if s contains ASCII characters only"""
    try:
        s.encode('ascii')
        return True
    except UnicodeEncodeError:
        return False

def getDomainFromUrl(u: str) -> str:
    """Return the domain part of the given URL"""
    return urlparse(u).netloc

def getSubdomainFromDomain(d: str) -> str:
    """
    Return the subdomain part of the given domain
    e.g. a.b.c.com returns a.b
    """
    return tldextract.extract(d).subdomain
    
def getHttpResponse(u: str) -> str:
    """
    Return the HTTP response of the given url
    """
    return urlopen(u).read()

def getLoadedHtmlFromUrl(u: str) -> str:
    """
    Return HTML content of the given url after the page being loaded
    """
    options = Options()
    options.headless = True

    driver = webdriver.Firefox(options=options)
    driver.get(u)
    driver.implicitly_wait(30)
    source = driver.page_source
    driver.quit()
    return source

#print (getLoadedHtmlFromUrl('https://google.com'))