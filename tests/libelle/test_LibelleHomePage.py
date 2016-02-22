from core.config import LIBELLE_URL
from pages.Pages import Pages
from tests.BaseTest import BaseTest

"""
Test Scenario:
----------
1. Open url="http://www.margriet.nl/"
2. Check site url's and title's
3. Open login page and check that e-mail and password fields present on the page

Test Environment:
----------
- Selenium 2.50.1
- Firefox 42.0

Expected Result:
----------------
All element should be present on the page

[FAIL]
 -  elements are not visible
"""
class TestLoginFunctionality(BaseTest):

#    def test_HomePage(self, driver):
#        """
#        Check Home page url's and title's
#        :param driver:instance of selenium driver
#        :return:
#        """
#        pages = Pages(driver)
#        homePage = pages.navigateTo().select_libelle_home_page()
#        open_home_page = homePage.open_libelle()
#        assert open_home_page == LIBELLE_URL, 'Incorrect url-address'
#        assert homePage.check_libelle_title() == homePage.PAGE_TITLE, 'Incorrect url-address'

    def test_LoginPage(self, driver):
        """
        Check LoginPage structure
        :param driver:
        :return:
        """
        pages = Pages(driver)
        homePage = pages.navigateTo().select_libelle_home_page()
        loginPage = pages.navigateTo().select_libelle_login_page()
        homePage.open_libelle()
        loginPage.open_login_page()
        assert loginPage.get_email_field_placeholder() == "E-mailadres*", 'E-mail field is not present'
        assert loginPage.get_password_field_placeholder() == "Wachtwoord*", 'Password field is not present'
