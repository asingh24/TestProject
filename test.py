from selenium.webdriver.common.by import By

class SDriver():

    def __init__(self, driver):
        self.driver = driver

    def getPageTitle(self):
        return self.driver.title

    def getByType(self, locatorType):

        locatorType = locatorType.lower()

        if locatorType == "xpath":
            return By.XPATH
        elif locatorType == "id":
            return By.ID
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "tag":
            return By.TAG_NAME
        elif locatorType == "plink":
            return By.PARTIAL_LINK_TEXT
        else:
            print("The Locator Type provide: " + locatorType + " is invalid")
        return False

    def getElement(self, locator = "", locatorType = "id"):
        locatorType = locatorType.lower()
        element = None
        try:
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("The Element was found with locator: " + locator + " and locatorType: " + locatorType)
        except:
            print("The Element was NOTfound with locator: " + locator + " and locatorType: " + locatorType)
        return element


    def clickElement(self, locator = "", locatorType = "id", element = None):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            print("The Element was clicked with locator: " + locator + " and locatorType: " + locatorType)
        except:
            print("The Elements was NOT clicked with locator: " + locator + " and locatorType: " + locatorType)
            #print_stack

    def sendKeys(self, data, locator = "", locatorType = "id", element = None):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            print("Data sent to Element with locator: " + locator + " and locatorType: " + locatorType)
        except:
            print("Data was NOT sent to element with locator: " + locator + " and locatorType: " + locatorType)
            #print_stack


    def getElements(self, locator, locatorType = "id"):
        locatorType = locatorType.lower()
        elements = None
        try:
            byType = self.getByType(locatorType)
            elements = self.driver.find_elements(byType, locator)
            print("The Elements were found with locator: " + locator + " and locatorType: " + locatorType)
        except:
            print("The Elements were NOT found with locator: " + locator + " and locatorType: " + locatorType)
        return elements

    def elementPresent(self, locator, locatorType = "id"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                print("The Element exists with locator: " + locator + " and locatorType: " + locatorType)
                return True
            else:
                print("The Element does not exists with locator: " + locator + " and locatorType: " + locatorType)
                return False
        except:
            print("The Element does not exist in the DOM with locator: " + locator + " and locatorType: " + locatorType)
        return False

    def elementsPresent(self, locator, locatorType = "id"):
        try:
            elements = self.getElements(locator, locatorType)
            if len(elements) > 0:
                print("The Element exists with locator: " + locator + " and locatorType: " + locatorType)
                return True
            else:
                print("The Element does not exists with locator: " + locator + " and locatorType: " + locatorType)
                return False
        except:
            print("The Element does not exist in the DOM with locator: " + locator + " and locatorType: " + locatorType)
        return False