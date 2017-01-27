import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _my_courses = "All Courses"
    _all_courses = "My Courses"
    _practice = "Practice"
    _user_settings_icon = "//div[@id='navbar']//li[@class='dropdown']"
    _edit_profile = "//div[@id='navbar']//a[contains(text(),'Edit Profile')]"
    _manage_subs = "//div[@id='navbar']//a[contains(text(),'Manage Subscriptions')]"
    _add_change_cc = "//div[@id='navbar']//a[contains(text(),'Add / Change Credit Card')]"
    _log_out = "//div[@id='navbar']//a[contains(text(),'Log out')]"
    _login = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "//form[@id='new_user']//input[@name='commit']"


    def navigateToAllCourses(self):
        self.clickElement(self._all_courses, locatorType="link")

    def navigateToMyCourses(self):
        self.elementClick(self._my_courses, locatorType="link")

    def navigateToPractice(self):
        self.elementClick(self._practice, locatorType="link")

    def navigateToUserSettings(self):
        user_icon = self.waitForElement(self._user_settings_icon, locatorType="xpath",pollfrequency=1)
        self.elementClick(element=user_icon)

    def navigateToEditProfile(self):
        self.navigateToUserSettings()
        self.elementClick(self._edit_profile, locatorType="xpath")

    def navigateToManageSubs(self):
        self.navigateToUserSettings()
        self.elementClick(self._manage_subs, locatorType="xpath")

    def navigateToAddChangeCC(self):
        self.navigateToUserSettings()
        self.elementClick(self._add_change_cc, locatorType="xpath")

    def navigateToLogOut(self):
        self.navigateToUserSettings()
        logoutLink = self.waitForElement(self._log_out, locatorType="xpath",pollfrequency=1)
        self.elementClick(element=logoutLink)