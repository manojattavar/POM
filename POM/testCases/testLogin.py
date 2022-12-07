import pytest

from testResources import constants
from utils import ReadingData


@pytest.mark.parametrize('argVals', ReadingData.getCellData('LoginTest', constants.TEST_CASE_FILE_PATH))
def test_login_new(argVals):
    testRunMode = ReadingData.isTestRunnable('LoginTest', constants.TEST_CASE_FILE_PATH)
    dataRunMode = argVals[constants.RUNMODE_COL]

    if (testRunMode):
        if (dataRunMode == constants.Y):
            print(argVals)

        else:
            pytest.skip("Test case has been skipped...")

    else:
        pytest.skip("Test case has been skipped...")