from pages.base import BasePage
from pages.enterPasswordPage import EnterPassword
from testresources import Constants


class EnterUserName(BasePage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def enterUserName(self):
        username = self.prop['username']
        self.type('email_id', username)
        self.click('nextbutton_xpath')
        return EnterPassword(self.driver)