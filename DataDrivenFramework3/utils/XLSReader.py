import xlrd
from _overlapped import NULL


class XLSReader:
    def __init__(self, xlspath):
        self.xlspath = xlspath
        self.xls = xlrd.open_workbook(xlspath)

    def getCellDataByIndex(self, sheetName, rowInd, colInd):
        sheet = self.xls.sheet_by_name(sheetName)
        data = sheet.cell_value(rowInd, colInd)
        if (data != NULL):
            return data
        else:
            print("data not found")

    def checkCellEmpty(self, sheetName, rowInd, colInd):
        sheet = self.xls.sheet_by_name(sheetName)
        data = sheet.cell_type(rowInd, colInd)

        if (data == xlrd.XL_CELL_EMPTY):
            return True
        else:
            return False