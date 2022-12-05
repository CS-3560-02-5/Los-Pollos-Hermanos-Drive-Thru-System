import sys
from PyQt5 import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt

from welcomeScreen import *
from selectingItemsAttached import *
from manageOrderAttached import *
from finishOrder import *

class welcomeScreenAttatched(Ui_welcomeScreen, QMainWindow):

    def __init__(self, mass, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.mass = mass
        self.createOrderBtn.clicked.connect(self.switchToSelectingItems)
        self.show()
        self.manageOrderBtn.clicked.connect(self.switchToManagerOrder)

    def switchToSelectingItems(self):
        self.selectingItemsWindow = QtWidgets.QMainWindow()
        self.selectingItemsUi = selectingItemsAttatched(self.mass, self.selectingItemsWindow)
        self.selectingItemsUi.show()
    
    def switchToManagerOrder(self):
        self.manageOrderWindow = QtWidgets.QMainWindow()
        self.manageOrderUi = manageOrderAttached(self.mass, self.manageOrderWindow)
        self.manageOrderUi.show()
