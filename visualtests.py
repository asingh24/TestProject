from needle.cases import NeedleTestCase
from needle.driver import NeedleChrome
from needle.driver import NeedlePhantomJS
from needle.driver import NeedleSafari


class BBCNewsTest(NeedleTestCase):
    cleanup_on_success = True # DELETES SCREENSHOTS IF THE RESULT IS A SUCCESS, DEFAULT VALUE IS SET TO FALSE

    @classmethod
    def get_web_driver(cls):
        return NeedleChrome()

    def test_masthead(self):
        self.baseurl = 'http://www.bbc.co.uk/news/'
        self.driver.get(self.baseurl)

        self.assertScreenshot('#orb-header', 'bbc-masthead')
        self.assertScreenshot(".site-brand.site-brand--height", 'bbc-masthead-1')




