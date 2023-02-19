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

    def get_column(self, header):
        header_cell = self.worksheet.find(header)
        target_column = header_cell.col
        column_list = self.worksheet.col_values(target_column)
        column_values = column_list[1:]
        return column_values

    def get_categories(self):
        list_of_worksheets = self.spreadsheet.worksheets()
        self.categories = [name.title for name in list_of_worksheets]
        print(self.categories)
        return self.categories