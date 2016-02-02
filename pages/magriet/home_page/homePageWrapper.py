from pages.page import Page


class HomePageWrapper(Page):
    """
    http://www.libelle.nl homepage

    """

    SA_LOGIN_BUTTON = 'id=SA_login_button'
    PAGE_TITLE = 'Margriet | Alles over gezond en lekker leven'

    def __init__(self, *args, **kwargs):
        super(HomePageWrapper, self).__init__(*args, **kwargs)
