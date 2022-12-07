from testResources import constants
from utils.XLSReader import XLSReader


def getCellData(testCaseName, xlspath):
    xls = XLSReader(xlspath)

    testCaseStartIndex = 0

    try:
        while not (xls.getCellDataByIndex(constants.DATASHEET, testCaseStartIndex, 0) == testCaseName):
            testCaseStartIndex += 1
    except Exception as e:
        print(e)

    testCaseColNameStartIndex = testCaseStartIndex + 1
    testDataValStartIndex = testCaseStartIndex + 2

    maxRows = 0

    try:
        while not (xls.checkEmptyCell(constants.DATASHEET, testDataValStartIndex+maxRows, 0)):
            maxRows += 1
    except Exception as e:
        print(e)

    maxCols = 0

    try:
        while not (xls.checkEmptyCell(constants.DATASHEET, testDataValStartIndex, maxCols)):
            maxCols += 1
    except Exception as e:
        print(e)

    dataList = []
    for rNum in range(testDataValStartIndex, testDataValStartIndex+maxRows):
        dataDict = {}
        for cNum in range(0, maxCols):
            dataKey = xls.getCellDataByIndex(constants.DATASHEET, testCaseColNameStartIndex, cNum)
            dataValue = xls.getCellDataByIndex(constants.DATASHEET, rNum, cNum)
            dataDict[dataKey] = dataValue
        dataList.append(dataDict)
    return dataList


def isTestRunnable(testCaseName, xlspath):
    xls = XLSReader(xlspath)
    rows = xls.getRows(constants.TESTCASES)

    for rowNum in range(0, rows):
        testName = xls.getCellDataByColName(constants.TESTCASES, rowNum, constants.TCID_COL)
        if (testName == testCaseName):
            runMode = xls.getCellDataByColName(constants.TESTCASES, rowNum, constants.RUNMODE_COL)
            if (runMode == constants.Y):
                return True
            else:
                return False
