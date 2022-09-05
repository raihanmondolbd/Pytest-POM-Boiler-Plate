import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from Config.config import TestData


@pytest.fixture(params=['chrome'], scope='class')
def init_driver(request):
    global web_driver
    if request.param == 'chrome':
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == "firefox":
        web_driver = webdriver.Chrome(executable_path=GeckoDriverManager().install())
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    web_driver.maximize_window()
    web_driver.get(TestData.BASE_URL)

    yield
    web_driver.quit()

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



