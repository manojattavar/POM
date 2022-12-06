'''
Created on 22-Jul-2020
@author: jaspreet
'''
from pyjavaproperties import Properties
import pytest
from keywords.genkeyword import genKeywords
import allure
from DriverScript.driverScript import driverScript

prod=Properties()
envProp=Properties()

Dlist=[]
Glist=[]

@pytest.yield_fixture(scope='function', autouse=True)
def base_fixture():
    with allure.step("Initializing block....."):
        try:              
            prodPath= open("D:\\eclipse\\HybridFramework\\utils\\environment.properties")
            prod.load(prodPath)
            
            path= open("D:\\eclipse\\HybridFramework\\utils\\"+prod['env']+".properties")
            envProp.load(path) 
            d = driverScript()
            Dlist.append(d)
            
            gen = genKeywords()
            Glist.append(gen)
        except FileNotFoundError as f:
            print(f)
    yield locals()
    with allure.step("Finishing block....."):
        gen.quit()
