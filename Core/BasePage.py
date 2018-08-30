import time
import unittest

from selenium import webdriver

from Base.SingletonPattern import Singleton


class BasePage(unittest.TestCase):

    def __init__(self):
        "Constructor"
        self.driver = webdriver.Remote(
            command_executor='http://localhost:9999',
            desired_capabilities={
                "debugConnectToRunningApp": 'true',
            })
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