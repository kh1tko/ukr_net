from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def typeText_action(self, element, textType):
        elem = self.driver.find_element(*element)
        elem.send_keys(textType)

    def click_action(self, element):
        elem = self.driver.find_element(*element)
        elem.click()

    def get_elementText(self, element):
        elem = self.driver.find_element(*element)
        return elem.text

    def elementEnableStatus(self, element):
        elem = self.driver.find_element(*element)
        return elem.is_enabled()

    def elementDisplayStatus(self, element):
        elem = self.driver.find_element(*element)
        return elem.is_displayed()

    def get_pageTitle(self):
        return self.driver.title
