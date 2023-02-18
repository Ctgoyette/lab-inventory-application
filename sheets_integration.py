import os
import gspread

class Sheet:
    def __init__(self, sheet, credentials_file):
        self.sheet = sheet
        self.credentials_file = os.path.expanduser("~\Documents\Programming\\") + credentials_file
        self.gc = gspread.service_account(filename=self.credentials_file)
        self.sh = self.gc.open(self.sheet)
        self.worksheet = self.sh.sheet1

    def select_worksheet(self, worksheet):
        self.worksheet = self.sh.worksheet(worksheet)

    def get_column(self, header):
        header_cell = self.worksheet.find(header)
        target_column = header_cell.col

        print(header_cell.row)
        print(header_cell.col)
        column_list = self.worksheet.col_values(target_column)
        column_values = column_list[1:]

        return column_values

new_sheet = Sheet('Lab Contents', 'nurobotics-lab-inventory-bot-credentials')