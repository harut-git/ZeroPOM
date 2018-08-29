import unittest
import datetime
from selenium import webdriver
import os


class EnvironmentSetup(object):
    def __init__(self):
        self.driver = webdriver.Remote(
            command_executor='http://localhost:9999',
            desired_capabilities={
                "app": r"C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.exe",
            })
        print ("Run Started at :" + str(datetime.datetime.now()))
        print("Outlook Environment Set Up")
        print("------------------------------------------------------------------")