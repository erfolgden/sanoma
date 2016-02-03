from core.config import *
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class HomePageWrapper(BasePage):
    """
    http://www.margriet.nl/ homepage

    """

    SA_LOGIN_BUTTON = 'id=SA_login_button'
    PAGE_TITLE = 'Margriet | Alles over gezond en lekker leven'
    BAR_MENU_XPATH = 'menu-primary-menu'
    HOME = 'menu-item-37198'

    def open_margriet(self):
        self.driver.get(MARGRIET_URL)
        return self.driver.current_url

    def get_site_logo(self):
        return self.driver.find_element_by_id("site-logo").get_attribute("text")

    def get_bar_links(self):
        return filter(bool, [i.text for i in self.driver.find_elements_by_xpath(HomePageWrapper.BAR_MENU_XPATH)])

    def get_home_links(self):
        return [i.text for i in self.driver.find_elements_by_xpath("//ul[@id='menu-primary-menu']/li")]
