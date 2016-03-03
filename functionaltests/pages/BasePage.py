import selenium.common
from core.config import UI_MAX_RESPONSE_TIME
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait


# fixme: should be re-factored


class BasePage(object):

    """

    Base class to initialize the base page that will be called from all pages

    """

    URL = None

    def __init__(self, driver):
        self.driver = driver.instance
        self.wait = WebDriverWait(
            self.driver,
            UI_MAX_RESPONSE_TIME,
            ignored_exceptions=selenium.common.exceptions.WebDriverException
            )

    def is_element_present(self, locator):
        """Verifies that the element is present
        :param locator:
        """
        return WebDriverWait(self.driver, 5).until(
            lambda driver: True if self.find_element_by_locator(locator) else False)

    def find_element_by_locator(self, locator):
        """Find element by locator. You can use locator's: class, xpath, id, name
        :param locator:
        """
        locator_type, locator_value = locator.split('=')
        d = {'id': self.driver.find_element_by_id(locator_value),
             'xpath': self.driver.find_element_by_xpath(locator_value),
             'class': self.driver.find_element_by_class_name(locator_value),
             'name': self.driver.find_element_by_name(locator_value),
             'css': self.driver.find_elements_by_css(locator_value)
             }
        return self.wait.until(lambda driver: d.get(locator_type))

    def is_visible(self, locator):
        """Find element by locator. You can use locator's: class, xpath, id, name
        :param locator:
        """
        return lambda driver: True if self.find_element_by_locator(locator).is_displayed() else False

    # Check is element available or not
    def is_element_available(self, locator):
        if self.is_element_present(locator):
            if self.is_visible(locator):
                return True
        else:
            return False

    def click(self, locator):
        try:
            self.find_element_by_locator(locator).click()
        except NoSuchElementException:
            return False

    def get_page_title(self):
        return self.driver.title
