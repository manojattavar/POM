'''
Created on 23-Jul-2020
@author: jaspreet
'''
from utils.readingData import XLSReader
from testResources import constants
from keywords.genkeyword import genKeywords
import sys

class driverScript:
    def execute(self, key,testCaseName, xlsPath, testData):
        xls = XLSReader(xlsPath)
        rows = xls.rowCount(constants.KEYWORD)
        for rNum in range(0, rows):
            tName = xls.getCellDataByColName(constants.KEYWORDSHEET, rNum, constants.TCID)
            if(tName==testCaseName):
                keywordKey = xls.getCellDataByColName(constants.KEYWORDSHEET, rNum, constants.KEYWORD)
                objectKey = xls.getCellDataByColName(constants.KEYWORDSHEET, rNum, constants.OBJECT)
                dataKey = xls.getCellDataByColName(constants.KEYWORDSHEET, rNum, constants.DATA)
                          
                key.set_ObjectKey(objectKey)
                key.set_dataKey(dataKey)
                key.set_data(testData)
                          
                y = getattr(sys.modules[__name__], 'genKeywords')
                getattr(y, keywordKey)(key)