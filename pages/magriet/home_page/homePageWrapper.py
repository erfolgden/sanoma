from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from pages.BasePage import BasePage
from core.config import *


class HomePageWrapper(BasePage):
    """
    http://www.margriet.nl/ homepage

    """

    SA_LOGIN_BUTTON = 'id=SA_login_button'
    PAGE_TITLE = 'Margriet | Alles over gezond en lekker leven'
    BAR_MENU_XPATH = "//ul[@id='menu-primary-menu']/li"
    GEZOND_LEVEN = 'menu-item-37198'

    FITGEZOND = 'menu-item-417594'
    BEWEGEN = 'menu-item-342552'
    AFWALLEN = 'menu-item-81566'
    OVERGANG = 'menu-item-406463'
    PSYCHE = 'menu-item-417122'
    DASHGOROSCCOP = 'menu-item-372578'
    WOVEN = 'menu-item-424915'

    ORDER_TAB_LIST = (FITGEZOND, BEWEGEN, AFWALLEN, OVERGANG, PSYCHE, DASHGOROSCCOP, WOVEN)

    def open_margriet(self):
        self.driver.get(MARGRIET_URL)
        return self.driver.current_url

    def get_site_logo(self):
        return self.driver.find_element_by_id("site-logo").get_attribute("text")

    def get_bar_links(self):
        return filter(bool, [i.text for i in self.driver.find_elements_by_xpath(HomePageWrapper.BAR_MENU_XPATH)])

    def get_gezond_links(self):
        find_element = self.wait.until(ec.visibility_of_element_located((By.ID, HomePageWrapper.GEZOND_LEVEN)))
        ActionChains(self.driver).move_to_element(find_element).perform()
        list_of_tab = [self.wait.until(ec.visibility_of_element_located((By.ID, i))).text
                       for i in HomePageWrapper.ORDER_TAB_LIST]
        return list_of_tab


