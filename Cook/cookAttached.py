from cookGUI import *

import sys
from PyQt5 import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi

class cookAttached(Ui_cookGUI, QMainWindow):
    #making constructor

    def __init__(self, parent = None, menuItems = None, quantity = None, notes = None):
        super().__init__(parent)
        self.setupUi(self)
        self.menu_items = menuItems
        self.quantity = quantity
        self.notes = notes

        #set up buttons to reset each slot everytime it is presses
        self.doneButton1.clicked.connect(self.updateOrderSlot1)     #update slot 1
        self.doneButton2.clicked.connect(self.updateOrderSlot2)     #update slot 2
        self.doneButton3.clicked.connect(self.updateOrderSlot3)     #update slot 3
        self.doneButton4.clicked.connect(self.updateOrderSlot4)     #update slot 4

        self.show()

    #edit slot 1
    def updateOrderSlot1(self):
        #find all active orders in db and add them to active_order

        #initializing test array to pull data from
        orderArray = [1,"walter's Nuggies",14,"medium rare"]

        orderlength = 3
        orderStr = ""

        #setting data from array to one string 
        for item in range(orderlength):
                quantity = str(orderArray[2])
                name = str(orderArray[1])
                note = str(orderArray[3])
                orderStr += (quantity + "  " + name + "\n" + note + "\n\n")

        self.orderNum1.setText(str(orderArray[0]))  #show order number on GUI
        self.textArea1.setText(orderStr)            #show completed order string on gui

        #make order as completed after chef clicks done


    #edit slot 2
    def updateOrderSlot2(self):
        #initializing test array to pull data from
        orderArray = [1,"walter's Nuggies",14,"medium rare"]

        orderlength = 3
        orderStr = ""
        for item in range(orderlength):
                quantity = str(orderArray[2])
                name = str(orderArray[1])
                note = str(orderArray[3])
                orderStr += (quantity + "  " + name + "\n" + note + "\n\n")

        self.orderNum2.setText(str(orderArray[0]))
        self.textArea2.setText(orderStr)

    #edit slot 3
    def updateOrderSlot3(self):
        #initializing test array to pull data from
        orderArray = [1,"walter's Nuggies",14,"medium rare"]

        orderlength = 3
        orderStr = ""
        for item in range(orderlength):
                quantity = str(orderArray[2])
                name = str(orderArray[1])
                note = str(orderArray[3])
                orderStr += (quantity + "  " + name + "\n" + note + "\n\n")

        self.orderNum3.setText(str(orderArray[0]))
        self.textArea3.setText(orderStr)

    #edit slot 4
    def updateOrderSlot4(self):
        #initializing test array to pull data from
        orderArray = [1,"walter's Nuggies",14,"medium rare"]
        orderlength = 3
        orderStr = ""
        for item in range(orderlength):
                quantity = str(orderArray[2])
                name = str(orderArray[1])
                note = str(orderArray[3])
                orderStr += (quantity + "  " + name + "\n" + note + "\n\n")

        self.orderNum4.setText(str(orderArray[0]))
        self.textArea4.setText(orderStr)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = cookAttached(MainWindow)
    app.exec_()

