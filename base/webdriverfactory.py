
"""

@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()

"""

from selenium import webdriver
import utilities.custom_logger as cl
import logging
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class WebDriverFactory():

    log = cl.customLogger(logging.DEBUG)

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
            driver = webdriver.Ie("C:\\Tools\\Webdrivers\\Microsoft Web Driver\\IEDriverServer\\IEDriverServer.exe")
        elif self.browser == "firefox":
            binary = FirefoxBinary("C:\Program Files (x86)\Mozilla Firefox\\firefox.exe")
            driver = webdriver.Firefox(firefox_binary=binary)
        elif self.browser == "chrome":
            # Set Chrome Driver if Environment variable chrome driver path is not set
            driver = webdriver.Chrome("C:\\Tools\\Webdrivers\\chromedriver\\chromedriver.exe")
        elif self.browser == "phantom":
            driver = webdriver.PhantomJS("C:\\Tools\\Webdrivers\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
        else:
            binary = FirefoxBinary("C:\Program Files (x86)\Mozilla Firefox\\firefox.exe")
            driver = webdriver.Firefox(firefox_binary=binary)
        # Setting Driver Implicit Time out for an Element based on the connection speed
        driver.implicitly_wait(3)
        # Maximize the browser window
        driver.maximize_window()
        # Loading browser with the App URL
        driver.get(baseurl)
        self.log.info("RUNNING TESTS ON: " + str(driver).upper())
        return driver
