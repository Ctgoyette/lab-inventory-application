import os
import gspread

class Sheet:
    def __init__(self, sheet, credentials_file):
        self.sheet = sheet
        self.credentials_file = os.path.expanduser("~\Documents\Programming\\") + credentials_file
        self.gc = gspread.service_account(filename=self.credentials_file)
        self.spreadsheet = self.gc.open(self.sheet)
        self.worksheet = self.spreadsheet.sheet1
        self.categories = []

    def select_worksheet(self, worksheet):
        self.worksheet = self.spreadsheet.worksheet(worksheet)

    def get_row_num(self, value):
        try:
            target_cell = self.worksheet.find(value)
            target_row = target_cell.row
        except:
            target_row = None

        return target_row

    def get_col_num(self, value):
        try:
            target_cell = self.worksheet.find(value)
            target_column = target_cell.col
        except:
            target_column = None

        return target_column

    def get_col_values(self, header):
        try:
            target_column = self.get_col_num(header)
            column_list = self.worksheet.col_values(target_column)
            if len(column_list) > 1:
                column_values = column_list[1:]
            else:
                column_values = None
        except:
            column_values = None
        
        return column_values


    def get_categories(self):
        list_of_worksheets = self.spreadsheet.worksheets()
        self.categories = [name.title for name in list_of_worksheets]
        return self.categories

    def get_cell_val(self, row, col):
        if row is not None and col is not None:
            return self.worksheet.cell(row, col).value
        else:
            return None