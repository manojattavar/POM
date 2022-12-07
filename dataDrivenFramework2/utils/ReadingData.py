from utils import constants
from utils.XLSReader import XLSReader


def getCellData(testCaseName, xlspath):
    xls = XLSReader(xlspath)

    testCaseStartRowInd = 0
    try:
        while not (xls.getCellDataByIndex(constants.DATASHEET, testCaseStartRowInd, 0) == testCaseName):
            testCaseStartRowInd += 1
    except Exception as e:
        print(e)

    testCaseColNameStartInd = testCaseStartRowInd + 1
    testDataValueStartInd = testCaseStartRowInd + 2

    maxRows = 0

    try:
        while not (xls.checkEmptyCell(constants.DATASHEET, testDataValueStartInd+maxRows, 0)):
            maxRows += 1
    except Exception as e:
        print(e)

    maxCols = 0

    try:
        while not (xls.checkEmptyCell(constants.DATASHEET, testDataValueStartInd, maxCols)):
            maxCols += 1
    except Exception as e:
        print(e)

    dataList = []
    for rowNum in range(testDataValueStartInd, testDataValueStartInd+maxRows):
        dataDict = {}
        for colNum in range(0, maxCols):
            dataKey = xls.getCellDataByIndex(constants.DATASHEET, testCaseColNameStartInd, colNum)
            dataValue = xls.getCellDataByIndex(constants.DATASHEET, rowNum, colNum)
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