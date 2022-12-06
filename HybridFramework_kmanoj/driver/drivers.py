import sys

from keywords.genkeywords import genkeyword
from testResources import constants
from utils.XLSReader import xlsReader

class driverScript:
    def execute(self, gen, testCaseName, xlspath, testData):
        xls = xlsReader(xlspath)

        rowCount = xls.getRowCount(constants.KEYWORD)

        for rowNum in range(0, rowCount):
            testName = xls.getCellDataByColName(constants.KEYWORD, rowNum, constants.TCID_COL)
            if (testName == testCaseName):
                keyword = xls.getCellDataByColName(constants.KEYWORD, rowNum, constants.KEYWORD_COL)
                object = xls.getCellDataByColName(constants.KEYWORD, rowNum, constants.OBJECT_COL)
                data = xls.getCellDataByColName(constants.KEYWORD, rowNum, constants.DATA_COL)

                gen.setObject(object)
                gen.setData(data)
                gen.setTestData(testData)

                genkey = getattr(sys.modules[__name__], "genkeyword")
                getattr(genkey, keyword)(gen)

