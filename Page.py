import time
import unittest


class Page(object):
    "Page class that all page models can inherit from"

    def __init__(self, selenium_driver, base_url='https://mail.google.com/'):
        "Constructor"
        # We assume relative URLs start without a / in the beginning
        self.driver = selenium_driver
        # Visit and initialize xpaths for the appropriate page

    def get_xpath(self, xpath):
        "Return the DOM element of the xpath OR the 'None' object if the element is not found"

    def click_element(self, element):
        element.click()

    def wait(self, wait_seconds=5):
        " Performs wait for time provided"
        time.sleep(wait_seconds)