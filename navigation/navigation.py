import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _flights_tab =  "tab-flight-tab-hp" or "tab-flight-tab"
    _roundtrip_subTab = "gcw-packages-form-hp-package" or "flight-type-roundtrip-label"


    def bookRoundTrip(self):
        self.clickElement(self._flights_tab)
        self.clickElement(self._roundtrip_subTab)