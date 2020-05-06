# This file is responsible to extract keyword based features from the given URL

from common import utils

# General Function
def isStringInPage(url: str, searchTarget: str) -> int:
    """Return 1 if the the searchTarget exists in the page of the given URL"""
    source = utils.getLoadedHtmlFromUrl(url)
    return 1 if searchTarget in source else 0

def isPageContainingLogin(url: str) -> int:
    """Return 1 if the page contains 'login' in the page of the given URL"""
    source = utils.getLoadedHtmlFromUrl(url)
    result1 = 'login' in source
    result2 = 'Login' in source
    return 1 if (result1 or result2) else 0

def isPageContainingCreditCard(url: str) -> int:
    """Return 1 if the page contains 'credit card' in the page of the given URL"""
    source = utils.getLoadedHtmlFromUrl(url)
    result1 = 'credit card' in source
    result2 = 'credit-card' in source
    result3 = 'Credit Card' in source
    return 1 if (result1 or result2 or result3) else 0

def isPageContainingDownload(url: str) -> int:
    """Return 1 if the page contains 'download' in the page of the given URL"""
    source = utils.getLoadedHtmlFromUrl(url)
    result1 = 'download' in source
    result2 = 'Download' in source
    return 1 if (result1 or result2) else 0

def isPageContainingUrgent(url: str) -> int:
    """Return 1 if the page contains 'urgent' in the page of the given URL"""
    source = utils.getLoadedHtmlFromUrl(url)
    result1 = 'urgent' in source
    result2 = 'Urgent' in source
    result3 = 'URGENT' in source
    return 1 if (result1 or result2 or result3) else 0

def isPageContainingActionRequired(url: str) -> int:
    """Return 1 if the page contains 'action required' in the page of the given URL"""
    source = utils.getLoadedHtmlFromUrl(url)
    result1 = 'action required' in source
    result2 = 'Action Required' in source
    result3 = 'ACTION REQUIRED' in source
    return 1 if (result1 or result2 or result3) else 0