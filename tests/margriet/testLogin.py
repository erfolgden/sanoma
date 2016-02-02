from pages.magriet.home_page import homePageWrapper
from tests.BaseTest import BaseTest, driver


class TestLoginFunctionality(BaseTest):
    def test_login_button_is_present(self):
        homepage = homePageWrapper(driver)
