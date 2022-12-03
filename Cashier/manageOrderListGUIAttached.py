from manageOrderListGUI import *
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5.uic import loadUi
import sys

class manageOrderListGUIAttached(Ui_MainWindow, QMainWindow):
    #constructor
    def __init__(self, orderItems = None, menuItems = None, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        #calls clickEdit function
        self.edit_but.clicked.connect(self.clickEdit)
        #calls clickVoid function
        self.void_but.clicked.connect(self.clickVoid)
        #calls clickBack function
        self.back_but.clicked.connect(self.clickBack)
        #sets the order number label text
        self.manageOrderList_label.setText("Order #Bar")
        #ListWidget item
        self.item = QtWidgets.QTableWidgetItem("")
        self.globalRow = 0
        self.globalCol = 0
        #Order list widget
        # self.menuItems = menuItems
        # self.orderItems = orderItems
        
        # self.orderList_ListWidget
        self.orderList_TableWidget.setColumnWidth(0,340)
        self.orderList_TableWidget.setColumnWidth(1,50)
        n = 10
        self.orderList_TableWidget.setRowCount(n)
        for n in range(10):
            self.orderList_TableWidget.setItem(n, 0, QtWidgets.QTableWidgetItem("mack"))
            self.orderList_TableWidget.setItem(n, 1, QtWidgets.QTableWidgetItem("3"))
        for n in range(5):
            self.orderList_TableWidget.setItem(n, 0, QtWidgets.QTableWidgetItem("wang bang"))
            self.orderList_TableWidget.setItem(n, 1, QtWidgets.QTableWidgetItem("3"))
        self.increment_spinBox.valueChanged.connect(self.spinSelected)
        self.orderList_TableWidget.cellClicked.connect(self.cellClickPosition)
        # self.orderList_TableWidget.cellClicked.connect(self.editQuantity)
        #self.increment_spinBox.setValue(self.orderList_TableWidget.currentItem())
        # for item in orderItems:
        #     name = next(i.item_name for i in self.menuItems if i.item_id == item.item_id)
        #     self.orderList_ListWidget.addItem(name) 
        
        self.show()
        
    #allows the editing of order    
    def clickEdit(self):
        print("edit works")
    
    #deletes order from db
    def clickVoid(self):
        self.orderList_TableWidget.removeRow(self.globalRow)
        print("void works")
    
    #goes back to manageOrder    
    def clickBack(self):
        print("back works")
    
    #edits quantity of clicked cell

    def cellClickPosition(self, row, col):
        self.globalRow, self.globalCol = row, col
        
    
    #increments the quantity
    def spinSelected(self):
        if self.globalCol != 0:
            self.orderList_TableWidget.setItem(self.globalRow, self.globalCol, QtWidgets.QTableWidgetItem(str(self.increment_spinBox.value())))
    
    
#runs the application
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = manageOrderListGUIAttached(MainWindow)
    app.exec_()