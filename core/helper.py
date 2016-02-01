from core import config

# Helpers for the automation tests


def open_page(url):
    config.driver.get(url)
