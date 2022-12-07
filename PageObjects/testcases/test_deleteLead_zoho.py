import pytest

from conftest import baseList
from pages.landingPage import landingPage
from utils import readingData
from testresources import Constants


@pytest.mark.parametrize('argVals', readingData.getCellData('DeleteLead', Constants.TEST_CASE_FILE_PATH))
def test_DeleteLead_zoho(argVals):
    testRunMode = readingData.isTestRunnable('DeleteLead', Constants.TEST_CASE_FILE_PATH)
    dataRunMode = argVals[Constants.RUNMODE_COL]

    if (testRunMode):
        if (dataRunMode == Constants.Y):
            for i in range(0, len(baseList)):
                pass

            driver = baseList[i].openbrowser(argVals[Constants.BROWSERNAME])
            login = landingPage(driver).landingpage()
            userName = login.loginpage()
            password = userName.enterUserName()
            homePage = password.enterPassword(argVals[Constants.EXPECTED_RESULT])
            leadHomepage = homePage.homepage()
            leadHomepage.deleteLead(argVals[Constants.LEADNAME])

        else:
            pytest.skip("Test case has been skipped...")

    else:
        pytest.skip("Test case has been skipped...")
