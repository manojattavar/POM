import allure
import pytest
from pyjavaproperties import Properties

from driver.drivers import driverScript
from keywords.genkeywords import genkeyword
from testResources import constants

env = Properties()
prod = Properties()

gList = []
dList = []

@pytest.yield_fixture(scope='function', autouse=True)
def base_fixture():
    with allure.step("Initializing block..."):
        envPropFile = open(constants.ENV_CONFIG_FILE)
        env.load(envPropFile)

        prodPropFile = open(constants.PROJECT_PATH + "testResources\\" + env['env'] + ".properties")
        prod.load(prodPropFile)

        gen = genkeyword()
        gList.append(gen)

        d = driverScript()
        dList.append(d)

    yield locals()
    with allure.step("Closing block..."):
        gen.quit()