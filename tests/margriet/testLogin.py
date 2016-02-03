from tests.BaseTest import BaseTest
from pages.magriet.home_page.homePageWrapper import HomePageWrapper


class TestLoginFunctionality(BaseTest):
    def test_login(self, driver):
        modal = HomePageWrapper(driver=driver)
        modal.get_site_logo() == 'Margriet - Happy & Healthy', "Incorrect site-logo name"
        modal.open_login_page()
        modal.find_element_by_locator_test()
