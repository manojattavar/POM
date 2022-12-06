'''
Created on 05-Mar-2020
@author: Jaspreet
'''
from module09.ExcelFunctions import ReadWrite
sheetname='Jaspreet'
xls=ReadWrite("C:\\Users\\Jaspreet\\Desktop\\test.xlsx")
print(xls.readby_ColumnIndex(sheetname, 6, 3))
print(xls.readby_ColumnName(sheetname, 6, 'Course'))
print("Writing data in excel sheet")
xls.writeby_ColumIndex(sheetname, 6, 2, "Avneet")
xls.writeby_ColumnName(sheetname, 3, 'Names', 'Varsha')
print("")
print("Updates Done...Check ur excel file")
print("Total no. of rows : "+str(xls.getRowCount(sheetname)))
print("Total no. of columns : "+str(xls.getColumnCount(sheetname)))
print("")

for rowData in range(2,xls.getRowCount(sheetname)+1):
    print(xls.readby_ColumnName(sheetname, rowData, 'Names'))
    
print("")
for colData in range(1, xls.getColumnCount(sheetname)+1):
    print(xls.readby_ColumnIndex(sheetname, 3, colData))
    
for rowNum in range(2, xls.getRowCount(sheetname)+1):
    print("")
    for colNum in range(1, xls.getColumnCount(sheetname)+1):
        cellData= xls.readby_ColumnIndex(sheetname, rowNum, colNum)
        print(cellData)