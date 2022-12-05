import sys
from PyQt5 import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt

from welcomeScreen import *
from selectingItems import *
from finishOrder import *

class buttonsFunctions(Ui_welcomeScreen):

    def __init__(self, window):
        self.setupUi(window)

        self.createOrderBtn.clicked.connect(self.switchToSelectingItems)
        self.manageOrderBtn.clicked.connect(self.trythis)

    def switchToSelectingItems(self):
        self.selectingItemsWindow = QtWidgets.QMainWindow()
        self.ui = Ui_selectingItems()
        self.ui.setupUi(self.selectingItemsWindow)
        self.selectingItemsWindow.show()

    def trythis(self):
        self.selectingItemsWindow.hide()



app = QtWidgets.QApplication(sys.argv)

WelcomeScreenWindow = QtWidgets.QMainWindow()
ui = buttonsFunctions(WelcomeScreenWindow)
WelcomeScreenWindow.show()
app.exec_()