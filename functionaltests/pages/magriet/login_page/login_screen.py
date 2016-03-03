from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

locators = {
    'email_input_field':
        'xpath=//*[@id="gigya-login-screen"]//input[@class="gigya-input-text gigya-error-display"]',
    'password_input_field':
        'xpath=//*[@id="gigya-login-screen"]//input[@class="gigya-input-password gigya-error-display"]'}


class LoginScreen(BasePage):
    _url = ""

    SA_LOGIN_BUTTON = 'id=SA_login_button'

    def open_login_page(self):
        button = self.wait.until(ec.visibility_of_element_located(
            (By.ID, LoginScreen.SA_LOGIN_BUTTON)),
            message="Unable to find login button")
        if button:
            button.click()

    def is_email_field_present(self):
        # element = self.is_element_present(locators['email_input_field'])
        element = self.driver
        return element

    def is_password_field_present(self):
        return self.is_element_present(locators['password_input_field'])
