from manageOrder import *
import sys
from PyQt5 import *



class manageOrder(Ui_MainWindow):
    def __init__(self, window):
        #create ui
        self.setupUi(window)
        #button clickability
        self.backButton.clicked.connect(self.clickBack)
        self.manageButton.clicked.connect(self.clickManage)
        
        order1 = 'Order 1'
        order2 = "order 2"

        #fills the list with dummy data
        self.ordersList.addItem(order1)
        self.ordersList.addItem(order2)
        self.ordersList.addItem(order1)
        self.ordersList.addItem(order2)
        self.ordersList.addItem(order1)
        self.ordersList.addItem(order2)
        self.ordersList.addItem(order1)
        self.ordersList.addItem(order2)
        self.ordersList.addItem(order1)
        self.ordersList.addItem(order2)
        self.ordersList.addItem(order1)
        self.ordersList.addItem(order2)
        self.ordersList.addItem(order1)
        self.ordersList.addItem(order2)

    #this literally crashes the program but it closes it :)
    def clickBack(self):
        self.close()

    def clickManage(self):
        print("Manage test")

    def clickList(self):
        print("Test List")

#creates the window
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = manageOrder(MainWindow)
MainWindow.show()
app.exec_()