# This file is responsible to extract URL and domain based features from the given URL.

from common import utils

def isDomainHavingNonAscii(domain):
    """Return True if the given domain contains ASCII characters only"""
    return not utils.isAscii(domain)