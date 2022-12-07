import xlrd
from _overlapped import NULL


class XLSReader():
    def __init__(self, xlspath):
        self.xlspath = xlspath
        self.xls = xlrd.open_workbook(xlspath)

    def getCellDataByIndex(self, sheetName, rowInd, colInd):
        sheet = self.xls.sheet_by_name(sheetName)
        data = sheet.cell_value(rowInd, colInd)
        if (data != NULL or data != ''):
            return data
        else:
            print("No data found")

    def checkEmptyCell(self, sheetName, rowInd, colInd):
        sheet = self.xls.sheet_by_name(sheetName)
        cell_type = sheet.cell_type(rowInd, colInd)
        if (cell_type == xlrd.XL_CELL_EMPTY):
            return True
        else:
            return False

    def getRows(self, sheetName):
        sheet = self.xls.sheet_by_name(sheetName)
        return sheet.nrows

    def getColumns(self, sheetName):
        sheet = self.xls.sheet_by_name(sheetName)
        return sheet.ncols

    def getCellDataByColName(self, sheetName, rowNum, colName):
        for colNum in range(0, self.getColumns(sheetName)):
            extractedColName = self.getCellDataByIndex(sheetName, 0, colNum)
            if (extractedColName == colName):
                data = self.getCellDataByIndex(sheetName, rowNum, colName)
                if (data != NULL):
                    return data
                else:
                    return ''