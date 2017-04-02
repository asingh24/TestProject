
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from TestProject.utilities import custom_logger as cl
import logging
import os
import time


class PageElements():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot saved to directory: " + destinationFile)
        except:
            self.log.error("EXCEPTION: When taking The Screenshot")
            print_stack()

    def getPageTitle(self):
       return self.driver.title


    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "tag":
            return By.TAG_NAME
        else:
            self.log.error("The Locator Type: " + locatorType + " is invalid.")
        return False


    def getElement(self, locator = "", locatorType = "id"):
        locatorType = locatorType.lower()
        element = None
        try:
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator + " and locator type: " + locatorType)
        except:
            self.log.error("EXCEPTION: Element NOT found with locator: " + locator + " and locator type: " + locatorType)
        return element


    def clickElement(self, locator = "", locatorType ="id", element = None):
        try:
            if locator: # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on the Element with Locator: " + locator + " and Locator Type: " + locatorType)
        except:
            self.log.error("EXCEPTION: Cannot click on the element with Locator: " + locator + " and Locator Type: " +
                           locatorType)
            #print_stack()


    def sendKeys(self, data, locator = "", locatorType ="id", element = None):
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Data sent to the Element with Locator: " + locator + " and Locator Type: " + locatorType)
        except:
            self.log.error("EXCEPTION: Cannot send data to element with Locator: " + locator + " and Locator Type: " +
                           locatorType)
            #print_stack()


    def isSelected(self, locator = "", locatorType = "id", element = None):
        try:
            element = self.getElement(locator, locatorType)
            checkBox = element.get_attribute("checked")
            #checkBox = element.is_selected()

            if checkBox:
                self.log.info("Element is Selected with locator: " + locator + " and locator type: " + locatorType)
                return True
            else:
                self.log.info("Element is NOT Selected with locator: " + locator + " and locator type: " + locatorType)
                return False
        except:
            self.log.error("EXCEPTION: Element is NOT SELECTED")


    def getElements(self, locator = "", locatorType = "id"):
        locatorType = locatorType.lower()
        elements = None
        try:
            byType = self.getByType(locatorType)
            elements = self.driver.find_elements(byType, locator)
            self.log.info("Element found with locator: " + locator + " and locator type: " + locatorType)
        except:
            self.log.error("EXCEPTION: Element NOT found with locator: " + locator + " and locator type: " + locatorType)
        return elements


    def elementPresent(self, locator = "", locatorType = "id", element = None):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element is present with locator: " + locator + " and locator type: " + locatorType)
                return True
            else:
                self.log.error("Element is NOT present with locator: " + locator + " and locator type: " + locatorType)
                return False
        except:
            self.log.error("EXCEPTION: Element not found in the DOM")
        return False


    def elementsPresent(self, locator = "", locatorType = "id", element = None):
        try:
            elements = self.getElements(locator, locatorType)
            if len(elements) > 0:
                self.log.info("Element's' present with locator: " + locator + " and locator type: " + locatorType)
                return True
            else:
                self.log.error("Element's' NOT present with locator: " + locator + " and locator type: " + locatorType)
                return False
        except:
            self.log.error("EXCEPTION: Element's' not found in the DOM")
        return False


    # IMPLICITLY WAIT FOR AN ELEMENT TO APPEAR BASED ON THE TIME PROVIDED

    def waitForElement(self, locator, locatorType="id", timeout=10, pollfrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for the element to appear")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollfrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                    ElementNotVisibleException,
                                                    ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))

            self.log.info("Element appeared on the page")
        except:
            self.log.error("EXCEPTION: Element did not appear until the WAIT timeout")
            #print_stack()
        return element


    # METHOD FOR SCROLLING THE PAGE UP AND DOWN

    def pageScroll(self, direction="up"):
        """
        NEW METHOD
        """
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")


    # CHECK IF ELEMENT IS DISPLAYED

    def isElementDisplayed(self, locator = "", locatorType = "id", element = None):
        """
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " locatorType: " + locatorType)
                return isDisplayed
            else:
                self.log.error("Element not displayed with locator: " + locator +
                              " locatorType: " + locatorType)
                return isDisplayed

        except:
            self.log.error("EXCEPTION: Element is not displayed and hence was not found")
            return False


    # GET TEXT OF AN ELEMENT

    def getText(self, locator = "", locatorType = "id", element = None, info = ""):
        """
        NEW METHOD
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator: # This means if locator is not empty
                #self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            #self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " +  info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("EXCEPTION: Failed to get text on element " + info)
            print_stack()
            text = None
        return text


    #SCREENSHOT METHOD

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot saved to directory: " + destinationFile)
        except:
            self.log.error("EXCEPTION: Occurred when taking Screenshot")
            print_stack()



