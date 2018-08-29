from io import BytesIO

from PIL import Image

from Base.SingletonPattern import Singleton
from Core.BasePage import BasePage


class RibbonPage(BasePage):
    __metaclass__ = Singleton
    addin_name = 'Login'

    def check_addin(self):
        elem_to_be_found = self.get_name(self.addin_name)
        if elem_to_be_found is not None:
            print elem_to_be_found
            self.driver.get_screenshot_as_file("1.png")
