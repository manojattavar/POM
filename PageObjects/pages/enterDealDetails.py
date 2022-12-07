from pages.base import BasePage
from pages.dealCheckPage import DealCheckPage


class EnterDealDetails(BasePage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def enterDealDetails(self, dealName, accountName, closingDate):
        self.type('dealName_id', dealName)
        self.click('dealAccountNameWindow_xpath')
        self.wait()
        rowNum = self.getRowNumberByName('dealAccountNamesList_xpath', accountName)
        self.wait()
        self.clickElementByRowNum(rowNum, 'accuntNamePart1_xpath', 'accuntNamePart2_xpath')
        self.wait()
        self.enterClosingDate(closingDate)
        self.wait()
        self.click('saveBtn_id')
        self.click('saveBackArrowBtn_id')
        return DealCheckPage(self.driver)
