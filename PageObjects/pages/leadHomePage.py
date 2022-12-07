from pages.base import BasePage
from pages.enterDealDetails import EnterDealDetails
from pages.enterLeadDetails import EnterLeadDetails


class LeadHomePage(BasePage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def createLead(self):
        self.click('LeadsHomePageBtn_xpath')
        self.click('createLeadBtn_xpath')
        return EnterLeadDetails(self.driver)

    def convertLead(self, leadName):
        self.click('LeadsHomePageBtn_xpath')
        rowNum = self.getRowNumberByName('nameList_xpath', leadName)
        self.wait()
        if (rowNum != -1):
            self.clickElementByRowNum(rowNum, 'namePart1_xpath', 'namePart2_xpath')
            self.wait()
            self.click('convertBtn_name')
            self.click('convertBtnConfirmation_id')
            self.wait()
            self.click('goToLeadsButton_id')
            self.wait()

            rowNum = self.getRowNumberByName('nameList_xpath', leadName)
            self.wait()

            if (rowNum == -1):
                self.reportSuccess("Lead ID " + leadName + " is not present")
            else:
                self.reportFailure("Lead ID " + leadName + " is present at the row number " + str(rowNum))
        else:
            self.reportFailure("Lead ID " + leadName + " is not present...")

    def deleteLead(self, leadName):
        self.click('LeadsHomePageBtn_xpath')
        rowNum = self.getRowNumberByName('nameList_xpath', leadName)
        self.wait()
        if (rowNum != -1):
            self.clickElementByRowNum(rowNum, 'namePart1_xpath', 'namePart2_xpath')
            self.wait()
            self.click('deleteHomePageBtn_id')
            self.click('deleteActualBtn_xpath')
            self.wait()
            self.click('deleteAlertButton_xpath')
            self.wait()
            self.refresh()

            rowNum = self.getRowNumberByName('nameList_xpath', leadName)
            self.wait()

            if (rowNum == -1):
                self.reportSuccess("Lead ID " + leadName + " is not present")
            else:
                self.reportFailure("Lead ID " + leadName + " is present at the row number " + str(rowNum))
        else:
            self.reportFailure("Lead ID " + leadName + " is not present...")


    def createDeal(self):
        self.click('dealHomePageBtn_xpath')
        self.click('createDeal_xpath')
        return EnterDealDetails(self.driver)

    def deleteDeal(self, dealName):
        self.click('dealHomePageBtn_xpath')
        rowNum = self.getRowNumberByName('dealNameList_xpath', dealName)
        self.wait()
        if (rowNum != -1):
            self.clickElementByRowNum(rowNum, 'dealButtonXpath1_xpath', 'dealButtonXpath2_xpath')
            self.wait()
            self.click('deleteHomePageBtn_id')
            self.click('deleteActualBtn_xpath')
            self.wait()
            self.click('deleteAlertButton_xpath')
            self.wait()
            self.refresh()

            rowNum = self.getRowNumberByName('dealNameList_xpath', dealName)
            self.wait()

            if (rowNum == -1):
                self.reportSuccess("Deal ID " + dealName + " is not present")
            else:
                self.reportFailure("Deal ID " + dealName + " is present at the row number " + str(rowNum))
        else:
            self.reportFailure("Deal ID " + dealName + " is not present...")