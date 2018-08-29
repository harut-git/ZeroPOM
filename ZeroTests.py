import time
import unittest
from Core.Driver import Driver
from Pages.RibbonPage import RibbonPage


class ZeroTests(unittest.TestCase):

    def setUp(self):
        driver_obj = Driver()
        driver_obj.start_driver()
        self.driver = driver_obj.driver

    def test_addin(self):
        time.sleep(10)
        RibbonPage(self.driver).check_addin()