from manageOrder import *
import sys
from PyQt5 import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
import manageOrderListGUI
import manageOrderListGUIAttached
from manageOrderListGUIAttached import *



class manageOrder(Ui_MainWindow, QMainWindow):
    def __init__(self, mass, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.mass = mass
        print(self.ordersList)
        self.setupDisplay(mass.orders)
        self.setupButtons()
       
        self.manageOrderItems_win = QtWidgets.QMainWindow()
        self.josh = manageOrderListGUIAttached.manageOrderListGUIAttached(self.mass, self.manageOrderItems_win)
        self.show()
        #button clickability


    def setupDisplay(self, orders):
        self.ordersList.addItems([x.customer_name for x in orders])
    def setupButtons(self):
        self.backButton.clicked.connect(lambda:self.close())
        self.manageButton.clicked.connect(self.clickManage)
    
    def clickManage(self):
        orderName = self.ordersList.currentItem().text()

        for order in self.mass.orders:
            orderID = next(i.order_id for i in self.mass.orders if i.customer_name == orderName)
        self.josh.currentOrderID = orderID
        print(orderID)
        for item in self.mass.log[self.currentOrderID]:
            name = next(i.item_name for i in self.mass.menuItems if i.item_id == item.item_id)
            self.josh.nameList.append(name)
            print("name", str(name))
            quantity = item.quanity
            self.josh.quantList.append(quantity)
            print("quantity", str(quantity))
            # self.orderList_TableWidget.setItem(n, 1, QtWidgets.QTableWidgetItem(str(quantity)))
            notes = item.notes
            self.josh.notesList.append(notes)
            print("notes", str(notes))
        self.orderList_TableWidget.setRowCount(len(self.josh.nameList))
        for num in range(len(self.josh.nameList)):
            self.orderList_TableWidget.setItem(num, 0, QtWidgets.QTableWidgetItem(self.josh.nameList[num]))
            self.orderList_TableWidget.setItem(num, 1, QtWidgets.QTableWidgetItem(str(self.josh.quantList[num])))
            self.orderList_TableWidget.setItem(num, 2, QtWidgets.QTableWidgetItem(self.josh.notesList[num]))

        self.manageOrderItems_win.show()
        
        

        
