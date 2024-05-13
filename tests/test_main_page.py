from pages.MainPage import MainPage
from conftest import chrome


class TestMainPage:
    def test_currency_tab(self, chrome):
        page = MainPage(chrome)
        page.open()
        page.click_currency_tab()
        value = page.tab_current
        assert value is not None
