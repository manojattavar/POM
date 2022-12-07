import allure
import pytest
from pyjavaproperties import Properties

from keywords.genKeywords import genKeywords
from utils import constants

prop = Properties()
glist = []

@pytest.yield_fixture(scope='function', autouse=True)
def base_fixture():
    with allure.step("Initializing block..."):
        file = open(constants.ENV_CONFIG_FILE)
        prop.load(file)

        gen = genKeywords()
        glist.append(gen)

        yield locals()

    with allure.step("Finishing block..."):
        pass
