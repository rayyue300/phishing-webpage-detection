import unittest

from features_extraction import url_and_domain

class IsDomainHavingNonAsciiTest(unittest.TestCase):
    def testGoogle(self):
        self.assertFalse(url_and_domain.isDomainHavingNonAscii('https://google.com'))
    def testChinese(self):
        self.assertTrue(url_and_domain.isDomainHavingNonAscii('https://中文.com'))

class IsShortUrlTest(unittest.TestCase):
    def testGoogle(self):
        self.assertFalse(url_and_domain.isShortUrl('https://google.com'))
    def testBitly(self):
        self.assertTrue(url_and_domain.isShortUrl('https://bit.ly/2WsVM75'))

if __name__ == '__main__':
    unittest.main()