
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from navigation.navigation import NavigationPage
import time
import requests


class HomePage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)


    # DEFINING LOCATORS OF PAGE ELEMENTS

    _flights_tab = "tab-flight-tab"
    _roundtrip_subTab = "flight-type-roundtrip-label"
    _oneway_subTab = "flight-type-one-way-label"
    _multiDest_subTab = "flight-type-multi-dest-label"
    _flight_origin = "flight-origin"
    _flight_destination = "flight-destination"
    _departing_date = "flight-departing"
    _currentCalendar_month = "//div[@class='datepicker-cal-month'][position()=1]"
    _nextCalendar_month = "//div[@class='datepicker-cal-month'][position()=2]"
    _return_date = "flight-returning"
    _adults = "flight-adults"
    _children = "flight-children"
    _search_button = "search-button"
    _advance_options = "advanced-options"
    _non_stop = "advanced-flight-nonstop"
    _refundable = "advanced-flight-refundable"
    _preferred_airline = "flight-advanced-preferred-airline"
    _preferred_class = "flight-advanced-preferred-class"
    _add_hotel = "flight-add-hotel-checkbox"
    _add_car = "flight-add-car-checkbox"
    _hotel_checkin = "flight-hotel-checkin"
    _hotel_checkOut = "flight-hotel-checkout"
    _no_of_rooms = "flight-hotel-rooms"
    _checkin_adults = "flight-hotel-1-adults"
    _checkin_children = "flight-hotel-1-children"



    def clickFlightsTab(self):
        self.clickElement(self._flights_tab)

    def clickRoundtripSubnav(self):
        self.clickElement(self._roundtrip_subTab)

    def enterdepartAirport(self, fromAirport):
        self.sendKeys(fromAirport, self._flight_origin)

    def enterDestinationAirport(self, toAirport):
        self.sendKeys(toAirport, self._flight_destination)

    def clickDepartDate(self):
        self.clickElement(self._departing_date)
        time.sleep(1)

    def pickDepartDate(self, departDate):
        """
        Checks for the Active Dates in the Current Month and clicks on it
        :return:
        """
        callMonth = self.driver.find_element(By.XPATH, "//div[@class='datepicker-cal-month'][position()=1]")
        ValidDates = callMonth.find_elements(By.CLASS_NAME, "datepicker-cal-date")

        for date in ValidDates:
            if date.text == departDate:
                date.click()
                time.sleep(3)
                break

    def clickReturnDate(self):
        self.clickElement(self._return_date)
        time.sleep(3)

    def pickReturnDate(self, returnDate):
        callMonth = self.driver.find_element(By.XPATH, "//div[@class='datepicker-cal-month'][position()=2]")
        ValidDates = callMonth.find_elements(By.CLASS_NAME, "datepicker-cal-date")

        for date in ValidDates:
            if date.text == returnDate:
                date.click()
                break

    def selectAdults(self, adults):
        element = self.driver.find_element_by_id(self._adults)
        sel = Select(element)
        sel.select_by_value(adults)

    def selectChildren(self, children):
        element = self.driver.find_element_by_id(self._children)
        sel = Select(element)
        sel.select_by_value(children)

    def clickSearchButton(self):
        self.clickElement(self._search_button)

    def aOptionsIsDisplayed(self):
        self.isElementDisplayed(self._advance_options)

    def clickAddOptions(self):
        self.clickElement(self._advance_options)

    def clickNonstop(self):
        self.clickElement(self._non_stop)

    def clickRefundable(self):
        self.clickElement(self._refundable)

    def preferredAirline(self, airline):
        element = self.driver.find_element_by_id(self._preferred_airline)
        sel = Select(element)
        sel.select_by_value(airline)

    def preferredClass(self, classPreference):
        element = self.driver.find_element_by_id(self._preferred_class)
        sel = Select(element)
        sel.select_by_value(classPreference)

    def addHotel(self):
        self.clickElement(self._add_hotel)

    def addCar(self):
        self.clickElement(self._add_car)

    def clickCheckInDate(self):
        self.clickElement(self._hotel_checkin)
        time.sleep(1)

    def pickCheckIntDate(self, checkInDt):
        """
        Checks for the Active Dates in the Current Month and clicks on it
        :return:
        """
        callMonth = self.driver.find_element(By.XPATH, "//div[@class='datepicker-cal-month'][position()=1]")
        ValidDates = callMonth.find_elements(By.CLASS_NAME, "datepicker-cal-date")

        for date in ValidDates:
            if date.text == checkInDt:
                date.click()
                time.sleep(3)
                break

    def clickCheckOutDate(self):
        self.clickElement(self._hotel_checkOut)
        time.sleep(3)


    def pickCheckoutDate(self, checkoutDate):
        callMonth = self.driver.find_element(By.XPATH, "//div[@class='datepicker-cal-month'][position()=2]")
        ValidDates = callMonth.find_elements(By.CLASS_NAME, "datepicker-cal-date")

        for date in ValidDates:
            if date.text == checkoutDate:
                date.click()
                break

    def noOfRooms(self, rooms):
        element = self.driver.find_element_by_id(self._no_of_rooms)
        sel = Select(element)
        sel.select_by_value(rooms)

    def selectCheckInAdults(self, adults):
        element = self.driver.find_element_by_id(self._checkin_adults)
        sel = Select(element)
        sel.select_by_value(adults)

    def selectCheckinChildren(self, children):
        element = self.driver.find_element_by_id(self._checkin_children)
        sel = Select(element)
        sel.select_by_value(children)


    def bookRoundTripFlight(self, fromAirport, toAirport, departDate, returnDate, adults="1", children="0",
                            airline = "", classPreference = ""):
        self.clickFlightsTab()
        self.clickRoundtripSubnav()
        self.enterdepartAirport(fromAirport)
        self.enterDestinationAirport(toAirport)
        self.clickDepartDate()
        self.pickDepartDate(departDate)
        self.clickReturnDate()
        self.pickReturnDate(returnDate)
        self.selectAdults(adults)
        self.selectChildren(children)
        self.pageScroll("up")
        self.clickAddOptions()
        time.sleep(2)
        self.clickNonstop()
        self.clickRefundable()
        self.preferredAirline(airline)
        self.preferredClass(classPreference)


    def addRoundTripOptions(self, checkInDt, checkoutDate, rooms = "1", adults ="1", children= "0"):
        self.addCar()
        self.addHotel()
        self.clickCheckInDate()
        self.pickCheckIntDate(checkInDt)
        self.clickCheckOutDate()
        self.pickCheckoutDate(checkoutDate)
        self.noOfRooms(rooms)
        self.selectCheckInAdults(adults)
        self.selectCheckinChildren(children)


    def verifyHomepageTitle(self):
        self.verifyPageTitle("Expedia Travel: Vacations, Cheap Flights, Airline Tickets & Airfares")

    def nonstopIsSelected(self):
        element = self.driver.find_element_by_id("advanced-flight-nonstop").is_selected()
        return element

    def refundIsSelected(self):
        element = self.driver.find_element_by_id("advanced-flight-refundable").is_selected()
        return element

    def searchButtonIsDisplayed(self):
        self.isElementDisplayed(self._search_button)

    def addHotelIsSelected(self):
        element = self.driver.find_element_by_id("flight-add-hotel-checkbox").is_selected()
        return element

    def addCarIsSelected(self):
        element = self.driver.find_element_by_id("flight-add-car-checkbox").is_selected()
        return element









    def verifyPageLinks(self):

        links = self.driver.find_elements_by_css_selector("a")
        # response_codes = [302, ]

        # Use to this loop to log the list of working Links
        for link in links:
            r = requests.head(link.get_attribute("href"))
            self.log.info(r.status_code == 404)
            time.sleep(0.5)

        # Use this loop to log only the broken Links
        # for link in links:
        #     r = requests.head(link.get_attribute("href"))
        #     if r.status_code != 200:
        #         self.log.info(link.get_attribute("href"))
        #         time.sleep(0.5)



    def verifyBrokenImages(self):
        images = self.driver.find_elements_by_css_selector("img")

        # Use to this loop to log the list of working Images
        for image in images:
            r = requests.head(image.get_attribute("src"))
            print(r.status_code == 200)
            time.sleep(0.5)

        # Use this loop to log only the broken Links
        # for image in images:
        #     r = requests.head(image.get_attribute("href"))
        #     if r.status_code != 200:
        #         self.log.info(image.get_attribute("href"))
        #         time.sleep(0.5)


