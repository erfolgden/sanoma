from functionaltests.pages.Pages import Pages
from functionaltests.tests.BaseTest import BaseTest

"""
Test Step:
----------
Proceed with First Use Launching.
1. Launch http://www.margriet.nl/.
2. Check elements presence, clickability, text presence and order of representation on screen:
    1) Upper bar('HOME', 'GEZOND LEVEN', 'LEKKER ETEN', 'MODE & BEAUTY', 'INTERVIEWS', 'REISAANBIEDINGEN', 'VIDEO', 'MEER')
    2) DropDown list elements for all upper bar links
    3) Login button and dropdown list
    4) BottomBar

Test Environment:
----------
- Selenium
- Firefox
- Windows 10

Expected Result:
----------------
All element should be visible and rightly represented on screen.

[FAIL]
 -  elements are not visible
"""


class TestHomePage(BaseTest):

    BAR_LINK_ORDER = [u'HOME', u'GEZOND LEVEN', u'LEKKER ETEN', u'MODE & BEAUTY',
                      u'INTERVIEWS', u'REISAANBIEDINGEN', u'VIDEO', u'MEER']

    GEZOND_LEVEN_SUB_TAB = [u'FIT & GEZOND', u'BEWEGEN', u'AFVALLEN',
                            u'OVERGANG', u'PSYCHE', u'DAGHOROSCOOP', u'WONEN']
    LEKKER_SUB_TAB = [u'RECEPTEN', u'KOOKTIPS']
    MODE_BEAUTY_SUB_TAB = [u'MODE', u'FIGUURTIPS', u'BEAUTY']
    INTERVIEWS_SUB_TAB = [u'HARTEKREET', u'NOG NOOIT VERTELD', u'GESPREK VAN DE DAG', u'BN-ERS']
    REISAANBIEDINGEN_SUB_TAB = [u'STEDENTRIPS', u'ZONVAKANTIES', u'WINTERVAKANTIES', u'ACTIEVE VAKANTIES', u'EROPUIT']
    VIDEO_SUB_TAB = [u'LACH VAN DE DAG', u'DOE HET ZELF', u'HANDIG']
    MEER_SUB_TAB = [u'GRATIS & MET KORTING', u'WINNEN',
                    u'STUUR EEN KAARTJE', u'SPELLETJES', u'MUSICAL CLUB', u'ABONNEECADEAUS']
    LOGGIN_SUB_TAB = [u'INLOGGEN', u'REGISTREREN']
    BOTTOM_BAR = [u'ADVERTEREN', u'OVER ONS', u'CONTACT', u'DISCLAIMER', u'PRIVACY- EN COOKIEBELEID', u'COPYRIGHT']

    home_page = None
    def test_HomePage(self, driver):
        global home_page
        pages = Pages(driver)
        home_page = pages.navigateTo().select_home_page()
        open_page = home_page.open_margriet()
        assert open_page == 'http://www.margriet.nl/', 'Incorrect url-address'
        assert home_page.get_site_logo() == u'\n\t\t\t\t\tMargriet - Happy & Healthy\n\t\t\t\t', \
            'Incorrect site-logo text'
        assert home_page.get_bar_text() == TestHomePage.BAR_LINK_ORDER, \
            'Incorrect primary menu text or elements order'
        assert home_page.get_gezond_links_text() == TestHomePage.GEZOND_LEVEN_SUB_TAB, \
            'Incorrect GEZOND_LEVEN drop-down list text or elements order'
        assert home_page.get_leker_links_text() == TestHomePage.LEKKER_SUB_TAB, \
            'Incorrect LEKER drop-down list text or elements order'
        assert home_page.get_modeBeauty_links_text() == TestHomePage.MODE_BEAUTY_SUB_TAB, \
            'Incorrect Mode and Beauty drop-down list text or elements order'
        assert home_page.get_interviews_links_text() == TestHomePage.INTERVIEWS_SUB_TAB, \
            'Incorrect Interview drop-down list text or elements order'
        assert home_page.get_reisaanbiedingen_links_text() == TestHomePage.REISAANBIEDINGEN_SUB_TAB, \
            'Incorrect Reisaanbiedingen drop-down list text or elements order'
        assert home_page.get_video_links_text() == TestHomePage.VIDEO_SUB_TAB, \
            'Incorrect Video drop-down list text or elements order'
        assert home_page.get_meer_links_text() == TestHomePage.MEER_SUB_TAB, \
            'Incorrect Meer drop-down list text or elements order'
        assert home_page.get_login_links_text() == TestHomePage.LOGGIN_SUB_TAB, \
            'Incorrect Login drop-down list text or elements order'
        assert home_page.get_login_button() is not False, \
            "Login button is not clickable"
        assert home_page.get_bottom_bar() == TestHomePage.BOTTOM_BAR, \
            'Incorrect bottom bar elements text or order'

    def test_Registration(self):
        home_page.login_screen()
        home_page.registration_screen()
        home_page.click_agreement()

