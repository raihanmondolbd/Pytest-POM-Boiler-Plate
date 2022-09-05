from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""This class is the parent of all pages"""
"""It contains all the generic methods and utilities for all the pages"""


class BasePage:
    def __init__(self, driver, base_url=''):
        self.base_url = base_url
        self.driver = driver

    def get_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        # element = self.driver.find_element(*locator)
        return element

    def click_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def enter_at(self, locator, data):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(data)

    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

    def is_enabled_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.is_enabled()

    def is_selected_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.is_selected()

    # def get_title(self, locator):
    #     WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
    #     return self.driver.title
