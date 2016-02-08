import pytest

"""
Base class to initialize the base test class and driver

"""


class BaseTest(object):
    @pytest.fixture(scope="class", autouse=True)
    def manage_driver(self, request, driver, browser):
        driver.start(browser)
        request.addfinalizer(driver.stop)
