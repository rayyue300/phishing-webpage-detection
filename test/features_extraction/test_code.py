import unittest

from features_extraction import code

class IsHavingManyRedirectionsTest(unittest.TestCase):
    def testGoogle(self):
        self.assertEqual(code.isUsingManyExternalResources('https://google.com'), 0)
    def testGithub(self):
        self.assertEqual(code.isUsingManyExternalResources('https://github.com'), 1)

class IsOpeningNewWindowTest(unittest.TestCase):
    def testGoogle(self):
        # there is a target="_blank"
        self.assertEqual(code.isOpenningNewWindow('https://google.com/'), 1)
    def testBlankOrg(self):
        self.assertEqual(code.isOpenningNewWindow('https://blank.org/'), 0)
    def testExternalJS(self):
        self.assertEqual(code.isOpenningNewWindow('https://cdpn.io/rayyue300/fullpage/NWPwWaa'), 1)
    def testScript(self):
        self.assertEqual(code.isOpenningNewWindow('https://cdpn.io/rayyue300/fullpage/LYEOPgX'), 1)
    def testAnchor(self):
        self.assertEqual(code.isOpenningNewWindow('https://cdpn.io/rayyue300/fullpage/yLyPBEb') ,1)


if __name__ == '__main__':
    unittest.main()