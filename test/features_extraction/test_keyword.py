import unittest

from features_extraction import keyword

class IsStringInPageTest(unittest.TestCase):
    def testGoogleContainGoogle(self):
        self.assertEqual(keyword.isStringInPage('https://google.com','Google'), 1)
    def testGoogleContainApple(self):
        self.assertEqual(keyword.isStringInPage('https://google.com','Apple'), 0)

class IsPageContainingLoginTest(unittest.TestCase):
    def testW3LoginTutorial(self):
        self.assertEqual(keyword.isPageContainingLogin('https://www.w3schools.com/howto/howto_css_login_form.asp'), 1)
    def testW3Home(self):
        self.assertEqual(keyword.isPageContainingLogin('https://www.w3schools.com/'), 0)

class IsPageContainingCreditCardTest(unittest.TestCase):
    def testHKBEA(self):
        self.assertEqual(keyword.isPageContainingCreditCard('https://www.hkbea.com/html/en/index.html'), 1)
    def testHKO(self):
        self.assertEqual(keyword.isPageContainingCreditCard('https://www.hko.gov.hk/en/index.html'), 0)

class IsPageContainingDownloadTest(unittest.TestCase):
    def testGoogleChrome(self):
        self.assertEqual(keyword.isPageContainingDownload('https://www.google.com/chrome/'), 1)
    def testLoremIpsum(self):
        self.assertEqual(keyword.isPageContainingDownload('https://www.lipsum.com/'), 0)

class IsPageContainingUrgentTest(unittest.TestCase):
    def testDictionary(self):
        self.assertEqual(keyword.isPageContainingUrgent('https://dictionary.cambridge.org/us/dictionary/english/urgent'), 1)
    def testGoogle(self):
        self.assertEqual(keyword.isPageContainingUrgent('https://google.com/'), 0)

class IsPageContainingActionRequiredTest(unittest.TestCase):
    def testUCLA(self):
        self.assertEqual(keyword.isPageContainingActionRequired('https://www.it.ucla.edu/security/alerts/phishing-scams/re-action-required-udpdate-your-payment-information-now'), 1)
    def testGoogle(self):
        self.assertEqual(keyword.isPageContainingActionRequired('https://google.com/'), 0)