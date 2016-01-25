import pytest
from selenium import webdriver
import core.config

@pytest.fixture(scope='class')
def setup(request):
    core.config.driver = webdriver.Firefox()
    core.config.driver.implicitly_wait(10)
    core.config.driver.verificationErrors = []
    core.config.driver.accept_next_alert = True
    core.config.driver.maximize_window()

    def teardown():
        core.config.driver.quit()

    request.addfinalizer(teardown)

@pytest.mark.usefixtures("setup")
class BaseTest(object):
    pass
