from pages.base import BasePage


class LeadCheckPage(BasePage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def leadcheckpage(self, name):
        rowNum = self.getRowNumberByName('nameList_xpath', name)
        self.wait()
        if (rowNum != -1):
            self.reportSuccess("Lead ID " + name + " is present at the row number " + str(rowNum))
        else:
            self.reportFailure("Lead ID " + name + " is not present...")
