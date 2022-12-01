from manageOrder import *
import sys
from PyQt5 import *


class manageOrder(Ui_MainWindow):
    def __init__(self, window):
        self.setupUi(window)
        self.backButton.clicked.connect(self.clickBack)
        self.manageButton.clicked.connect(self.clickManage)
        

    def clickBack(self):
        print("back test")

    def clickManage(self):
        print("Manage test")

    def clickList(self):
        print("Test List")
        
    def getOrder(self):
       self.ordersList.clicked.connect(self.clickList)

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = manageOrder(MainWindow)
MainWindow.show()
app.exec_()