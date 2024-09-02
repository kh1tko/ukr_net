from Pages.MainPage import MainPage
from Configuration.TestData import TestData


class Test_login:
    def test_login_to_mail_successfully(self, firefox):
        self.driver = firefox
        self.driver.get(TestData.URL)
        main_page = MainPage(self.driver)
        main_page.login_to_mail_successfully(username=TestData.USERNAME, password=TestData.PASSWORD)
        assert "Mailbox" in self.driver.title
        print(self.driver.title)

    def test_forgot_password(self, firefox):
        self.driver = firefox
        self.driver.get(TestData.URL)
        main_page = MainPage(self.driver)
        assert main_page.get_pageTitle() == 'UKR.NET: Всі новини України, останні новини дня в Україні та Світі'
