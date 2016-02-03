from tests.BaseTest import BaseTest
from pages.Pages import Pages

class TestLoginFunctionality(BaseTest):

    BAR_LINK_ORDER = [u'HOME', u'GEZOND LEVEN', u'LEKKER ETEN', u'MODE & BEAUTY',
                      u'INTERVIEWS', u'REISAANBIEDINGEN', u'VIDEO', u'MEER']

    def test_HomePage(self, driver):
        pages = Pages(driver)
        home_page = pages.navigateTo().select_home_page()
        open_page = home_page.open_margriet()
        assert open_page == 'http://www.margriet.nl/', 'Incorrect url-address'
        assert home_page.get_site_logo() == u'\n\t\t\t\t\tMargriet - Happy & Healthy\n\t\t\t\t', 'Incorrect site-logo'
        assert home_page.get_bar_links() == TestLoginFunctionality.BAR_LINK_ORDER, 'Incorrect order of bar links'


