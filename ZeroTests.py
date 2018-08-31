import time
import unittest
import subprocess

from Pages.AddinsPage import AddinsPage
from Modules.login import login


class ZeroTests(unittest.TestCase):
    driver = None
    outlook = None

    def setUp(self):
        self.driver = subprocess.Popen("C:\\Users\\QA7\\Documents\\Driver\\Winium.Desktop.Driver.exe")
        self.outlook = subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.exe")
        #TODO check if program is loaded

    def test_addin_and_login(self):
        AddinsPage.inst().check_addin_visible()
        login()

    def tearDown(self):
        self.driver.kill()
        print "Closing Windows Desktop Driver on port 9999"
        self.outlook.kill()
        print "Closing Outlook"
