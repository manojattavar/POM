'''
Created on 25-Jul-2020
@author: jaspreet
'''
import pytest
from utils import readData
from testResources import constants
from conftest import Dlist, Glist

@pytest.mark.usefixtures("base_fixture")
class Test_Lead:
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("argVals", readData.getData("CreateLead", constants.XLS_PATH))
    def test_createLead(self,argVals):
        dataRunMode = argVals[constants.RUNMODE]
        testrunMode = readData.isRunnable("CreateLead", constants.XLS_PATH)
        if(testrunMode):
            if(dataRunMode==constants.RUNMODE_YES):
                #calling driverscript
                for i in range(0,len(Dlist)):
                    pass
                for j in range(0,len(Glist)):
                    pass
                Dlist[i].execute(Glist[j],"CreateLead", constants.XLS_PATH, argVals)
            else:
                pytest.skip("Skipping the test case as run Mode is NO on data sheet")
        else:
            pytest.skip("Skipping the test case reason Runmode is No")
            
    @pytest.mark.run(order=2)        
    @pytest.mark.parametrize("argVals", readData.getData("ConvertLead", constants.XLS_PATH))
    def test_convertLead(self,argVals):
        dataRunMode = argVals[constants.RUNMODE]
        testrunMode = readData.isRunnable("ConvertLead", constants.XLS_PATH)
        if(testrunMode):
            if(dataRunMode==constants.RUNMODE_YES):
                #calling driverscript
                for i in range(0,len(Dlist)):
                    pass
                for j in range(0,len(Glist)):
                    pass
                Dlist[i].execute(Glist[j],"CreateLead", constants.XLS_PATH, argVals)
            else:
                pytest.skip("Skipping the test case as run Mode is NO on data sheet")
        else:
            pytest.skip("Skipping the test case reason Runmode is No")
            
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("argVals", readData.getData("DeleteLead", constants.XLS_PATH))
    def test_deleteLead(self,argVals):
        dataRunMode = argVals[constants.RUNMODE]
        testrunMode = readData.isRunnable("CreateLead", constants.XLS_PATH)
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