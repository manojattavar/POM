'''
Created on 04-Jul-2020

@author: jaspreet
'''
import allure
from pyjavaproperties import Properties
import pytest
from testresources.generickeywords import genkeywords

prop = Properties()
@pytest.yield_fixture(scope='function',autouse=True)
def base_fixture():
    with allure.step("Initializing Properties File...."):
        try:
            propertiesFile = open("D:\\eclipse\\DataDrivenFramework\\config.properties")
            prop.load(propertiesFile)
            #15 test case = 15 browsers
            #close the browser at any condition be it fail or pass
            #Grid
            gen = genkeywords()
        except FileNotFoundError as f:
            print(f)
    yield locals()
    with allure.step("Quitting as Tear Down Process...."):
        gen.Quit()
