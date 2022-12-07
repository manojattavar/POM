from testResources import Constants
from utils.XLSReader import XLSReader


def getCellData(testCaseName, xlspath):
    xls = XLSReader(xlspath)

    testCaseStartRowNumber = 0

    try:
        while not (xls.getCellDataByIndex(Constants.DATASHEET, testCaseStartRowNumber, 0) == testCaseName):
            testCaseStartRowNumber += 1
    except Exception as e:
        print(e)

    testCaseColNameRowIndex = testCaseStartRowNumber + 1
    testDataValueStartIndex = testCaseStartRowNumber + 2

    maxRows = 0

    try:
        while not (xls.checkCellEmpty(Constants.DATASHEET, testDataValueStartIndex + maxRows, 0)):
            maxRows += 1
    except Exception as e:
        print(e)

    maxCols = 0

    try:
        while not (xls.checkCellEmpty(Constants.DATASHEET, testDataValueStartIndex, maxCols)):
            maxCols += 1
    except Exception as e:
        print(e)

    dataList = []
    for rowInd in range(testDataValueStartIndex, testDataValueStartIndex+maxRows):
        dataDict = {}
        for colInd in range(0, maxCols):
            dataKey = xls.getCellDataByIndex(Constants.DATASHEET, testCaseColNameRowIndex, colInd)
            dataValue = xls.getCellDataByIndex(Constants.DATASHEET, rowInd, colInd)
            dataDict[dataKey] = dataValue
        dataList.append(dataDict)
    return dataList


# getCellData('CreateLead', "C:\\Users\\029693744\\PycharmProjects\\DataDrivenFramework3\\testResources\\DDF.xls")