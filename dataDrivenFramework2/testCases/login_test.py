import pytest

from conftest import glist
from utils import ReadingData, constants


@pytest.mark.parametrize('argVals', ReadingData.getCellData('LoginTest', constants.TEST_CASE_FILE_PATH))
def login_test(argVals):
    testRunMode = ReadingData.isTestRunnable('LoginTest', constants.TEST_CASE_FILE_PATH)
    dataRunMode = argVals['RunMode']

    if (testRunMode):
        for i in range(0, len(glist)):
            pass

        

    else:
        pytest.skip("skip test cases")