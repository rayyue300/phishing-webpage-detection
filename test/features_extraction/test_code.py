import unittest

from features_extraction import code

class IsUsingManyExternalResourcesTest(unittest.TestCase):
    def testGoogle(self):
        self.assertEqual(code.isUsingManyExternalResources('https://google.com'), 0)
    def testGithub(self):
        self.assertEqual(code.isUsingManyExternalResources('https://github.com'), 1)

class IsRedirectingToOtherDomainTest(unittest.TestCase):
    def testGoogle(self):
        self.assertEqual(code.isRedirectingToOtherDomain('https://google.com'), 0)
    def testGooGl(self):
        self.assertEqual(code.isRedirectingToOtherDomain('https://goo.gl'), 1)

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

class IsBlockingRightClickTest(unittest.TestCase):
    def testGoogle(self):
        self.assertEqual(code.isBlockingRightClick('https://google.com'), 0)
    def testBody(self):
        self.assertEqual(code.isBlockingRightClick('https://rayyue300.github.io/phishing-webpage-detection-test-resources/BlockRightClickByBody.html'), 1)
    def testJs(self):
        self.assertEqual(code.isBlockingRightClick('https://rayyue300.github.io/phishing-webpage-detection-test-resources/BlockRightClickByJs.html'), 1)

class IsUsingInceptionBarTest(unittest.TestCase):
    def testWithInceptionBar(self):
        self.assertEqual(code.isUsingInceptionBar('https://jameshfisher.com/2019/04/27/the-inception-bar-a-new-phishing-method/'), 1)
    def testGoogle(self):
        self.assertEqual(code.isUsingInceptionBar('https://google.com/'), 0)

if __name__ == '__main__':
    unittest.main()