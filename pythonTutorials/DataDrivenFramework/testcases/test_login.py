import pytest


class Testlogin:
    @pytest.mark.parametrize("argVals", readingData.getCellData("LoginTest", constants.XLS_FILE_PATH))
    def test_login(self,argVals,base_fixture):
        dataRunMode = argVals[constants.RUNMODE_COL]
        testRunMode = readingData.isRunnable("LoginTest", constants.XLS_FILE_PATH)
        if(testRunMode):
            if(dataRunMode==constants.RUNMODE_YES):
                base_fixture['gen'].openBrowser(argVals[constants.BROWSER])
                base_fixture['gen'].navigate("URL")
                base_fixture['gen'].ValidateTitle()
                loginStatus = base_fixture['gen'].doLogin(argVals[constants.USERNAME], argVals[constants.PASSWORD])
                if loginStatus:
                    if(argVals[constants.EXPECTED_RESULT]==constants.EXPECTED_SUCCESS):
                        base_fixture['gen'].reportSuccess("Login Success as expected..Test case Passed")
                    else:
                        base_fixture['gen'].reportFailure("Login Failed unexpectedly")
                else:
                    base_fixture['gen'].reportFailure("Reason for test case failure is :"+str(loginStatus))
            else:
                pytest.skip("Reason for skipping the test case since dataRunMode is: "+dataRunMode)
        else:
            pytest.skip("Reason for skipping the test case since testRunMode is: "+str(testRunMode))
    