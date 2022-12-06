import xlrd


class XLSReader:
    def __init__(self,path):
        self.path = path
        self.readXLS = xlrd.open_workbook(path)
        
    def getCellData(self, sheetname, rowIndex, colIndex):
        cell = self.readXLS.sheet_by_name(sheetname)
        return cell.cell_value(rowIndex, colIndex)
    
    def getCellDataByColName(self, sheetname, rowIndex,colName):
        sheetData = self.readXLS.sheet_by_name(sheetname)
        for cNum in range(0,sheetData.ncols):
            extractedColName = sheetData.cell_value(0,cNum)
            if(colName==extractedColName):
                cellData = sheetData.cell_value(rowIndex,cNum)
                if(cellData!=''):
                    return cellData
                else:
                    return ''
    
    def checkEmptyCell(self,sheetname, rowIndex, colIndex):
        sheetData = self.readXLS.sheet_by_name(sheetname)
        cellType = sheetData.cell_type(rowIndex, colIndex)
        if cellType==xlrd.XL_CELL_EMPTY:
            return True
        else:
            return False
        
    def rowCount(self,sheetname):
        sheetData = self.readXLS.sheet_by_name(sheetname)
        return sheetData.nrows
    
    def colCount(self,sheetname):
        sheetData = self.readXLS.sheet_by_name(sheetname)
        return sheetData.ncols
        
        