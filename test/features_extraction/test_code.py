import unittest

from features_extraction import code

class IsHavingManyRedirectionsTest(unittest.TestCase):
    def testGoogle(self):
        self.assertEqual(code.isUsingManyExternalResources('https://google.com'), 0)
    def testGithub(self):
        self.assertEqual(code.isUsingManyExternalResources('https://github.com'), 1)
    #def testGoogle(self):
        #self.assertEqual(url_and_domain.isDomainHavingNonAscii('https://google.com'), 0)
    #def testChinese(self):
        #self.assertEqual(url_and_domain.isDomainHavingNonAscii('https://中文.com'), 1)


if __name__ == '__main__':
    unittest.main()