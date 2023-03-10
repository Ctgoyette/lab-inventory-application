from raw_gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import *
from database import Database
from functools import partial
import sys

class app(Ui_MainWindow):
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.main_window_setup()
        self.lab_database = Database('Lab Contents', 'nurobotics-lab-inventory-bot-credentials.json')
        self.setup_categories_list()
    
    def main_window_setup(self):
        '''
        Creates the main window
        '''
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.MainWindow.setWindowTitle('Inventory System')

    def setup_categories_list(self):
        for category in self.lab_database.categories.keys():
            self.categories_list.addItem(category)

        self.categories_list.itemSelectionChanged.connect(self.update_item_list)

    def update_item_list(self):
        self.item_list.clear()
        current_category = self.lab_database.categories[self.categories_list.currentItem().text()]
        for item in current_category.category_items.keys():
            self.item_list.addItem(item)
        
        self.item_list.itemSelectionChanged.connect(self.update_details_tab)
    
    def update_details_tab(self):
        current_category = self.lab_database.categories[self.categories_list.currentItem().text()]
        try:
            current_item = current_category.category_items[self.item_list.currentItem().text()]
            self.item_label.setText(current_item.name)
            self.brand_label.setText(current_item.brand)
            self.quantity_label.setText(current_category.quantity)
            self.location_label.setText(current_item.location)
            self.description_label.setText(current_item.description)
        except:
            return None


        


#########################################################
#Actually display stuff
#########################################################

ui = app()
# Shows the application window and automatically maximizes it
ui.MainWindow.showMaximized()
# Allows window to open before automatcally loading all songs and playlists in library (Windows) in case the library is very large
sys.exit(ui.app.exec_())