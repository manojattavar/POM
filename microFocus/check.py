import xlrd



class email:

    def __init__(self, xlspath):
        self.xlspath = xlspath
        self.xls = xlrd.open_workbook(xlspath)

    def checkEmail(self):
        sheet = self.xls.sheet_by_name("Sheet1")
        rows = sheet.nrows
        cols = sheet.ncols

        dataStartIndex = 1





email("C:\\Users\\029693744\\PycharmProjects\\microFocus\\email.xls").checkEmail()