
"""

@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()

"""

from selenium import webdriver


class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    """
    Set chrome driver and iexplorer environment based on OS

    chromedriver = "C:/..../chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    self.driver = webdriver.Chrome(chromedriver)

    PREFERRED: Set the path on the machine where browser wil be executed

    """

    def getWebDriverInstance(self):
        """
        Get WebDriver instance based on the browser configuration
        Returns:
            'WebDriver Instance'
        """
        baseurl = "https://www.expedia.com"

        if self.browser == "iexplorer":
            # Set ie Driver if Environment variable for the ie driver path is not set
            driver = webdriver.Ie("C:\\Browsers\\Microsoft Web Driver\\IEDriverServer\\IEDriverServer.exe")
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # Set Chrome Driver if Environment variable chrome driver path is not set
            driver = webdriver.Chrome("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")
        elif self.browser == "phantom":
            driver = webdriver.PhantomJS("C:\\Python\\phantomjs\\bin\\phantomjs.exe")
        else:
            driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for an Element based on the connection speed
        driver.implicitly_wait(10)
        # Maximize the browser window
        driver.maximize_window()
        # Loading browser with the App URL
        driver.get(baseurl)
        return driver
