from testresources import Constants
from utils.xlsReader import XLSReader


def getCellData(testCaseName, xlspath):
    testCaseStartRowIndex = 0

    xls = XLSReader(xlspath)

    while not (xls.getCellDataByIndex(Constants.DATASHEET, testCaseStartRowIndex, 0) == testCaseName):
        testCaseStartRowIndex += 1

    testCaseColRowStartIndex = testCaseStartRowIndex + 1
    dataValRowStartIndex = testCaseStartRowIndex + 2

    maxRows = 0
    try:
        while not (xls.checkEmptyCell(Constants.DATASHEET, dataValRowStartIndex + maxRows, 0)):
            maxRows += 1
    except Exception as e:
        print(e)

    maxColumns = 0
    try:
        while not (xls.checkEmptyCell(Constants.DATASHEET, testCaseColRowStartIndex, maxColumns)):
            maxColumns += 1
    except Exception as e:
        print(e)

    dataList = []
    for rNum in range(dataValRowStartIndex, dataValRowStartIndex+maxRows):
        dataDict = {}
        for cNum in range(0, maxColumns):
            dataKey = xls.getCellDataByIndex(Constants.DATASHEET, testCaseColRowStartIndex, cNum)
            dataValue = xls.getCellDataByIndex(Constants.DATASHEET, rNum, cNum)
            dataDict[dataKey] = dataValue
        dataList.append(dataDict)
    return dataList

def isTestRunnable(testCaseName, xlspath):
    xls = XLSReader(xlspath)

    for rNum in range(0, xls.getRowCount(Constants.TESTCASES)):
        testName = xls.getCellDataByColName(Constants.TESTCASES, rNum, Constants.TCID_COL)
        if (testName == testCaseName):
            runMode = xls.getCellDataByColName(Constants.TESTCASES, rNum, Constants.RUNMODE_COL)
            if (runMode == Constants.Y):
                return True
            else:
                return False