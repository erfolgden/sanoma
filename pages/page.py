class Page(object):
    """Base class to initialize the base page that will be called from all pages"""

    _url = None

    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get(self._url)