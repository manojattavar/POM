from pages.base import BasePage
from pages.enterUserNamePage import EnterUserName


class login(BasePage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def loginpage(self):
        self.click('signin_xpath')
        return EnterUserName(self.driver)