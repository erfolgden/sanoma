from tests.base_test import *
from pages.sanoma.home_page import Homepage


class TestHomePage(BaseTest):

    # Scenario: When I open Home page in Firefox browser
    # cookie bar should be present and page has title = "Sanoma - Home"
    # When I open home_page then cookie_bar_container is not None and title = "Sanoma - Home"
    def test_home_title(self):
        homepage = Homepage(core.config.driver)
        homepage.navigate()
        assert homepage.is_title_matches()
        assert homepage.cookie_bar_container is not None
