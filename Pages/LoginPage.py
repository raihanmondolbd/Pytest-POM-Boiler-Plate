from Pages.BasePage import BasePage
from Locators.Locators import Locators
from Config.config import TestData


class LoginPage(BasePage):
    def __init__(self, driver):
        self.locator = Locators
        # super(LoginPage, self).__init__(driver)
        super().__init__(driver)

    def enter_user_name(self):
        self.enter_at(self.locator.userNameTextBox, TestData.USER_NAME)

    def enter_password(self):
        self.enter_at(self.locator.passwordTextBox, TestData.PASSWORD)

    def click_login_button(self):
        self.click_element(self.locator.loginButton)
