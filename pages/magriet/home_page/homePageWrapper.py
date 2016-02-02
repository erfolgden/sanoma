from core.config import *
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from pages.page import Page
from pages.magriet.login_page import login_screen


class HomePageWrapper(Page):
    """
    http://www.libelle.nl homepage

    """

    SA_LOGIN_BUTTON = 'id=SA_login_button'
    PAGE_TITLE = 'Margriet | Alles over gezond en lekker leven'

    def get_site_logo(self):
        self.driver.get(MARGRIET_URL)
        return self._site_logo()

    def open_login_page(self):
        button = self.wait().until(ec.visibility_of_element_located((By.ID, "SA_login_button")),
                                   message="Unable to find login button")
        if button:
            button.click()

    def _site_logo(self):
        return self.driver.find_element_by_id("site-logo").get_attribute("text")
