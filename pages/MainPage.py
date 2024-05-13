from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MainPage:
    def __init__(self, driver: WebDriver):
        self.url = 'https://www.ukr.net/'
        self.driver = driver
        self.weather_tab = (By.CSS_SELECTOR, 'li[lc="823"]')
        self.currency_tab = (By.CSS_SELECTOR, 'li[lc="763"]')
        self.tab_current = (By.CSS_SELECTOR, 'li[class*="current"]')
        self.fuel_tab = (By.CSS_SELECTOR, 'li[lc="224"]')
        self.orakul_tab = (By.CSS_SELECTOR, 'li[lc="764"]')
        self.afisha_tab = (By.CSS_SELECTOR, 'li[lc="320"]')

    def open(self) -> 'MainPage':
        self.driver.get(self.url)
        return self

    def click_weather_tab(self) -> None:
        self.driver.find_element(*self.weather_tab).click()

    def click_currency_tab(self) -> None:
        self.driver.find_element(*self.currency_tab).click()

    def click_fuel_tab(self) -> None:
        self.driver.find_element(*self.fuel_tab).click()

    def click_orakul_tab(self) -> None:
        self.driver.find_element(*self.orakul_tab).click()

    def click_afisha_tab(self) -> None:
        self.driver.find_element(*self.afisha_tab).click()
