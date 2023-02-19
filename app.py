import raw_gui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import *
import sys

class app(raw_gui.Ui_MainWindow):
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.main_window_setup()
    
    def main_window_setup(self):
        '''
        Creates the main window and removes all margins around the main window. Only runs during the initialization of a PlayerWindow object
        '''
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.MainWindow.setWindowTitle('Inventory System')



#########################################################
#Actually display stuff
#########################################################

ui = app()
# Shows the application window and automatically maximizes it
ui.MainWindow.showMaximized()
# Allows window to open before automatcally loading all songs and playlists in library (Windows) in case the library is very large
sys.exit(ui.app.exec_())