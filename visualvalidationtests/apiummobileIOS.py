from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from applitools.eyes import Eyes

class HelloWorld:

    # Initialize the eyes SDK and set your private API key.
    eyes = Eyes()
    eyes.api_key = 'BILoo102mY17vGUvaPXz0jsJiKD8SbdgSz5W101102DaAXmQw110'

    # Set the desired capapbilities.

    desiredCapabilities = {}
    DesiredCapabilities['platformName'] = 'iOS'
    DesiredCapabilities['browserName'] ='Safari'
    DesiredCapabilities['deviceName'] = 'DEVICE_NAME'
    DesiredCapabilities['platformVersion'] = '10.1'
    #desired_caps['automationName'] = 'XCUITest' # Possible to run without.

    # Open browser
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desiredCapabilities)

    try:

        # Start the test.
        eyes.open(driver=driver, app_name='Hello World!', test_name='My first Appium web Python test!')

        # Navigate the browser to the "Hello World!" web-site.
        driver.get(r'https://applitools.com/helloworld')

        # Visual validation point #1.
        eyes.check_window('Hello!')

        # Click the "Click me!" button.
        driver.find_element_by_tag_name('button').click()

        # Visual validation #2.
        eyes.check_window('Click!')

        # End the test.
        eyes.close()

    finally:

        # Close the browser.
        driver.quit()

        # If the test was aborted before eyes.Close was called, end the test as aborted.
        eyes.abort_if_not_closed()
