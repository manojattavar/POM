import openpyxl

path = "C:/Users/029693744/Desktop/Employee Feedback/2022/1H feedback/Manoj A Kumar1-1H_feedback.xlsx"

wb = openpyxl.load_workbook(path)
sheet = wb.active
print(sheet.cell(2,1).value)
