
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests




class LinksTest():
    def test(self):
        baseUrl = "https://www.nytimes.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # try:
        #     links = driver.find_elements_by_css_selector("a")
        #     protocol = "http://"
        #     for link in links:
        #         r = requests.head(link.get_attribute("href"))
        #         url = protocol + str(r)
        #         print(url, r.status_code)
        #     # prints the int of the status code. Find more at httpstatusrappers.com :)
        # except requests.ConnectionError:
        #     print("failed to connect")
       # def checkForBrokenImages(self):
        images = driver.find_elements_by_css_selector("img")

        # Use to this loop to log the list of working Images
        for image in images:
            r = requests.head(image.get_attribute("src"))
            if r.status_code != 200:
                print("The image is: " + str(images) + " & the response code is: " + str(r))
                time.sleep(0.5)

        # links = driver.find_elements_by_css_selector("a")
        # # Use this loop to log only the broken Links
        # for link in links:
        #     r = requests.head(link.get_attribute("href"))
        #     if r.status_code == requests.codes.ok: #r.status_code != 200:
        #         print(link.get_attribute("href"))
        #         time.sleep(1)
        #     elif r.status_code == "None":
        #
        #         continue

link = LinksTest()
link.test()