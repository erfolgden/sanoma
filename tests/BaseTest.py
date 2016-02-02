import pytest

from selenium import webdriver
import selenium.common
from selenium.webdriver.support.ui import WebDriverWait
from core.config import UI_MAX_RESPONSE_TIME

"""Base class to initialize the base test class and driver"""

driver = None

@pytest.fixture(scope='class')
def setUp(request):
    global driver
    print("setUP class")
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.verificationErrors = []
    driver.accept_next_alert = True
    driver.maximize_window()
    request.addfinalizer(lambda: driver.quit())

@pytest.mark.usefixtures("setup")
class BaseTest(object):
    def __init__(self):
        print("BaseTest class")
        self.wait = WebDriverWait(
            self.driver,
            UI_MAX_RESPONSE_TIME,
            ignored_exceptions=selenium.common.exceptions.WebDriverException
        )
