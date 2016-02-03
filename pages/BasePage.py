from selenium.common.exceptions import WebDriverException, NoSuchElementException, InvalidSelectorException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.command import Command
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support import expected_conditions
import selenium.common
from selenium.webdriver.support.ui import WebDriverWait
from core.config import UI_MAX_RESPONSE_TIME


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

    def is_element_visible(self, locator):
        """Verifies that the element is visible
        :param locator:
        """
        return WebDriverWait(self.driver, 5).until(lambda driver: True if self.is_element_present(locator) else False)


    # Find element by locator. you can use locator's: class, xpath, id, name
    def find_element_by_locator(self, locator):
        locator_type, locator_value = locator.split('=')
        d = {'id': 'self.driver.find_element_by_id(locator_value)',
             'xpath': 'self.driver.find_element_by_xpath(locator_value)',
             'class': 'self.driver.find_element_by_class_name(locator_value)',
             'name': 'self.driver.find_element_by_name(locator_value)',
             'css': 'self.driver.find_elements_by_css(locator_value)'
             }
        try:
            self.wait().until(lambda driver: d.get(locator_type))
            element_value = d.get(locator_type)
        except NoSuchElementException:
            raise Exception('Invalid locator')
        return element_value


    # Is Element is present or not
    def is_element_present(self, locator):
        try:
            element = self.find_element_by_locator(locator)
            if element:
                return True
        except NoSuchElementException:
            return False

    # Element is visible or not
    def is_visible(self, locator):
        return self.find_element_by_locator(locator).is_displayed()

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
