'''
Created on 10-Jul-2020
@author: jaspreet
'''
import pytest
from testresources import readingData, constants

class Test_Lead:
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("argVals", readingData.getCellData("CreateLead", constants.XLS_FILE_PATH))
    def test_CreateLead(self,base_fixture,argVals):
        dataRunMode = argVals[constants.RUNMODE_COL]
        testRunMode = readingData.isRunnable("CreateLead", constants.XLS_FILE_PATH)
        if(testRunMode):
            if(dataRunMode==constants.RUNMODE_YES):
                base_fixture['gen'].openBrowser(argVals[constants.BROWSER])
                base_fixture['gen'].navigate("URL")
                base_fixture['gen'].ValidateTitle()
                loginStatus = base_fixture['gen'].doLogin(argVals[constants.USERNAME], argVals[constants.PASSWORD])
                if(loginStatus):
                    base_fixture['gen'].Click("crmlink_xpath")
                    base_fixture['gen'].Click("leadbtn_xpath")
                    base_fixture['gen'].Click("addbtn_xpath")
                    base_fixture['gen'].Type("companyname_id", argVals[constants.COMPANY_NAME])
                    base_fixture['gen'].Type("firstname_id", argVals[constants.FIRSTNAME])
                    base_fixture['gen'].Type("lastname_id", argVals[constants.LASTNAME])
                    base_fixture['gen'].Click("saveleadbtn_id")
                    base_fixture['gen'].Click("leadbtn_xpath")
                    rowNum = base_fixture['gen'].getRowNumByName(argVals[constants.FIRSTNAME]+" "+argVals[constants.LASTNAME])
                    if(rowNum==-1):
                        base_fixture['gen'].reportFailure("LeadName "+argVals[constants.FIRSTNAME]+" "+argVals[constants.LASTNAME]+" not found")
                    else:
                        base_fixture['gen'].reportSuccess("Leadname "+argVals[constants.FIRSTNAME]+" "+argVals[constants.LASTNAME]+" found at row number : "+str(rowNum))
                else:
                    base_fixture['gen'].reportFailure("Reason for test case failure is :"+str(loginStatus))
            else:
                pytest.skip("Reason for skipping the test case since dataRunMode is: "+dataRunMode)
        else:
            pytest.skip("Reason for skipping the test case since testRunMode is: "+str(testRunMode))
     
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("argVals", readingData.getCellData("ConvertLead", constants.XLS_FILE_PATH))
    def test_ConvertLead(self,base_fixture,argVals):
        dataRunMode = argVals[constants.RUNMODE_COL]
        testRunMode = readingData.isRunnable("ConvertLead", constants.XLS_FILE_PATH)
        if(testRunMode):
            if(dataRunMode==constants.RUNMODE_YES):
                base_fixture['gen'].openBrowser(argVals[constants.BROWSER])
                base_fixture['gen'].navigate("URL")
                base_fixture['gen'].ValidateTitle()
                loginStatus = base_fixture['gen'].doLogin(argVals[constants.USERNAME], argVals[constants.PASSWORD])
                if(loginStatus):
                    base_fixture['gen'].Click("crmlink_xpath")
                    base_fixture['gen'].Click("leadbtn_xpath")
                    rNum = base_fixture['gen'].getRowNumByName(argVals[constants.LEADNAME])
                    if(rNum==-1):
                        base_fixture['gen'].reportFailure("Lead "+argVals[constants.LEADNAME]+" not found")
                    else:
                        base_fixture['gen'].ClickonLeadName(argVals[constants.LEADNAME])
                        base_fixture['gen'].Click("convertBtn_xpath")
                        base_fixture['gen'].Click("saveConvertLeadbtn_xpath")
                        base_fixture['gen'].Click("gotoleadsBtn_name")
                        rNum = base_fixture['gen'].getRowNumByName(argVals[constants.LEADNAME])
                        if(rNum==-1):
                            base_fixture['gen'].reportSuccess("Lead "+argVals[constants.LEADNAME]+" converted, not found in lead list")
                        else:
                            base_fixture['gen'].reportFailure("Lead "+argVals[constants.LEADNAME]+" not converted, found in lead list at row no. "+str(rNum))
                else:
                    base_fixture['gen'].reportFailure("Reason for test case failure is :"+str(loginStatus))
            else:
                pytest.skip("Reason for skipping the test case since dataRunMode is: "+dataRunMode)
        else:
            pytest.skip("Reason for skipping the test case since testRunMode is: "+str(testRunMode)) 
                            
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("argVals", readingData.getCellData("DeleteLead", constants.XLS_FILE_PATH))
    def test_DeleteLead(self,base_fixture,argVals):
        dataRunMode = argVals[constants.RUNMODE_COL]
        testRunMode = readingData.isRunnable("DeleteLead", constants.XLS_FILE_PATH)
        if(testRunMode):
            if(dataRunMode==constants.RUNMODE_YES):
                base_fixture['gen'].openBrowser(argVals[constants.BROWSER])
                base_fixture['gen'].navigate("URL")
                base_fixture['gen'].ValidateTitle()
                loginStatus = base_fixture['gen'].doLogin(argVals[constants.USERNAME], argVals[constants.PASSWORD])
                if(loginStatus):
                    base_fixture['gen'].Click("crmlink_xpath")
                    base_fixture['gen'].Click("contactLink_xpath")
                    rNum = base_fixture['gen'].getRowNumByName(argVals[constants.LEADNAME])
                    if(rNum==-1):
                        base_fixture['gen'].reportFailure("Lead "+argVals[constants.LEADNAME]+" not found")
                    else:
                        base_fixture['gen'].ClickonLeadName(argVals[constants.LEADNAME]) 
                        base_fixture['gen'].Click("options_id")
                        base_fixture['gen'].Click("deletebtn_xpath")  
                        base_fixture['gen'].DeleteLead()
                        rNum = base_fixture['gen'].getRowNumByName(argVals[constants.LEADNAME])
                        if(rNum==-1):
                            base_fixture['gen'].reportSuccess("Lead "+argVals[constants.LEADNAME]+" deleted, not found in lead list")
                        else:
                            base_fixture['gen'].reportFailure("Lead "+argVals[constants.LEADNAME]+" not deleted, found in lead list at row no. "+str(rNum))
                else:
                    base_fixture['gen'].reportFailure("Reason for test case failure is :"+str(loginStatus))
            else:
                pytest.skip("Reason for skipping the test case since dataRunMode is: "+dataRunMode)
        else:
            pytest.skip("Reason for skipping the test case since testRunMode is: "+str(testRunMode))          
                    
    