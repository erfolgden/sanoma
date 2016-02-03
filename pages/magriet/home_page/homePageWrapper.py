from core.config import *
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from pages.page import Page
from pages.magriet.login_page import login_screen

SA_LOGIN_BUTTON = 'id=SA_login_button'
CONTAINER_SOCIAL = 'SA_screenset_container_social_0'
CONTAINER_SOCIAL_ID = 'id=SA_screenset_container_social_0'
PAGE_TITLE = 'Margriet | Alles over gezond en lekker leven'
CSS_ELEMENTS_TEST = 'css=.img-container>img'

class HomePageWrapper(Page):
    """
    http://www.libelle.nl homepage

    """


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

    def find_element_by_locator_test(self):
        self.find_element_by_locator(CONTAINER_SOCIAL_ID)