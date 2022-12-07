import pytest
from pyjavaproperties import Properties

from keywords.genKeywords import genkeywords

prop = Properties()

glist = []

@pytest.yield_fixture(scope='function', autouse=True)
def base_fixture():
    file = open("C:\\Users\\029693744\\PycharmProjects\\dataDrivenFW\\testResources\\config.properties")
    prop.load(file)

    gen = genkeywords()
    glist.append(gen)

    yield locals()