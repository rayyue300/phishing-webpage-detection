import unittest

from features_extraction import url_and_domain

class IsDomainHavingNonAsciiTest(unittest.TestCase):
    def testGoogle(self):
        self.assertFalse(url_and_domain.isDomainHavingNonAscii('google.com'))
    def testChinese(self):
        self.assertTrue(url_and_domain.isDomainHavingNonAscii('中文.com'))

if __name__ == '__main__':
    unittest.main()