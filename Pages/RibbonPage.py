from io import BytesIO

from PIL import Image

from Base.SingletonPattern import Singleton
from Core.BasePage import BasePage


class RibbonPage(BasePage):
    __instance = None

    @staticmethod
    def inst():
        if RibbonPage.__instance is None:
            RibbonPage.__instance = RibbonPage()
        return RibbonPage.__instance

    "Page class that all page models can inherit from"

    login = 'Login'
    username = 'Username'
    password = 'Password'
    filing_log = 'Filing Log'

    def check_addin(self):
        print "STAAAAAAAAAAAAAAAAAARTIIING TEST"
        elem_to_be_found = self.get_name(self.login)
        if elem_to_be_found is not None:
            print elem_to_be_found
            self.driver.get_screenshot_as_file("1.png")
            elem_to_be_found.click()

    def nd_frame_login(self):
        username_field = self.get_name(self.username)
        password_field = self.get_name(self.password)
        login_button = self.get_name(self.login)
        username_field.send_keys("qa@zeroapp.ai")
        password_field.send_keys("InboxZero123")
        login_button.click()

    def check_filing_log(self):
        filing_log_button = self.get_name(self.filing_log)
        while True:
            if filing_log_button.get_attribute('IsEnabled'):
                filing_log_button.click()
