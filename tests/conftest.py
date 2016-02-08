import pytest

from selenium import webdriver

browsers = {"ff": 'firefox', 'ch': 'chrome'}


class DriverManager(object):

    def __init__(self):
        self._instance = None

    def start(self, type='firefox'):

        """
        Webdriver instantiation method

        :param type: of selected browser via commandline,
            in case of None pass browser will be runned all browsers from browsers dictionary
        :return: webdriver instance

        """

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

    """

    Register commandline options
      :param parser - commandline arg(e.g 'py.test --browser')

    """
    parser.addoption("--browser", default='',
                     type='choice', choices=sorted(browsers),
                     help="runs tests only for given browser")


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


@pytest.fixture(scope="module")
def driver():

    """
    DriverManager instantiation function

    :return: Instance of DriverManager

    PS: driver is visible across module
    """
    return DriverManager()
