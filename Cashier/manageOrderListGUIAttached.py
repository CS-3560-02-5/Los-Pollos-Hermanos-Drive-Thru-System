from manageOrderListGUI import *
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5.uic import loadUi
import sys

class manageOrderListGUIAttached(Ui_MainWindow, QMainWindow):
    #constructor
    def __init__(self, orderItems, menuItems, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        #calls clickEdit function
        self.editOrder_but.clicked.connect(self.clickEdit)
        #calls clickVoid function
        self.voidOrder_but.clicked.connect(self.clickVoid)
        #calls clickBack function
        self.back_but.clicked.connect(self.clickBack)
        #sets the order number label text
        self.manageOrderList_label.setText("Order #Bar")
        #Order list widget
        self.menuItems = menuItems
        self.orderItems = orderItems
        #self.orderList_ListWidget
        for item in orderItems:
            name = next(i.item_name for i in self.menuItems if i.item_id == item.item_id)
            self.orderList_ListWidget.addItem(name)
        self.show()
        
    #allows the editing of order    
    def clickEdit(self):
        print("edit works")
    
    #deletes order from db
    def clickVoid(self):
        print("void works")
        
    def clickBack(self):
        print("back works")
    
#runs the application
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = manageOrderListGUIAttached(MainWindow)
    MainWindow.show()
    app.exec_()