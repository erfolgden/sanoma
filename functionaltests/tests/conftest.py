import pytest
from selenium import webdriver

from functionaltests.core.config import USERNAME, BROWSERSTACK_KEY

desired_cap = {'browser': 'Firefox',
               'browser_version': '43.0',
               'os': 'Windows',
               'os_version': '8.1',
               'resolution': '1920x1200',
               'browserstack.debug': 'true',
               'project': 'Sanoma Account Functional Tests'}

url = 'http://den378:7Lh6qWZ5xQrYg8iveqmo@hub.browserstack.com:80/wd/hub'

browsers = {'bs': 'browserstack', "ff":"firefox"}


class DriverManager(object):

    def __init__(self):
        self._instance = None

    def start(self, browser_type='browserstack'):

        """
        Webdriver instantiation method

        :param browser_type: of selected browser via commandline,
            in case of None pass browser will be runned all browsers from browsers dictionary
        :return: webdriver instance

        """

        if browser_type == 'firefox':
            self._instance = webdriver.Firefox()
        if browser_type == 'browserstack':
            if not (USERNAME and BROWSERSTACK_KEY):
                raise Exception("Please provide your BrowserStack username and access key")
            else:
                self._instance = \
                    webdriver.Remote(
                        command_executor='http://den378:7Lh6qWZ5xQrYg8iveqmo@hub.browserstack.com:80/wd/hub',
                        desired_capabilities=desired_cap)
        return self._instance

    @property
    def instance(self):
        if not self._instance:
            self.start()
        return self._instance

    def stop(self):
        self._instance.close()
        self._instance.quit()


def pytest_addoption(parser):

    """

    Register commandline options
      :param parser - commandline arg(e.g 'py.test --browser')

    """
    parser.addoption("--browser", default='',
                     type='choice', choices=sorted(browsers),
                     help="runs tests only for given browser")
    parser.addoption("--url", default='',
                     help="runs tests with specific url address")


@pytest.yield_fixture(scope="module", params=browsers.keys())
def browser(request):

    """

    :scope module - the scope for which this fixture is shared,
        one of 'function' (default). Has been selected module because of 'DriverManager' class instantiate
        and commandline args option pass via 'start' method
    :param request: an optional list of parameters
    :return: str of selected option(e.g py.test --browser=ff, will return 'firefox'),
        after this option pass in 'start()' method of 'DriverManager' class via BaseTest

    """
    selected = request.config.getoption('browser')
    if selected and selected != request.param:
        pytest.skip('browser {} selected in the command line'.format(selected))
    driver = browsers[request.param]
    yield driver


@pytest.yield_fixture(scope="module")
def url(request):
    """
    url as param can pass via tests

    """

    yield request.config.getoption("url")


@pytest.fixture(scope="module")
def driver():

    """
    DriverManager instantiation function

    :return: Instance of DriverManager

    PS: driver is visible across module
    """
    return DriverManager()
