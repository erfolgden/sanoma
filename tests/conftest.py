import pytest

from selenium import webdriver


class DriverManager(object):

    def __init__(self):
        self._instance = None

    def start(self, type='firefox'):
        # implement logic to create instance depends on condition
        if type == 'firefox':
            self._instance = webdriver.Firefox()
        else:
            pass
            # self._instance = webdriver.Chrome("path//to//webdriver")
        self._instance.maximize_window()
        return self._instance

    @property
    def instance(self):
        if not self._instance:
            self.start()
        return self._instance

    def stop(self):
        self._instance.close()


@pytest.fixture(scope="module")
def driver():
    return DriverManager()
