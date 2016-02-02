import pytest

"""
Base class to initialize the base test class and driver

"""


class BaseTest(object):

    @pytest.fixture(scope="class", autouse=True)
    def manage_driver(self, request, driver):
        driver.start()
        request.addfinalizer(driver.stop)
