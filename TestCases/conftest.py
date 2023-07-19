import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Config.config import TestData


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture()
def getBrowser(request):
    _browser = request.config.getoption("--browser")
    return _browser


@pytest.fixture()
def init_driver(request, getBrowser):
    _driver = None
    print(f'The getting browser is - {getBrowser}')
    if getBrowser == "chrome":
        service = Service(ChromeDriverManager().install())
        _driver = webdriver.Chrome(service=service)
    elif getBrowser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        _driver = webdriver.Firefox(service=service)
    _driver.maximize_window()
    _driver.get(DATA.BASE_URL)
    time.sleep(5)
    request.cls.driver = _driver

    yield request.cls.driver
    request.cls.driver.quit()




# @pytest.fixture(params=['chrome'], scope='class')
# def init_driver(request):
#     global web_driver
#     if request.param == 'chrome':
#         web_driver = webdriver.Chrome(ChromeDriverManager().install())
#     if request.param == "firefox":
#         web_driver = webdriver.Chrome(executable_path=GeckoDriverManager().install())
#     request.cls.driver = web_driver
#     web_driver.implicitly_wait(10)
#     web_driver.maximize_window()
#     web_driver.get(TestData.BASE_URL)

#     yield
#     web_driver.quit()

# @pytest.fixture(scope='module')
# def init_driver():
#     global web_driver
#     web_driver = webdriver.Chrome(ChromeDriverManager().install())
#     web_driver.implicitly_wait(10)
#     web_driver.maximize_window()
#     web_driver.get(TestData.BASE_URL)
#
#     yield
#     web_driver.quit()



