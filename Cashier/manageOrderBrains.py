from manageOrder import *
import sys
from PyQt5 import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
import manageOrderListGUI
import manageOrderListGUIAttached



class manageOrderClass(Ui_MainWindow, QMainWindow):
    def __init__(self, mass, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.mass = mass
        print(self.ordersList)
        self.setupDisplay(mass.orders)
        self.setupButtons()
        self.show()
        self.manageOrderItems_win = QtWidgets.QMainWindow()
        self.josh = manageOrderListGUIAttached.manageOrderListGUIAttached(self.mass, self.manageOrderItems_win)
        
        #button clickability


    def setupDisplay(self, orders):
        self.ordersList.addItems([x.customer_name for x in orders])
    def setupButtons(self):
        self.backButton.clicked.connect(lambda:self.close())
        self.manageButton.clicked.connect(self.clickManage)
    
    def clickManage(self):
        orderName = self.ordersList.currentItem().text()

        for order in self.mass.orders:
            orderID = next(i.order_id for i in self.mass.orders if i.customer_name == orderName)
        self.josh.currentOrderID = orderID
        print(orderID)
        self.manageOrderItems_win.show()
        
        

        
