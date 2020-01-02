# This file is responsible to extract code based features from the given URL

from bs4 import BeautifulSoup
from common import utils

def isHavingManyRedirections(url: str) -> int:
    return 0

def isUsingManyExternalResources(url: str) -> int:
    noOfExtRes = 0
    MANY = 30

    source = utils.getLoadedHtmlFromUrl(url)
    soup = BeautifulSoup(source, 'html.parser')
    domain = utils.getDomainFromUrl(url)

    def compileList(soup: str, tag: str, attr: str) -> []:
        outputList = []
        for x in soup.findAll(tag):
            try:
                outputList.append(x[attr])
            except KeyError:
                pass
        return outputList

    imageSources = compileList(soup, 'img', 'src')
    scriptSources = compileList(soup, 'script', 'src')
    styleSources = compileList(soup, 'link', 'href')
    videoSources = compileList(soup, 'video', 'src')
    audioSources = compileList(soup, 'audio', 'src')
    iframeSources = compileList(soup, 'iframe', 'src')
    embedSources = compileList(soup, 'embded', 'src')
    objectSources = compileList(soup, 'object', 'data')
    sourceSources = compileList(soup, 'source', 'src')

    sources = imageSources + scriptSources + styleSources + videoSources + audioSources + iframeSources + embedSources + objectSources + sourceSources

    for s in sources:
        if str(s).startswith('http'):
            if utils.getDomainFromUrl(str(s)) != domain:
                noOfExtRes += 1

    if noOfExtRes >= MANY:
        return 1
    else:
        return 0

def isHavingPopupWindow(url: str) -> int:
    return 0

def isBlockingRightClick(url: str) -> int:
    return 0

def isUsingInceptionBar(int: str) -> int:
    return 0