import sys
from PyQt5 import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt

from welcomeScreen import *
from selectingItems import *
from finishOrder import *

class welcomeScreenAttatched(Ui_welcomeScreen, QMainWindow):

    def __init__(self, mass, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.mass = mass
        self.createOrderBtn.clicked.connect(self.switchToSelectingItems)
        self.manageOrderBtn.clicked.connect(self.trythis)
        self.show()

    def switchToSelectingItems(self):
        self.selectingItemsWindow = QtWidgets.QMainWindow()
        self.ui = Ui_selectingItems()
        self.ui.setupUi(self.selectingItemsWindow)
        self.selectingItemsWindow.show()

    def trythis(self):
        self.selectingItemsWindow.hide()