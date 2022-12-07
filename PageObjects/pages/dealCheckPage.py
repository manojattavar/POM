from pages.base import BasePage


class DealCheckPage(BasePage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def dealcheckpage(self, name):
        rowNum = self.getRowNumberByName('dealNameList_xpath', name)
        self.wait()
        if (rowNum != -1):
            self.reportSuccess("Deal ID " + name + " is present at the row number " + str(rowNum))
        else:
            self.reportFailure("Deal ID " + name + " is not present...")
