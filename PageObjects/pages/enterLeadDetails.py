from pages.base import BasePage
from pages.leadCheckPage import LeadCheckPage


class EnterLeadDetails(BasePage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def enterLeadDetail(self, accountName, firstName, lastName):
        self.type('companyName_xpath', accountName)
        self.type('firstName_xpath', firstName)
        self.type('lastName_xpath', lastName)
        self.click('saveBtn_id')
        self.click('saveBackArrowBtn_id')
        self.wait()
        return LeadCheckPage(self.driver)
