import pytest

from testResources import constants
from conftest import gList, dList
from utils import ReadingData


@pytest.mark.parametrize("argVals", ReadingData.getCellData('CreateDeal', constants.TEST_CASE_FILE_PATH))
def test_createDeal(argVals):
    testRunMode = ReadingData.isTestRunnable('CreateDeal', constants.TEST_CASE_FILE_PATH)
    dataRunMode = argVals[constants.RUNMODE_COL]

    if (testRunMode):
        if (dataRunMode == constants.Y):

            for i in range(0, len(gList)):
                pass

            for j in range(0, len(dList)):
                pass

            dList[j].execute(gList[i], 'CreateDeal', constants.TEST_CASE_FILE_PATH, argVals)

        else:
            pytest.skip("Test case has been skipped...")

    else:
        pytest.skip("Test case has been skipped...")