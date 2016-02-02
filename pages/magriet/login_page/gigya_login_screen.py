from pages.page import Page
from selenium import webdriver

locators = {
    'email_input_field':
        'xpath=//*[@id="gigya-login-screen"]//input[@class="gigya-input-text gigya-error-display"]',
    'password_input_field':
        'xpath=//*[@id="gigya-login-screen"]//input[@class="gigya-input-password gigya-error-display"]'}


class GigyaLoginScreen(Page):
    _url = ""

    def is_email_field_present(self):
        # element = self.is_element_present(locators['email_input_field'])
        element = self.driver
        return element


    def is_password_field_present(self):
        return self.is_element_present(locators['password_input_field'])
