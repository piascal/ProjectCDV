import selenium
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.airbnb.pl/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    def tearDown(self):
        self.driver.quit()