from manageOrderList import *
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5.uic import loadUi
import sys
class manageOrderListAttached(Ui_MainWindow, QMainWindow):
    #constructor
    def __init__(self, mass, parent = None):  
        self.currentOrderID = ""
        self.custName_var = ""
        super().__init__(parent)
        self.setupUi(self)
        self.mass = mass
        #initializing variables
        self.globalRow = 0
        self.globalCol = 0
        # self.orderList_TableWidget
        self.orderList_TableWidget.setColumnWidth(0,100)
        self.orderList_TableWidget.setColumnWidth(1,75)
        self.orderList_TableWidget.setColumnWidth(2,200)
        #calls clickEdit function
        self.accept_but.clicked.connect(self.clickAccept)
        #calls clickVoid function
        self.void_but.clicked.connect(self.clickVoid)
        #calls clickBack function
        self.back_but.clicked.connect(self.clickBack)
        #calls spinSelected if increment box changes
        self.increment_spinBox.valueChanged.connect(self.spinSelected)
        #gets position of current cell clicked
        self.orderList_TableWidget.cellClicked.connect(self.cellClickPosition)
        
    #allows the editing of order    
    def clickAccept(self):
        nameList_Complete = []
        quantList_Complete = []
        notesList_Complete = []
        menuIDList_Complete = []
        numRows = self.orderList_TableWidget.rowCount()
        
        #pulls customer name from custName_LineEdit (cuts off suffix)
        custName_Complete = self.custName_LineEdit.text()[:-9]
        print("custName_Complete:", custName_Complete)
        
        #adds all the edited attributes to respective lists
        for row in range(numRows):
            nameList_Complete.append(self.orderList_TableWidget.item(row, 0).text())
            quantList_Complete.append(self.orderList_TableWidget.item(row, 1).text())
            notesList_Complete.append(self.orderList_TableWidget.item(row, 2).text())
        print("nameList_Complete:", nameList_Complete)
        print("quantList_Complete:", quantList_Complete)
        print("notesList_Complete:", notesList_Complete)
            
        #changes nameList into menuID's in menuIDList_Complete
        for item in nameList_Complete:
            menuID = next(i.item_id for i in self.mass.menu_items if i.item_name == item)
            menuIDList_Complete.append(menuID)
            print("menuIDList_Complete:", menuIDList_Complete)
        
    #deletes order from db
    def clickVoid(self):
        self.orderList_TableWidget.removeRow(self.globalRow)
        print("void works")
    
    #goes back to manageOrder    
    def clickBack(self):
        print("back works")
        self.hide()
    
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
    ui = manageOrderListAttached(MainWindow)
    MainWindow.show()
    app.exec_()