import pytest

from conftest import baseList
from pages.landingPage import landingPage
from utils import readingData
from testresources import Constants


@pytest.mark.parametrize('argVals', readingData.getCellData('CreateDeal', Constants.TEST_CASE_FILE_PATH))
def test_CreateDeal_zoho(argVals):
    testRunMode = readingData.isTestRunnable('CreateDeal', Constants.TEST_CASE_FILE_PATH)
    dataRunMode = argVals[Constants.RUNMODE_COL]

    if (testRunMode):
        if (dataRunMode == Constants.Y):
            for i in range(0, len(baseList)):
                pass

            driver = baseList[i].openbrowser(argVals[Constants.BROWSERNAME])
            login = landingPage(driver).landingpage()
            userName =  login.loginpage()
            password = userName.enterUserName()
            homePage = password.enterPassword(argVals[Constants.EXPECTED_RESULT])
            leadHomepage = homePage.homepage()
            EnterDealDetails = leadHomepage.createDeal()
            dealCheckPage = EnterDealDetails.enterDealDetails(argVals[Constants.DEALNAME], argVals[Constants.ACCOUNTNAME], argVals[Constants.CLOSINGDATE])

            dealCheckPage.dealcheckpage(argVals[Constants.DEALNAME])

        else:
            pytest.skip("Test case has been skipped...")

    else:
        pytest.skip("Test case has been skipped...")
