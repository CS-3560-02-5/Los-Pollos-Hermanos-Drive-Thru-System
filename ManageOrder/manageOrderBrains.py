from manageOrder import *
import sys



class manageOrder(Ui_MainWindow):
    def __init__(self, window):
        self.setupUi(window)
        self.backButton.clicked.connect(self.clickBack)
        self.manageButton.clicked.connect(self.clickManage)
        
        order1 = 'Order 1'
        order2 = "order 2"

        
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


    def clickBack(self):
        self.close()

    def clickManage(self):
        print("Manage test")

    def clickList(self):
        print("Test List")


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = manageOrder(MainWindow)
MainWindow.show()
app.exec_()