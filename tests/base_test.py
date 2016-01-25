import pytest
from selenium import webdriver
import core.config


@pytest.fixture(scope='class')
def setup(request):
    core.config.driver = webdriver.Firefox()

    def teardown():
        core.config.driver.quit()

    request.addfinalizer(teardown)


@pytest.mark.usefixtures("setup")
class BaseTest(object):
    pass
