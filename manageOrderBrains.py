from manageOrder import *
import sys
from PyQt5 import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi



class manageOrder(Ui_MainWindow, QMainWindow):
    def __init__(self, orders, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.orders = orders
        self.setupDisplay(self.orders)
        self.setupButtons()
        self.show()
        #button clickability


    def setupDisplay(self, orders):
        self.ordersList.addItems([x.customer_name for x in orders])
    def setupButtons(self):
        self.backButton.clicked.connect(self.clickBack)
        self.manageButton.clicked.connect(self.clickManage)
    #this literally crashes the program but it closes it :)
    def clickBack(self):
        print("back test")
        self.ordersList.addItem("russel Rickards")

    def clickManage(self):
        print("Manage test")

        
