from EnvironmentSetup import EnvironmentSetup
from LoginPageObject import Login
from Page import Page


def login():
    driver = EnvironmentSetup().driver
    login = Page(driver)
    login.click_element(Login(driver).getLogo())


login()