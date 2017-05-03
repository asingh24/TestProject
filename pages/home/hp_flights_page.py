
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

    _oneway_subTab = "flight-type-one-way-label-hp-flight"
    _multiDest_subTab = "flight-type-multi-dest-label-hp-flight"
    _flight_origin = "flight-origin-hp-flight"
    _flight_destination = "flight-destination-hp-flight"
    _departing_date = "flight-departing-hp-flight"
    _currentCalendar_month = "//div[@class='datepicker-cal-month'][position()=1]"
    _nextCalendar_month = "//div[@class='datepicker-cal-month'][position()=2]"
    #_nextCalendar_page = "//div[@id='flight-departing-wrapper-hp-flight']//button[@class='datepicker-paging datepicker-next btn-paging btn-secondary next']"
    _return_date = "flight-returning-hp-flight"
    _adults = "flight-adults-hp-flight"
    _children = "flight-children-hp-flight"
    _advance_options = "flight-advanced-options-hp-flight"
    _non_stop = "advanced-flight-nonstop-hp-flight"
    _refundable = "advanced-flight-refundable-hp-flight"
    _preferred_airline = "flight-advanced-preferred-airline-hp-flight"
    _preferred_class = "flight-advanced-preferred-class-hp-flight"
    _add_hotel = "flight-add-hotel-checkbox-hp-flight"
    _add_car = "flight-add-car-checkbox-hp-flight"
    _hotel_checkin = "flight-hotel-checkin-hp-flight"
    #_hotel_checkin_nextpage = "//div[@id='flight-hotel-checkin-wrapper-hp-flight']//button[@class='datepicker-paging datepicker-next btn-paging btn-secondary next']"
    _hotel_checkOut = "flight-hotel-checkout-hp-flight"
    #_hotel_checkout_nextpage = "//div[@id='flight-hotel-checkout-wrapper-hp-flight']//button[@class='datepicker-paging datepicker-next btn-paging btn-secondary next']"
    _no_of_rooms = "flight-hotels-rooms-hp-flight"
    _checkin_adults = "flight-hotel-1-adults-hp-flight"
    _checkin_children = "flight-hotel-1-children-hp-flight"
    _search_button = "//form[@id='gcw-flights-form-hp-flight']//button[@type='submit']"
    _search_property = "inpHotelNameMirror"
    _sort_price = "//div[@id='sortContainer']//button[@aria-label='Sort by: Price']"


    def navigateToRoundTrip(self):
        self.nav.bookRoundTrip()

    def enterdepartAirport(self, fromAirport):
        self.clickElement(self._flight_origin)
        time.sleep(2)
        self.sendKeys(fromAirport, self._flight_origin)

    def enterDestinationAirport(self, toAirport):
        self.clickElement(self._flight_destination)
        time.sleep(2)
        self.sendKeys(toAirport, self._flight_destination)

    def clickDepartDate(self):
        self.clickElement(self._departing_date)
        time.sleep(2)

    def pickDepartDate(self, departDate):
        """
        Checks for the Active Dates in the Current Month and clicks on it
        :return:
        """
        callMonth = self.driver.find_element(By.XPATH, "//div[@class='datepicker-cal-month'][position()=2]")
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
        callMonth = self.driver.find_element(By.XPATH, "//div[@class='datepicker-cal-month'][position()=2]")
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
        self.clickElement(self._search_button, locatorType="xpath")
        time.sleep(3)

    def handleWindowPopup(self):
        # Find Parent Window handle (The Main Window)
        parentHandle = self.driver.current_window_handle
        self.log.info("Parent Window Handle is: " + parentHandle)
        # Find all handles, there should be two handles after clicking the open window button above and switch to other
        # window to perform actions
        handles = self.driver.window_handles
        for handle in handles:
            #self.log.info("Handle: " + handle)
            if handle not in parentHandle:
                self.driver.switch_to.window(handle)
                self.driver.close()
                break
        # Switch back to Parent window
        self.driver.switch_to.window(parentHandle)

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

    def pickCheckIntDate(self, checkInDt):
        """
        Checks for the Active Dates in the Current Month and clicks on it
        :return:
        """
        callMonth = self.driver.find_element(By.XPATH, "//div[@class='datepicker-cal-month'][position()=2]")
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


    def click_search(self):
        self.clickSearchButton()
        self.handleWindowPopup()
        self.waitForSearchProperty()
        self.clickSortByPrice()

    def verifyHomepageTitle(self):
        return self.verifyPageTitle("Expedia Travel: Vacations, Cheap Flights, Airline Tickets & Airfares")


    def nonStopIsDisplayed(self):
        return self.isElementDisplayed(self._non_stop)

    def refundIsDisplayed(self):
        return self.isElementDisplayed(self._refundable)

    def searchButtonIsPresent(self):
        return self.elementPresent(self._search_button)


    def addHotelIsSelected(self):
        return self.isSelected(self._add_hotel)

    def addCarIsSelected(self):
        return self.isSelected(self._add_car)