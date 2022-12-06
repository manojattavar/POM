from testresources.dataReading import XLSReader
from testresources import constants


def getCellData(testcasename,path):
    dataList = []
    xls = XLSReader(path)

    testStartRowIndex = 0
    while not(xls.getCellData(constants.DATASHEET, testStartRowIndex, 0)==testcasename):
        testStartRowIndex = testStartRowIndex+1
    
    colStartRowIndex = testStartRowIndex+1
    dataStartRowIndex = testStartRowIndex+2
    
    maxRows = 0
    try:
        while not(xls.checkEmptyCell(constants.DATASHEET, dataStartRowIndex+maxRows,0)):
            maxRows = maxRows+1
    except IndexError:
        pass
    
    maxCols = 0
    try:
        while not(xls.checkEmptyCell(constants.DATASHEET, colStartRowIndex, maxCols)):
            maxCols = maxCols+1
    except IndexError:
        pass
    
    for rowNum in range(dataStartRowIndex, dataStartRowIndex+maxRows):
        dataDictionary = {}
        for colNum in range(0,maxCols):
            dataKey = xls.getCellData(constants.DATASHEET, colStartRowIndex, colNum)
            dataValue = xls.getCellData(constants.DATASHEET, rowNum, colNum)
            dataDictionary[dataKey]=dataValue
        dataList.append(dataDictionary)
    return dataList 

def isRunnable(testcasename,path):
    xls = XLSReader(path)
    row = xls.rowCount(constants.TESTSHEET)
    for rNum in range(0,row):
        tName = xls.getCellDataByColName(constants.TESTSHEET, rNum, constants.TCID_COL)
        if(testcasename==tName):
            runMode = xls.getCellDataByColName(constants.TESTSHEET, rNum, constants.RUNMODE_COL)
            if(runMode==constants.RUNMODE_YES):
                return True
            else:
                return False
        