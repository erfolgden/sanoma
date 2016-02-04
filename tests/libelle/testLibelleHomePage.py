from core.config import LIBELLE_URL
from pages.Pages import Pages
from tests.BaseTest import BaseTest


class TestLoginFunctionality(BaseTest):


    def testHomePage(self, driver):
        """
        Check url and title of the HomePage
        :param driver:
        :return:
        """
        pages = Pages(driver)
        homePage = pages.navigateTo().select_libelle_home_page()
        open_home_page = homePage.open_libelle()
        assert open_home_page == LIBELLE_URL, 'Incorrect url-address'
        assert homePage.check_libelle_title() == homePage.PAGE_TITLE, 'Incorrect url-address'