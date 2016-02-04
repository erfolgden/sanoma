from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage
from pages.libelle.home_page.homePageLibelleWrapper import LibelleHomePageWrapper


class LibelleLoginPageWrapper(BasePage):
    """
    http://www.libelle.nl/ homepage

    """

    LOGIN_HEADER = 'login-social header'
    EMAIL_FIELD = "(//form[@class='gigya-login-form']//input[@name='username'])[2]"
    PASSWORD_FIELD = "(//form[@class='gigya-login-form']//input[@name='password'])[2]"

    def open_login_page(self):
        button = self.wait.until(ec.visibility_of_element_located(
            (By.ID, LibelleHomePageWrapper.SA_LOGIN_BUTTON)),
            message="Unable to find login button")
        if button:
            button.click()

    def click_login_button(self):
        self.wait.until(ec.visibility_of_element_located(
            (By.CLASS_NAME, LibelleLoginPageWrapper.NAVIGATION_WINDOW)),
            message="Unable to find login button").click()
        element = self.wait.until(ec.visibility_of_element_located(
            (By.CLASS_NAME, LibelleLoginPageWrapper.LOGIN_HEADER)),
            message="Unable to find login button")

    def get_email_field_placeholder(self):
        self.wait.until(ec.visibility_of_element_located(
            (By.XPATH, LibelleLoginPageWrapper.EMAIL_FIELD)),
            message="Unable to find E-mail field")
        return self.driver.find_element_by_xpath(LibelleLoginPageWrapper.EMAIL_FIELD).get_attribute("placeholder")

    def get_password_field_placeholder(self):
        password_field = self.wait.until(ec.visibility_of_element_located(
            (By.XPATH, LibelleLoginPageWrapper.PASSWORD_FIELD)),
            message="Unable to find Password field")
        return self.driver.find_element_by_xpath(LibelleLoginPageWrapper.PASSWORD_FIELD).get_attribute("placeholder")
