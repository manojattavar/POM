'''
Created on 23-Jul-2020
@author: jaspreet
'''
from utils.readingData import XLSReader
from testResources import constants
def getData(testCaseName, xlsPath):
    dataList = []
    xls = XLSReader(xlsPath)
    
    testStartRowIndex = 0
    while not(xls.getCellData(constants.DATASHEET, testStartRowIndex, 0)==testCaseName):
        testStartRowIndex = testStartRowIndex+1
    
    colStartRowIndex = testStartRowIndex+1
    dataStartRowIndex = testStartRowIndex+2
    
    maxRows = 0
    try:
        while not(xls.checkEmptyCell(constants.DATASHEET, dataStartRowIndex+maxRows, 0)):
            maxRows = maxRows+1
    except Exception:
        pass
    
    maxCols = 0
    try:
        while not(xls.checkEmptyCell(constants.DATASHEET,colStartRowIndex, maxCols)):
            maxCols = maxCols+1
    except Exception:
        pass
    
    for rNum in range(dataStartRowIndex, dataStartRowIndex+maxRows):
        dataDictionary = {}
        for cNum in range(0, maxCols):
            dataKey = xls.getCellData(constants.DATASHEET, colStartRowIndex, cNum)
            dataValue = xls.getCellData(constants.DATASHEET, rNum, cNum)
            dataDictionary[dataKey]=dataValue
        dataList.append(dataDictionary)
    return dataList

def isRunnable(testCaseName, xlsPath):
    xls = XLSReader(xlsPath)
    rows = xls.rowCount(constants.TESTCASESHEET)
    for rNum in range(0, rows):
        tName = xls.getCellDataByColName(constants.TESTCASESHEET, rNum, constants.TCID)
        if(tName == testCaseName):
            runMode = xls.getCellDataByColName(constants.TESTCASESHEET, rNum, constants.RUNMODE)
            if(runMode==constants.RUNMODE_YES):
                return True
            else:
                return False        
    
