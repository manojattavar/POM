import pytest
from pyjavaproperties import Properties

from testResources import constants

prop = Properties()

@pytest.yield_fixture(scope='function', autouse=True)
def base_fixture():
    file = open(constants.CONFIG_FILE)
    prop.load(file)

    yield locals()