from core import locators
from core.config import base_url
from pages.page import Page


class ContactPage(Page):
    """Contact page action methods come here"""

    _url = base_url + "pagina/artikel/contact/"

    def is_title_matches(self):
        """Verifies that the "Sanoma" appears in page title"""
        return locators.ContactPageLocators.Title in self.driver.title
