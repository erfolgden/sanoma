import pytest

"""
Base class to initialize the base test class and driver

"""

browsers = ['firefox', 'chrome']

class BaseTest(object):

    @pytest.fixture(scope="class", autouse=True, params=browsers)
    def manage_driver(self, request, driver):
        driver.start(request.param)
        request.addfinalizer(driver.stop)
