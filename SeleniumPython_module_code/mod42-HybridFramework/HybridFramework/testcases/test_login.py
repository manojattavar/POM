'''
Created on 24-Jul-2020
@author: jaspreet
'''
import pytest
from utils import readData
from testResources import constants
from conftest import Dlist, Glist

@pytest.mark.usefixtures("base_fixture")
class Test_Login:
    @pytest.mark.parametrize("argVals", readData.getData("LoginTest", constants.XLS_PATH))
    def test_Login(self,argVals):
        dataRunMode = argVals[constants.RUNMODE]
        testrunMode = readData.isRunnable("LoginTest", constants.XLS_PATH)
        if(testrunMode):
            if(dataRunMode==constants.RUNMODE_YES):
                #calling driverscript
                for i in range(0,len(Dlist)):
                    pass
                for j in range(0,len(Glist)):
                    pass
                Dlist[i].execute(Glist[j],"LoginTest", constants.XLS_PATH, argVals)
            else:
                pytest.skip("Skipping the test case as run Mode is No on data sheet")
        else:
            pytest.skip("Skipping the test case reason Runmode is No")