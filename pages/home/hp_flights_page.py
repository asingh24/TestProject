
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from navigation.navigation import NavigationPage
import time
import requests


class FlightRTBundle(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)


    # DEFINING LOCATORS OF PAGE ELEMENTS


    _oneway_subTab = "flight-type-one-way-label"
    _multiDest_subTab = "flight-type-multi-dest-label"
    _flight_origin = "flight-origin"
    _flight_destination = "flight-destination"
    _departing_date = "flight-departing"
    _currentCalendar_month = "//div[@class='datepicker-cal-month'][position()=1]"
    _nextCalendar_month = "//div[@class='datepicker-cal-month'][position()=2]"
    _nextCalendar_page = "//div[@id='flight-departing-wrapper']//span[@class='icon icon-pagenext']"
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
    _hotel_checkin_nextpage = "//div[@id='flight-hotel-checkin-wrapper']//span[@class='icon icon-pagenext']"
    _hotel_checkOut = "flight-hotel-checkout"
    _no_of_rooms = "flight-hotel-rooms"
    _checkin_adults = "flight-hotel-1-adults"
    _checkin_children = "flight-hotel-1-children"
    _search_property = "inpHotelNameMirror"
    _sort_price = "//div[@id='sortContainer']//button[@aria-label='Sort by: Price']"



    def navigateToRoundTrip(self):
        self.nav.bookRoundTrip()

    def enterdepartAirport(self, fromAirport):
        self.sendKeys(fromAirport, self._flight_origin)

    def enterDestinationAirport(self, toAirport):
        self.sendKeys(toAirport, self._flight_destination)

    def clickDepartDate(self):
        self.clickElement(self._departing_date)
        time.sleep(2)
        self.clickElement(self._nextCalendar_page, locatorType="xpath")
        time.sleep(2)

    def pickDepartDate(self, departDate):
        """
        Checks for the Active Dates in the Current Month and clicks on it
        :return:
        """
        callMonth = self.getElement(locator="//div[@class='datepicker-cal-month'][position()=1]", locatorType="xpath")
        #callMonth = self.driver.find_element(By.XPATH, "//div[@class='datepicker-cal-month'][position()=1]")
        validDates = callMonth.find_elements(By.CLASS_NAME, "datepicker-cal-date")


        for date in validDates:
            if date.text == departDate:
                date.click()
                time.sleep(3)
                break

    def clickReturnDate(self):
        self.clickElement(self._return_date)
        time.sleep(3)

    def pickReturnDate(self, returnDate):
        callMonth = self.getElement(locator="//div[@class='datepicker-cal-month'][position()=2]", locatorType="xpath")
        #callMonth = self.driver.find_element(By.XPATH, "//div[@class='datepicker-cal-month'][position()=2]")
        validDates = callMonth.find_elements(By.CLASS_NAME, "datepicker-cal-date")

        for date in validDates:
            if date.text == returnDate:
                date.click()
                break

    def selectAdults(self, adults):
        element = self.getElement(self._adults)
        sel = Select(element)
        sel.select_by_value(adults)

    def selectChildren(self, children):
        element = self.getElement(self._children)
        sel = Select(element)
        sel.select_by_value(children)

    def clickSearchButton(self):
        self.clickElement(self._search_button)

    def aOptionsIsDisplayed(self):
        return self.isElementDisplayed(self._advance_options)

    def clickAddOptions(self):
        self.clickElement(self._advance_options)

    def clickNonstop(self):
        self.clickElement(self._non_stop)

    def clickRefundable(self):
        self.clickElement(self._refundable)

    def preferredAirline(self, airline):
        element = self.getElement(self._preferred_airline)
        sel = Select(element)
        sel.select_by_value(airline)

    def preferredClass(self, classPreference):
        element = self.getElement(self._preferred_class)
        sel = Select(element)
        sel.select_by_value(classPreference)

    def addHotel(self):
        self.clickElement(self._add_hotel)

    def addCar(self):
        self.clickElement(self._add_car)

    def clickCheckInDate(self):
        self.clickElement(self._hotel_checkin)
        time.sleep(2)
        self.clickElement(self._hotel_checkin_nextpage, locatorType="xpath")
        time.sleep(2)

    def pickCheckIntDate(self, checkInDt):
        """
        Checks for the Active Dates in the Current Month and clicks on it
        :return:
        """
        callMonth = self.getElement(locator="//div[@class='datepicker-cal-month'][position()=1]", locatorType="xpath")
        #callMonth = self.driver.find_element(By.XPATH, "//div[@class='datepicker-cal-month'][position()=1]")
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
        callMonth = self.getElement(locator="//div[@class='datepicker-cal-month'][position()=2]", locatorType="xpath")
        #callMonth = self.driver.find_element(By.XPATH, "//div[@class='datepicker-cal-month'][position()=2]")
        validDates = callMonth.find_elements(By.CLASS_NAME, "datepicker-cal-date")

        for date in validDates:
            if date.text == checkoutDate:
                date.click()
                break

    def noOfRooms(self, rooms):
        element = self.getElement(self._no_of_rooms)
        sel = Select(element)
        sel.select_by_value(rooms)

    def selectCheckInAdults(self, adults):
        element = self.getElement(self._checkin_adults)
        sel = Select(element)
        sel.select_by_value(adults)

    def selectCheckinChildren(self, children):
        element = self.getElement(self._checkin_children)
        sel = Select(element)
        sel.select_by_value(children)

    def waitForSearchProperty(self):
        self.waitForElement(self._search_property, timeout=50)

    def clickSortByPrice(self):
        element = self.waitForElement(self._sort_price, locatorType="xpath")
        element.click()
        self.waitForElement(self._sort_price, locatorType="xpath", timeout=40)


    def bookRoundTripFlight(self, fromAirport, toAirport, departDate, returnDate, adults="1", children="0",
                            airline = "", classPreference = ""):

        self.navigateToRoundTrip()
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
        self.pageScroll("up")


    def search(self):
        self.clickSearchButton()
        self.waitForSearchProperty()
        self.clickSortByPrice()

    def verifyHomepageTitle(self):
        return self.verifyPageTitle("Expedia Travel: Vacations, Cheap Flights, Airline Tickets & Airfares")


    def nonStopIsDisplayed(self):
        return self.isElementDisplayed(self._non_stop)

    # def nonstopIsSelected(self):
    #     self.isSelected(self._non_stop)
    #     # element = self.driver.find_element_by_id("advanced-flight-nonstop").is_selected()
    #     # return element

    def refundIsDisplayed(self):
        return self.isElementDisplayed(self._refundable)

    # def refundIsSelected(self):
    #     self.isSelected(self._refundable)
    #     # element = self.driver.find_element_by_id("advanced-flight-refundable").is_selected()
    #     # return element

    def searchButtonIsDisplayed(self):
        return self.isElementDisplayed(self._search_button)


    def addHotelIsSelected(self):
        return self.isSelected(self._add_hotel)
        # element = self.driver.find_element_by_id("flight-add-hotel-checkbox").is_selected()
        # return element

    def addCarIsSelected(self):
        return self.isSelected(self._add_car)
        # element = self.driver.find_element_by_id("flight-add-car-checkbox").is_selected()
        # return element