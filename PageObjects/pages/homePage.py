from pages.base import BasePage
from pages.leadHomePage import LeadHomePage


class Homepage(BasePage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def homepage(self):
        self.click('CRMLinkBtn_xpath')
        return LeadHomePage(self.driver)