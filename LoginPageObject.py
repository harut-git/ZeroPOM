from selenium.webdriver.common.by import By

from Locators import Locator


class Login(object):

    def __init__(self, driver):
        self.driver = driver

        # home page locators defining
        self.logo = driver.find_element(By.NAME, Locator.logo)
        # self.sign_on = driver.find_element(By.NAME, Locator.login_button)

    def getLogo(self):
        return self.logo

    # def getSignOn(self):
    #     return self.sign_on