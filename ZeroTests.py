import time
import unittest
import subprocess
from Pages.RibbonPage import RibbonPage


class ZeroTests(unittest.TestCase):
    driver = None
    outlook = None

    def setUp(self):
        self.driver = subprocess.Popen("C:\\Users\\QA7\\Documents\\Driver\\Winium.Desktop.Driver.exe")
        self.outlook = subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.exe")

    def test_addin(self):
        time.sleep(10)
        RibbonPage.inst().check_addin()
        RibbonPage.inst().nd_frame_login()

    def tearDown(self):
        self.driver.kill()
        self.outlook.kill()
