import pytest
from pyjavaproperties import Properties

from pages.base import BasePage
from testresources import Constants

prop = Properties()
baseList = []

@pytest.yield_fixture(scope='function', autouse=True)
def base_fixture():
    file = open(Constants.CONFIG_FILE)
    prop.load(file)

    base = BasePage()
    baseList.append(base)

    yield locals()
    base.quit()