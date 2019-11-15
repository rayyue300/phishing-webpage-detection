import unittest

from features_extraction import url_and_domain

class IsDomainHavingNonAsciiTest(unittest.TestCase):
    def testGoogle(self):
        self.assertEqual(url_and_domain.isDomainHavingNonAscii('https://google.com'), 0)
    def testChinese(self):
        self.assertEqual(url_and_domain.isDomainHavingNonAscii('https://中文.com'), 1)

class IsShortUrlTest(unittest.TestCase):
    def testGoogle(self):
        self.assertEqual(url_and_domain.isShortUrl('https://google.com'), 0)
    def testBitly(self):
        self.assertEqual(url_and_domain.isShortUrl('https://bit.ly/2WsVM75'), 1)

class IsDeepLevelSubdomainTest(unittest.TestCase):
    def test1dot(self):
        self.assertEqual(url_and_domain.isDeepLevelSubdomain('https://a.b.com'), 1)
    def test2dot(self):
        self.assertEqual(url_and_domain.isDeepLevelSubdomain('https://a.b.c.com/abc.def/'), 2)

class IsLowAlexaRankTest(unittest.TestCase):
    def testGoogle(self):
        self.assertEqual(url_and_domain.isLowAlexaRank('https://google.com'), 1)
    def testYoutube(self):
        self.assertEqual(url_and_domain.isLowAlexaRank('https://youtube.com'), 2)

class IsNotIndexedByGoogle(unittest.TestCase):
    def testGithub(self):
        self.assertEqual(url_and_domain.isNotIndexedByGoogle('https://github.com'), -1)
    def testOthers(self):
        self.assertEqual(url_and_domain.isNotIndexedByGoogle('https://somethingdoesnotexist.com'), 1)

if __name__ == '__main__':
    unittest.main()