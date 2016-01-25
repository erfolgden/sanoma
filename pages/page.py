from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.expected_conditions import visibility_of_element_located


class Page(object):
    """Base class to initialize the base page that will be called from all pages"""

    _url = None

    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get(self._url)

    def is_element_visible(self, locator):
        """Verifies that the element is visible
        :param locator:
        """
        try:
            self.driver.wait.until(visibility_of_element_located(locator))
            return True
        except WebDriverException:
            return False
