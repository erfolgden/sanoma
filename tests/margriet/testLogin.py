from core.locators.margriet_locators import HomePageLocators
from pages.margriet import gigya_login_screen
from pages.margriet.gigya_login_screen import GigyaLoginScreen
from tests.base_test import *
from pages.margriet.home_page import HomePage


class TestLoginFunctionality(BaseTest):

    def test_login_button_is_present(self):
        homepage = HomePage(core.config.driver)
        homepage.navigate()
        assert homepage.is_element_present(HomePageLocators.SA_login_button)

    def test_popup_window(self):
        homepage = HomePage(core.config.driver)
        ##gigya_login_screen = GigyaLoginScreen(core.config.driver)
        homepage.navigate()
        homepage.click_login_button()
        gigya_login_screen_page = GigyaLoginScreen(core.config.driver)
        assert gigya_login_screen_page.is_email_field_present()
        assert gigya_login_screen_page.is_password_field_present()
