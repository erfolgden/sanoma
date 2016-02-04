from selenium.webdriver.support import wait

from core.config import LIBELLE_URL
from pages.BasePage import BasePage


class LibelleHomePageWrapper(BasePage):
    """
    http://www.libelle.nl/ homepage

    """

    SA_LOGIN_BUTTON = 'id=SA_login_button'
    PAGE_TITLE = "Libelle Daily - Dagelijks het laatste nieuws dat informeert, inspireert en vermaakt"

    def open_libelle(self):
        self.driver.get(LIBELLE_URL)
        return self.driver.current_url

    def check_libelle_title(self):
        return self.get_page_title()
