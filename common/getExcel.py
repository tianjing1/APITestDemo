
from xlrd import open_workbook


class GetExcel:
    def get_xls(self, xls_name, sheet_name):
        """
        get interface data from xls file
        :return:
        """
        cls = []
        # get xls file's path
        # xlsPath = os.path.join("testFile", 'case', xls_name)
        # open xls file
        file = open_workbook(xls_name)
        # get sheet by name
        sheet = file.sheet_by_name(sheet_name)
        # get one sheet's rows
        nrows = sheet.nrows
        for i in range(nrows):
            if sheet.row_values(i)[0] != u'case_name':
                cls.append(sheet.row_values(i))
        return cls