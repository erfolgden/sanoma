from selenium.common.exceptions import WebDriverException, NoSuchElementException, InvalidSelectorException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.command import Command
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from core.config import timeout_seconds
from selenium.webdriver.support import expected_conditions


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

    # Find element by locator. you can use locator's: class, xpath, id, name
    def find_element_by_locator(self, locator):
        locator_type = locator[:locator.find("=")], locator_value = locator[locator.find("=") + 1:]
        if locator_type == 'class':
            return self.driver.find_element_by_class(locator_value)
        elif locator_type == 'xpath':
            return self.driver.find_element_by_xpath(locator_value)
        elif locator_type == 'id':
            return self.driver.find_element_by_id(locator_value)
        elif locator_type == 'name':
            return self.driver.find_element_by_class_name(locator_value)
        else:
            raise Exception('Invalid locator')

        # Find element by locator. you can use locator's: class, xpath, id, name
    def find_elements_by_locator(self, locator):
        locator_type, locator_value = locator.split('=')
        if locator_type == 'class':
            elements = self.driver.find_elements_by_class(locator_value)
        elif locator_type == 'xpath':
            elements = self.driver.find_elements_by_xpath(locator_value)
        elif locator_type == 'id':
            elements = self.driver.find_elements_by_id(locator_value)
        elif locator_type == 'name':
            elements = self.driver.find_elements_by_class_name(locator_value)
        else:
            raise Exception('Invalid locator')

        return [WebElement(e, elements) for e in elements]

    # Is Element is present or not
    def is_element_present(self, locator):
        try:
            element = self.find_element_by_locator(locator)
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

