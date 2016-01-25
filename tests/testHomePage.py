import unittest

from base_test import *
from pages.home_page import Homepage


class TestHomePage(BaseTest):

    def test_home(self):
        homepage = Homepage(core.config.driver)
        homepage.navigate()
        assert homepage.is_title_matches()