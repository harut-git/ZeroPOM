import time
import unittest


class BasePage(unittest.TestCase):
    "Page class that all page models can inherit from"

    def __init__(self, selenium_driver):
        "Constructor"
        # We assume relative URLs start without a / in the beginning
        self.driver = selenium_driver
        # Visit and initialize xpaths for the appropriate page

    def get_name(self, name):
        return self.driver.find_element_by_name(name)

    def get_xpath(self, xpath):
        "Return the DOM element of the xpath OR the 'None' object if the element is not found"

    def click_element(self, xpath):
        "Click the button supplied"

    def wait(self, wait_seconds=5):
        " Performs wait for time provided"
        time.sleep(wait_seconds)