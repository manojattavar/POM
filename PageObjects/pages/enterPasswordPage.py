from pages.base import BasePage
from pages.homePage import Homepage
from testresources import Constants


class EnterPassword(BasePage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def enterPassword(self, expResult):
        password = self.prop['password']
        self.type('password_id', password)
        self.click('nextbutton_xpath')
        self.validateLogin('CRMLinkBtn_xpath', expResult)
        self.wait()
        return Homepage(self.driver)
