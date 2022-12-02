from manageOrder import *
import sys
from PyQt5 import *
import data_bridge
import Order



class manageOrder(Ui_MainWindow):
    def __init__(self, window):
        bridge = data_bridge.bridge("sql.json")
        #create ui
        self.setupUi(window)
        #button clickability
        self.backButton.clicked.connect(self.clickBack)
        self.manageButton.clicked.connect(self.clickManage)
        
        active_orders = []
        for index, order in bridge.get_active_orders().sort_values(by=["queue_num"]).iterrows():
            active_orders.append(Order.Order(**order))
        print([x.__dict__ for x in active_orders])
        
        order1 = "order1"
        #fills the list with dummy data
        self.ordersList.addItem(order1)

    #this literally crashes the program but it closes it :)
    def clickBack(self):
        print("back test")
        self.ordersList.addItem("russel Rickards")

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