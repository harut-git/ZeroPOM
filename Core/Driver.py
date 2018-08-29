from selenium import webdriver


class Driver(object):
    def __init__(self):
        self.driver = None

    def start_driver(self):
        self.driver = webdriver.Remote(
            command_executor='http://localhost:9999',
            desired_capabilities={
                "app": r"C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.exe",
            })

    def stop_driver(self):
        self.driver.close()
