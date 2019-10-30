import unittest

from common import utils

class IsAsciiTest(unittest.TestCase):
    def testEnglish(self):
        self.assertTrue(utils.isAscii('test'))
    def testChinese(self):
        self.assertFalse(utils.isAscii('測試'))
    def testLookAlike(self):
        self.assertFalse(utils.isAscii('àéç'))

class GetDomainFromUrlTest(unittest.TestCase):
    def testDomain(self):
        self.assertEqual(utils.getDomainFromUrl('https://www.google.com/'), 'www.google.com')
    def testDomainWithDirectory(self):
        self.assertEqual(utils.getDomainFromUrl('https://github.com/rayyue300/phishing-webpage-detection'), 'github.com')

if __name__ == '__main__':
    unittest.main()