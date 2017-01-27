from pages.home.hp_flights_page import HomePage
import unittest
import pytest
from utilities.statustests import StatusTests
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RoundTrip(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.ts = StatusTests(self.driver)

    @pytest.mark.run(order=1)
    def test_flightRoundTrip(self):
        # result = self.hp.verifyPageLinks()
        # self.ts.mark(result, "Page Links are Validated")
        # result1 = self.hp.verifyBrokenImages()
        # self.ts.mark(result1, "Page images are Validated")


        result2 = self.hp.verifyHomepageTitle()
        self.ts.mark(result2, "Title Verification")
        self.hp.bookRoundTripFlight("Philadelphia, PA (PHL-Philadelphia Intl.)", "Las Vegas, NV (LAS-McCarran Intl.)",
                                    "27", "10", "2")
        result3 = self.hp.aOptionsIsDisplayed()
        self.ts.mark(result3, "Add Options Link is displayed")
        result4 = self.hp.nonstopIsSelected()
        self.ts.mark(result4, "NonStop Checkbox is selected")
        result5 = self.hp.refundIsSelected()
        self.ts.mark(result5, "Refund Flight checkbox is selected")

        self.hp.addRoundTripOptions("27", "10", adults="2")
        result6 = self.hp.addHotelIsSelected()
        self.ts.mark(result6, "Add Hotel Checkbox is Selected")
        result7 = self.hp.addCarIsSelected()
        self.ts.mark(result7, "Add Car Checkbox is selected")
        result8 = self.hp.searchButtonIsDisplayed()
        self.ts.markFinal("test_flightRoundTrip", result8, "PASSED")
        self.hp.clickSearchButton()






