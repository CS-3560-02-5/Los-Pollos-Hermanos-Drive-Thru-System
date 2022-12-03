from manageOrderListGUI import *
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5.uic import loadUi
import sys

class manageOrderListGUIAttached(Ui_MainWindow, QMainWindow):
    #constructor
    def __init__(self, mass, parent = None):
        
        self.currentOrderID = 0
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
        #initializing variables
        self.globalRow = 0
        self.globalCol = 0
        n = 0
        nameList = []
        quantList = []
        notesList = []
        # self.orderList_ListWidget
        self.orderList_TableWidget.setColumnWidth(0,100)
        self.orderList_TableWidget.setColumnWidth(1,75)
        self.orderList_TableWidget.setColumnWidth(2,200)

        # for x in range(10):
        #     self.orderList_TableWidget.setItem(x, 0, QtWidgets.QTableWidgetItem("mack"))
        #     self.orderList_TableWidget.setItem(x, 1, QtWidgets.QTableWidgetItem("3"))
        # for x in range(5):
        #     self.orderList_TableWidget.setItem(x, 0, QtWidgets.QTableWidgetItem("wang bang"))
        #     self.orderList_TableWidget.setItem(x, 1, QtWidgets.QTableWidgetItem("3"))
        self.increment_spinBox.valueChanged.connect(self.spinSelected)
        self.orderList_TableWidget.cellClicked.connect(self.cellClickPosition)
        menuItems = self.mass.menuItems
        orderItems = self.mass.orderItems
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
    MainWindow.show()
    app.exec_()