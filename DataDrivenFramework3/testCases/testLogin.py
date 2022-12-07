import pytest

from testResources import Constants
from utils import ReadingData


@pytest.mark.parametrize('argVals', ReadingData.getCellData('LoginTest', Constants.TEST_CASE_FILE_PATH))
def testLogin(argVals):
    pass