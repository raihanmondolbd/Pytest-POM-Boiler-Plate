import time

import pytest
from TestCases.BaseTest import BaseTest
from Pages.LoginPage import LoginPage


class Test_Login(BaseTest):

    def test_login(self):
        login = LoginPage(self.driver)
        login.enter_user_name()
        time.sleep(3)
        login.enter_password()
        time.sleep(3)
        login.click_login_button()
        time.sleep(3)

# @pytest.mark.Login
# def test_login(init_driver):
#     login = LoginPage(init_driver)
#     login.enter_user_name()
#     time.sleep(3)
#     login.enter_password()
#     time.sleep(3)
#     login.click_login_button()
#     time.sleep(3)
