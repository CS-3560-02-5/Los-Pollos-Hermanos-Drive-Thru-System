from manageOrder import *
import sys
from PyQt5 import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
import manageOrderListGUI
import manageOrderListGUIAttached



class manageOrder(Ui_MainWindow, QMainWindow):
    def __init__(self, mass, parent=None):
        super().__init__(parent)
        self.setupUi(self)


        self.mass = mass
        self.setupDisplay(mass.orders)
        self.setupButtons()
        self.show()
        #button clickability


    def setupDisplay(self, orders):
        self.ordersList.addItems([x.customer_name for x in orders])
    def setupButtons(self):
        self.backButton.clicked.connect(lambda:self.close())
        self.manageButton.clicked.connect(self.clickManage)
    #this literally crashes the program but it closes it :)
    def clickBack(self):
        print("back test")
        self.ordersList.addItem("Russel Rickards")
        ''' app = QtGui.QGuiApplication(sys.argv)
        myapp = manageOrder()
        myapp.show()
        ret = app.exec()
        sys.exit(ret)'''
    
    def clickManage(self):
        self.manageOrderItems = QtWidgets.QMainWindow()
        self.ui = manageOrderListGUIAttached.Ui_MainWindow()
        self.ui.setupUi(self.manageOrderItems)
        manageOrderListGUIAttached.Ui_MainWindow(self.ordersList.currentItem().text()  , self.mass)
        self.manageOrderItems.show()
        
        

        
