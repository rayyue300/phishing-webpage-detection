# This file is responsible to extract keyword based features from the given URL

from common import utils

# General Function
def isStringInPage(url: str, searchTarget: str) -> int:
    """Return 1 if the the searchTarget exists in the page of the given URL"""
    source = utils.getLoadedHtmlFromUrl(url)
    return 1 if searchTarget in source else 0

def isPageContainingLogin(url: str) -> int:
    """Return 1 if the page contains 'login' in the page of the given URL"""
    resultSmallLetter = isStringInPage(url, 'login')
    resultCapitalLetter = isStringInPage(url, 'Login')
    return resultSmallLetter or resultCapitalLetter

def isPageContainingCreditCard(url: str) -> int:
    """Return 1 if the page contains 'credit card' in the page of the given URL"""
    result1 = isStringInPage(url, 'credit card')
    result2 = isStringInPage(url, 'credit-card')
    result3 = isStringInPage(url, 'Credit Card')
    result4 = isStringInPage(url, 'Credit card')
    return result1 or result2 or result3 or result4

def isPageContainingDownload(url: str) -> int:
    """Return 1 if the page contains 'download' in the page of the given URL"""
    resultSmallLetter = isStringInPage(url, 'download')
    resultCapitalLetter = isStringInPage(url, 'Download')
    return resultSmallLetter or resultCapitalLetter

def isPageContainingUrgent(url: str) -> int:
    """Return 1 if the page contains 'urgent' in the page of the given URL"""
    result1 = isStringInPage(url, 'urgent')
    result2 = isStringInPage(url, 'Urgent')
    result3 = isStringInPage(url, 'URGENT')
    return result1 or result2 or result3

def isPageContainingActionRequired(url: str) -> int:
    """Return 1 if the page contains 'action required' in the page of the given URL"""
    result1 = isStringInPage(url, 'action required')
    result2 = isStringInPage(url, 'Action Required')
    result3 = isStringInPage(url, 'ACTION REQUIRED')
    return result1 or result2 or result3