import pytest

from testResources import constants
from utils import ReadingData


@pytest.mark.parametrize("argVals", ReadingData.getCellData('Logintest', constants.TEST_CASE_FILE_PATH))
def test_login(argVals):
    print(argVals)
    testRunMode = ReadingData.isTestRunnable('LoginTest', constants.TEST_CASE_FILE_PATH)
    dataRunMode = argVals[constants.RUNMODE_COL]
    if (testRunMode):
        if (dataRunMode):
            print(argVals)