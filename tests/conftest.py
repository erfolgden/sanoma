import pytest

from selenium import webdriver

browsers = {"ff": 'firefox', 'ch': 'chrome'}


class DriverManager(object):

    def __init__(self):
        self._instance = None

    def start(self, type='firefox'):
        # implement logic to create instance depends on condition
        if type == 'firefox':
            self._instance = webdriver.Firefox()
        else:
            # fixme: path to browser is hardcoded now. Need to instatiate browser somewhere in discussed place and get him from ENV
            self._instance = webdriver.Chrome("D:\\Install\\chromedriver_win32\\chromedriver.exe")
        self._instance.maximize_window()
        return self._instance

    @property
    def instance(self):
        if not self._instance:
            self.start()
        return self._instance

    def stop(self):
        self._instance.close()


def pytest_addoption(parser):
    parser.addoption("--browser", default='',
                     type='choice', choices=sorted(browsers),
                     help="runs tests only for given browser")


@pytest.yield_fixture(scope="module", params=browsers.keys())
def browser(request):
    selected = request.config.getoption('browser')
    if selected and selected != request.param:
        pytest.skip('browser {} selected in the command line'.format(selected))
    driver = browsers[request.param]
    yield driver


@pytest.fixture(scope="module")
def driver():
    return DriverManager()
