from TestProject.pages.home.hp_flights_page import FlightRTBundle
import unittest
import pytest
from TestProject.utilities.statustests import StatusTests


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RoundTrip(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = FlightRTBundle(self.driver)
        self.ts = StatusTests(self.driver)

    @pytest.mark.run(order=1)
    def test_flightRoundTrip(self):

        result2 = self.hp.verifyHomepageTitle()
        self.ts.mark(result2, "The Actual and Expected Titles Differ")
        self.hp.bookRoundTripFlight("Philadelphia, PA (PHL-Philadelphia Intl.)", "Las Vegas, NV (LAS-McCarran Intl.)",
                                    "27", "7", "2")
        result3 = self.hp.aOptionsIsDisplayed()
        self.ts.mark(result3, "Add Options Link is displayed")
        result4 = self.hp.nonStopIsDisplayed()
        self.ts.mark(result4, "NonStop Checkbox is displayed")
        result5 = self.hp.refundIsDisplayed()
        self.ts.mark(result5, "Refund Flight checkbox is displayed")
        self.hp.addRoundTripOptions("27", "7", adults="2")
        result6 = self.hp.addHotelIsSelected()
        self.ts.mark(result6, "Add Hotel Checkbox is Selected")
        result7 = self.hp.addCarIsSelected()
        self.ts.markFinal("FLIGHT ROUNDTRIP BUNDLE FLOW: ",result7, " All Checks completed  --- PASSED ")
        self.hp.click_search()






