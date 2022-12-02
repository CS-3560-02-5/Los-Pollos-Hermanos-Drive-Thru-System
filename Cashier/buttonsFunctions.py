import sys
from PyQt5 import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt

sys.path.append("Cashier")
from welcomeScreen import *
from selectingItems import *
from finishOrder import *

class buttonsFunctions(Ui_welcomeScreen):

    def __init__(self, window):
        self.setupUi(window)

        self.createOrderBtn.clicked.connect(self.switchToSelectingItems)

    def switchToSelectingItems(self):
        self.selectingItemsWindow = QtWidgets.QMainWindow()
        self.ui = Ui_selectingItems()
        self.ui.setupUi(self.selectingItemsWindow)
        self.selectingItemsWindow.show()



app = QtWidgets.QApplication(sys.argv)

WelcomeScreenWindow = QtWidgets.QMainWindow()
ui = buttonsFunctions(WelcomeScreenWindow)
WelcomeScreenWindow.show()
app.exec_()