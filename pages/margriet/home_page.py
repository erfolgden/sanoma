from core.locators.margriet_locators import HomePageLocators
from pages.margriet.gigya_login_screen import GigyaLoginScreen
from pages.page import Page


class HomePage(Page):
    """http://www.libelle.nl homepage"""
    _url = "http://www.margriet.nl/"

    def click_login_button(self):
        element = self.find_element_by_locator(HomePageLocators.SA_login_button)
        element.click()
