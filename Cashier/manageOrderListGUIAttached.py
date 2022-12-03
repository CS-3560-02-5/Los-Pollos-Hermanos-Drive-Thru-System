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
        self.accept_but.clicked.connect(self.clickAccept)
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
        #self.menuItems = mass.menu_items
        #self.orderItems = mass.log[self.currentOrderID]
        # self.orderList_ListWidget
        self.orderList_TableWidget.setColumnWidth(0,100)
        self.orderList_TableWidget.setColumnWidth(1,75)
        self.orderList_TableWidget.setColumnWidth(2,200)
        self.increment_spinBox.valueChanged.connect(self.spinSelected)
        self.orderList_TableWidget.cellClicked.connect(self.cellClickPosition)
'''
        for item in self.orderItems:
            name = next(i.item_name for i in self.menuItems if i.item_id == item.item_id)
            nameList.append(name)
            print("name", str(name))
            quantity = next(j.quantity for j in self.orderItems if j.quantity == item.quantity)
            quantList.append(quantity)
            print("quantity", str(quantity))
            notes = next(k.notes for k in self.orderItems if k.notes == item.notes)
            notesList.append(notes)
            print("notes", str(notes))
        
        self.orderList_TableWidget.setRowCount(len(nameList))
        for num in range(len(nameList)):
            self.orderList_TableWidget.setItem(num, 0, QtWidgets.QTableWidgetItem(nameList[num]))
            self.orderList_TableWidget.setItem(num, 1, QtWidgets.QTableWidgetItem(str(quantList[num])))
            self.orderList_TableWidget.setItem(num, 2, QtWidgets.QTableWidgetItem(notesList[num]))
'''
        self.show()
        
    #allows the editing of order    
    def clickAccept(self):
        nameList_Complete = []
        quantList_Complete = []
        notesList_Complete = []
        print("accept works")
        numRows = self.orderList_TableWidget.rowCount()
        for row in range(numRows):
            nameList_Complete.append(self.orderList_TableWidget.item(row, 0).text())
            quantList_Complete.append(self.orderList_TableWidget.item(row, 1).text())
            notesList_Complete.append(self.orderList_TableWidget.item(row, 2).text())
        

    
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
        if self.globalCol == 1:
            self.orderList_TableWidget.setItem(self.globalRow, self.globalCol, QtWidgets.QTableWidgetItem(str(self.increment_spinBox.value())))
    
    
#runs the application
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = manageOrderListGUIAttached(MainWindow)
    MainWindow.show()
    app.exec_()