from pages.BasePage import BasePage
from pages.libelle.home_page.homePageLibelleWrapper import LibelleHomePageWrapper
from pages.magriet.home_page.homePageWrapper import HomePageWrapper


class Pages(BasePage):
    def __init__(self, driver):
        super(Pages, self).__init__(driver)
        self.driver = driver

    def navigateTo(self):
        return PageWrappers(self.driver)


class PageWrappers(Pages):
    def __init__(self, driver):
        super(PageWrappers, self).__init__(driver)

    def select_home_page(self):
        return HomePageWrapper(self.driver)

    def select_login_page(self):
        pass

    def select_libelle_home_page(self):
        return LibelleHomePageWrapper(self.driver)