from core import locators
from pages.page import Page
from pages.sanoma.contact_page import ContactPage


class Homepage(Page):
    """Home page action methods come here"""

    _url = "http://sanoma.nl"

    @property
    def cookie_bar_container(self):
        return self.driver.find_element_by_id("cookiebar-top")

    @property
    def cookie_bar_akkord_button(self):
        return self.driver.find_elements_by_class_name("accept-button font-medium")

    def click_content_menu_item(self):
        self.driver.find_element_by_id("nav-main-contact").click()
        contact_page = ContactPage(self.driver)
        return contact_page

    def is_title_matches(self):
        """Verifies that the hardcoded text "Sanoma - Home" appears in page title"""
        return locators.HomePageLocators.Title in self.driver.title
