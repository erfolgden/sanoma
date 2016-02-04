from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from pages.BasePage import BasePage
from core.config import *
import cfg


class HomePageWrapper(BasePage):
    """
    http://www.margriet.nl/ homepage

    """

    ORDER_SUB_GEZOND = (cfg.FITGEZOND, cfg.BEWEGEN, cfg.AFWALLEN, cfg.OVERGANG,
                        cfg.PSYCHE, cfg.DASHGOROSCCOP, cfg.WOVEN)
    ORDER_SUB_LEKER = (cfg.RECEPTEN, cfg.KOOKTIPS)
    ORDER_SUB_MODE_BEAUTY = (cfg.MODE, cfg.FIGUURTIPS, cfg.BEAUTY)
    ORDER_SUB_INTERVIEWS = (cfg.HARTEKREET, cfg.NOG_NOOIT_VERTELD, cfg.GESPREK_VAN_DE_DAG, cfg.BN_ERS)
    ORDER_SUB_REISAANBIEDINGEN = (cfg.STEDENTRIPS, cfg.ZONVAKANTIES, cfg.WINTERVAKANTIES,
                                  cfg.ACTIEVE_VAKANTIES, cfg.EROPUIT)
    ORDER_SUB_VIDEO = (cfg.LACH_VAN_DE_DAG, cfg.DOE_HET_ZELF, cfg.HANDIG)
    ORDER_SUB_MEER = (cfg.GRATIS_MET_KORTING, cfg.WINNEN, cfg.STUUR_EEN_KAARTJE,
                      cfg.STUUR_EEN_KAARTJE, cfg.SPELLETJES, cfg.MUSICAL_CLUB, cfg.ABONNEECADEAUS)
    ORDER_BOTTOM_BAR = (cfg.ADVERTEREN, cfg.OVER_ON, cfg.CONTACT, cfg.DISCLAIMER,
                       cfg.PRIVACY_EN_COOKIEBELEID, cfg.COPYRIGHT)

    def open_margriet(self):
        self.driver.get(MARGRIET_URL)
        return self.driver.current_url

    def get_site_logo(self):
        return self.driver.find_element_by_id("site-logo").get_attribute("text")

    def get_bar_text(self):
        return filter(bool, [i.text for i in self.driver.find_elements_by_xpath(cfg.BAR_MENU_XPATH)])

    def get_gezond_links_text(self):
        return self._get_links(cfg.GEZOND_LEVEN, HomePageWrapper.ORDER_SUB_GEZOND)

    def get_leker_links_text(self):
        return self._get_links(cfg.LEKKER_ETEN, HomePageWrapper.ORDER_SUB_LEKER)

    def get_modeBeauty_links_text(self):
        return self._get_links(cfg.MODE_AND_BEAUTY, HomePageWrapper.ORDER_SUB_MODE_BEAUTY)

    def get_interviews_links_text(self):
        return self._get_links(cfg.INTERVIEWS, HomePageWrapper.ORDER_SUB_INTERVIEWS)

    def get_reisaanbiedingen_links_text(self):
        return self._get_links(cfg.REISAANBIEDINGEN, HomePageWrapper.ORDER_SUB_REISAANBIEDINGEN)

    def get_video_links_text(self):
        return self._get_links(cfg.VIDEO, HomePageWrapper.ORDER_SUB_VIDEO)

    def get_meer_links_text(self):
        html = self.wait.until(ec.visibility_of_element_located((By.ID, cfg.MEER)))
        ActionChains(self.driver).move_to_element(html).perform()
        items = html.find_elements_by_tag_name("li")
        return filter(bool, [i.text for i in items])

    def get_login_links_text(self):
        html = self.wait.until(
            ec.visibility_of_element_located((By.XPATH, cfg.LOGIN_LIST_XPATH)))
        ActionChains(self.driver).move_to_element(html).perform()
        return [[k.text for k in i.find_elements_by_tag_name("li")]
                for i in html.find_elements_by_tag_name("div")][0]

    def get_login_button(self):
        return self.wait.until(ec.element_to_be_clickable((By.ID, cfg.SA_LOGIN_BUTTON)),
                               message="Unable to locate login button on screen")

    def get_bottom_bar(self):
        return [self.driver.find_element_by_id(element).text for element in HomePageWrapper.ORDER_BOTTOM_BAR
                if self.wait.until(ec.element_to_be_clickable((By.ID, element)),
                                   message="Unable to locate links on screen")]

    def _get_links(self, bar_menu_element, dropdown_list):
        element = self.wait.until(
            ec.visibility_of_element_located((By.ID, bar_menu_element)), message="Unable to locate WebElement")
        ActionChains(self.driver).move_to_element(element).perform()
        return [self.wait.until(
            ec.visibility_of_element_located((By.ID, i)), "Unable to locate WebElement").text
            for i in dropdown_list]


