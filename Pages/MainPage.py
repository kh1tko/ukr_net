from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class MainPage(BasePage):
    textbox_username = (By.XPATH, "//input[@name='login']")
    textbox_password = (By.XPATH, "//input[@name='password']")
    button_signIn = (By.XPATH, "//button[@class='_1_n87kyy']")
    textbox_search_field = (By.CLASS_NAME, "_1_n87kyy")

    forgot_password = (By.XPATH, "//a[@class='_2C_50gb1 _1vp-ZEjb']")

    # createAccount = (By.XPATH, "//a[@class='action create primary']/span")
    # customerLoginText = (By.XPATH, "//*[text()='CustomerLogin']")

    def __init__(self, driver):
        super().__init__(driver)

    def login_to_mail_successfully(self, username, password):
        BasePage.typeText_action(self, element=self.textbox_username, textType=username)
        BasePage.typeText_action(self, element=self.textbox_password, textType=password)
        BasePage.click_action(self, element=self.button_signIn)

    def search_field(self, search_field):
        BasePage.typeText_action(self.textbox_search_field, search_field)

    def clickForgotPassword(self):
        BasePage.click_action(self, element=self.forgot_password)
