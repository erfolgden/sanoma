import pytest

from selenium import webdriver


class DriverManager(object):

    def __init__(self):
        self._instance = None

    def start(self, type='ff'):
        # implement logic to create instance depends on condition
        self._instance = webdriver.Firefox()
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
