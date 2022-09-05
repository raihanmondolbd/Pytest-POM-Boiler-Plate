from Config.config import TestData
from Pages.BasePage import BasePage
from Locators.Locators import Locators


class HomePage(BasePage):
    def __init__(self, driver):
        self.locator = Locators
        # super(LoginPage, self).__init__(driver)
        super().__init__(driver)

    def get_text_from_employee_list(self):
        element = self.get_element(self.locator.employeeList)
        val = element.text
        print(val)
        return val

