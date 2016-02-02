
from tests.BaseTest import *
from pages.sanoma.home_page import Homepage


class TestContentPage(BaseTest):

    # Scenario: When I open Home page in Firefox browser and click on menu item "contact"
    # Contact page is opened and title = "Sanoma"
    # When I open home_page and click content menu item "nav-main-contact"
    # then contact page will opened and title = "Sanoma"
    def test_contact_page(self):
        homepage = Homepage(core.config.driver)
        homepage.navigate()
        contact_page = homepage.click_content_menu_item()
        contact_page.is_title_matches()
