from raw_gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import *
from sheets_integration import Sheet
from functools import partial
import sys

class app(Ui_MainWindow):
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.main_window_setup()

        self.contents_file = Sheet('Lab Contents', 'nurobotics-lab-inventory-bot-credentials.json')
        self.setup_categories_list()
    
    def main_window_setup(self):
        '''
        Creates the main window
        '''
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.MainWindow.setWindowTitle('Inventory System')

    def setup_categories_list(self):
        for category in self.contents_file.get_categories():
            self.categories_list.addItem(category)

        self.categories_list.itemSelectionChanged.connect(self.update_item_list)

    def update_item_list(self):
        self.item_list.clear()
        self.contents_file.select_worksheet(self.categories_list.currentItem().text())
        for item in self.contents_file.get_column('Item'):
            self.item_list.addItem(item)
        


#########################################################
#Actually display stuff
#########################################################

ui = app()
# Shows the application window and automatically maximizes it
ui.MainWindow.showMaximized()
# Allows window to open before automatcally loading all songs and playlists in library (Windows) in case the library is very large
sys.exit(ui.app.exec_())