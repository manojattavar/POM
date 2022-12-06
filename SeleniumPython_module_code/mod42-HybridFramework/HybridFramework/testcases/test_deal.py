'''
Created on 01-Aug-2020
@author: jaspreet
'''
import pytest
from utils import readData
from testResources import constants
import conftest
from conftest import Dlist, Glist


@pytest.mark.usefixtures("base_fixture")
class Test_Deal:
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("argVals", readData.getData("CreateDeal", constants.XLS_PATH))
    def test_createDeal(self,argVals):
        dataRunMode = argVals[constants.RUNMODE]
        testrunMode = readData.isRunnable("CreateDeal", constants.XLS_PATH)
        if(testrunMode):
            if(dataRunMode==constants.RUNMODE_YES):
                #calling driverscript 
                for i in range(0,len(Dlist)):
                    pass
                for j in range(0,len(Glist)):
                    pass
                Dlist[i].execute(Glist[j],"CreateDeal", constants.XLS_PATH, argVals)            
            else:
                pytest.skip("Skipping the test case as run Mode is NO on data sheet")
        else:
            pytest.skip("Skipping the test case reason Runmode is No")
            
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("argVals", readData.getData("DeleteDeal", constants.XLS_PATH))
    def test_deleteDeal(self,argVals):
        dataRunMode = argVals[constants.RUNMODE]
        testrunMode = readData.isRunnable("DeleteDeal", constants.XLS_PATH)
        if(testrunMode):
            if(dataRunMode==constants.RUNMODE_YES):
                #calling driverscript
                for i in range(0,len(Dlist)):
                    pass
                for j in range(0,len(Glist)):
                    pass
                Dlist[i].execute(Glist[j],"DeleteDeal", constants.XLS_PATH, argVals)     
            else:
                pytest.skip("Skipping the test case as run Mode is NO on data sheet")
        else:
            pytest.skip("Skipping the test case reason Runmode is No")