from core import locators
from pages.page import Page


class Homepage(Page):
    _url = "http://sanoma.nl"

    def is_title_matches(self):
        """Verifies that the text "title" appears in page title"""
        print self.driver.title

        if self.driver.title == locators.HomePageLocators.Title:
            return True
        else:
            return False