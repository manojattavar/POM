import xlrd
from _overlapped import NULL


class XLSReader:
    def __init__(self, xlspath):
        self.xlspath = xlspath
        self.xls = xlrd.open_workbook(xlspath)

    def getCellDataByIndex(self, sheetName, rowInd, colInd):
        sheet = self.xls.sheet_by_name(sheetName)
        cell = sheet.cell_value(rowInd, colInd)
        return cell

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

    def getCols(self, sheetName):
        sheet = self.xls.sheet_by_name(sheetName)
        return sheet.ncols

    def getCellDataByColName(self, sheetName, rowNum, colName):
        for cNum in range(0, self.getCols(sheetName)):
            extractedCol = self.getCellDataByIndex(sheetName, 0, cNum)
            if (extractedCol == colName):
                data = self.getCellDataByIndex(sheetName, rowNum, cNum)
                if (data != NULL):
                    return data
                else:
                    return ''
