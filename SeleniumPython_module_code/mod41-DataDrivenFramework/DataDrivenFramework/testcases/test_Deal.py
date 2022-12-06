from testresources import readingData, constants


class TestDeal:
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("argVals", readingData.getCellData("CreateDeal", constants.XLS_FILE_PATH))
    def test_createdeal(self,base_fixture,argVals):
        dataRunMode = argVals[constants.RUNMODE_COL]
        testRunMode = readingData.isRunnable("CreateDeal", constants.XLS_FILE_PATH)
        if(testRunMode):
            if(dataRunMode==constants.RUNMODE_YES):
                base_fixture['gen'].openBrowser(argVals[constants.BROWSER])
                base_fixture['gen'].navigate("URL")
                base_fixture['gen'].ValidateTitle()
#                 loginStatus = base_fixture['gen'].doLogin(argVals[constants.USERNAME], argVals[constants.PASSWORD])
#                 if(loginStatus):
#                     base_fixture['gen'].Click("crmlink_xpath")
#                     base_fixture['gen'].Click("optionsTab_xpath")
#                     base_fixture['gen'].Click("dealLink_xpath")
#                     base_fixture['gen'].Click("addbtn_xpath")
#                     base_fixture['gen'].Type("DealNametxtBox_xpath", argVals[constants.DEALNAME])
#                     base_fixture['gen'].Type("accounttxtBox_xpath", argVals[constants.ACCOUNTNAME])
#                     base_fixture['gen'].Type("stage_xpath", argVals[constants.STAGE])
#                     base_fixture['gen'].SelectDate(argVals[constants.CLOSING_DATE])
#                     time.sleep(2)
#                     base_fixture['gen'].Click("saveDealbtn_xpath")
#                     base_fixture['gen'].Click("backBtn_xpath")
#                     rowNum = base_fixture['gen'].getRowNumByName(argVals[constants.DEALNAME])
#                     if(rowNum==-1):
#                         base_fixture['gen'].reportFailure("Deal Name "+argVals[constants.DEALNAME]+" not found")
#                     else:
#                         base_fixture['gen'].reportSuccess("Deal Name "+argVals[constants.DEALNAME]+" found at row number : "+str(rowNum))
#                 else:
#                     base_fixture['gen'].reportFailure("Reason for test case failure is :"+str(loginStatus))
            else:
                pytest.skip("Reason for skipping the test case since dataRunMode is: "+dataRunMode)
        else:
            pytest.skip("Reason for skipping the test case since testRunMode is: "+str(testRunMode))

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("argVals", readingData.getCellData("DeleteDeal", constants.XLS_FILE_PATH))
    def test_DeleteLead(self,base_fixture,argVals):
        dataRunMode = argVals[constants.RUNMODE_COL]
        testRunMode = readingData.isRunnable("DeleteDeal", constants.XLS_FILE_PATH)
        if(testRunMode):
            if(dataRunMode==constants.RUNMODE_YES):
                base_fixture['gen'].openBrowser(argVals[constants.BROWSER])
                base_fixture['gen'].navigate("URL")
                base_fixture['gen'].ValidateTitle()
#                 loginStatus = base_fixture['gen'].doLogin(argVals[constants.USERNAME], argVals[constants.PASSWORD])
#                 if(loginStatus):
#                     base_fixture['gen'].Click("crmlink_xpath")
#                     base_fixture['gen'].Click("optionsTab_xpath")
#                     base_fixture['gen'].Click("dealLink_xpath")
#                     rNum = base_fixture['gen'].getRowNumByName(argVals[constants.DEALNAME])
#                     if(rNum==-1):
#                         base_fixture['gen'].reportFailure("Deal name "+argVals[constants.DEALNAME]+" not found")
#                     else:
#                         base_fixture['gen'].ClickonLeadName(argVals[constants.DEALNAME]) 
#                         base_fixture['gen'].Click("options_id")
#                         base_fixture['gen'].Click("deletedeal_xpath")  
#                         base_fixture['gen'].DeleteLead()
#                         rNum = base_fixture['gen'].getRowNumByName(argVals[constants.DEALNAME])
#                         if(rNum==-1):
#                             base_fixture['gen'].reportSuccess("Deal name "+argVals[constants.DEALNAME]+" deleted, not found in lead list")
#                         else:
#                             base_fixture['gen'].reportFailure("Deal name "+argVals[constants.DEALNAME]+" not deleted, found in lead list at row no. "+str(rNum))
#                 else:
#                     base_fixture['gen'].reportFailure("Reason for test case failure is :"+str(loginStatus))
            else:
                pytest.skip("Reason for skipping the test case since dataRunMode is: "+dataRunMode)
        else:
            pytest.skip("Reason for skipping the test case since testRunMode is: "+str(testRunMode)) 