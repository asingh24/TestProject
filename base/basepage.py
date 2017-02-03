"""
@package base

Base Page class implementation
It implements methods which are common to all the pages throughout the application

This class needs to be inherited by all the page classes
This should not be used by creating object instances

Example:
    Class LoginPage(BasePage)
"""
from base.selenium_driver import PageElements
from traceback import print_stack
from utilities.util import Util
import requests
import time



class BasePage(PageElements):

    def __init__(self, driver):
        """
        Inits BasePage class

        Returns:
            None
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verifyPageTitle(self, titleToVerify):
        """
        Verify the page Title

        Parameters:
            titleToVerify: Title on the page that needs to be verified
        """
        try:
            actualTitle = self.getPageTitle()
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("EXCEPTION: Actual and Expected Page Title Differ")
            #print_stack()
            return False


    # def verifyPageLinks(self):
    #
    #     links = self.driver.find_elements_by_css_selector("a")
    #     jsvoid = "javascript:void(0)"
    #      # Use to this loop to log the list of working Links
    #     for link in links:
    #         r = requests.head(link.get_attribute("href"))
    #         if r.status_code != requests.codes.ok:
    #            self.log.error(link.get_attribute("href"))
    #
    #         elif jsvoid in r.status_code:
    #             continue
            # else:
            #     r.raise_for_status()
            #     continue

            #time.sleep(0.5)

        # Use this loop to log only the broken Links
        # for link in links:
        #     r = requests.head(link.get_attribute("href"))
        #     if r.status_code != 200:
        #         self.log.info(link.get_attribute("href"))
        #         time.sleep(0.5)



    # def checkForBrokenImages(self):
    #     images = self.driver.find_elements_by_css_selector("img")
    #
    #     # Use to this loop to log the list of working Images
    #     for image in images:
    #         r = requests.head(image.get_attribute("src"))
    #         if r.status_code != 200:
    #             self.log.info("The image is: " + str(images) + " & the response code is: " + str(r))
    #         time.sleep(0.5)

        # Use this loop to log only the broken Links
        # for image in images:
        #     r = requests.head(image.get_attribute("href"))
        #     if r.status_code != 200:
        #         self.log.info(image.get_attribute("href"))
        #         time.sleep(0.5)



