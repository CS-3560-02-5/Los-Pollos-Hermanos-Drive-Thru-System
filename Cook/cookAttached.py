from cookGUI import *
import sys
from PyQt5 import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt


class cookAttached(Ui_cookGUI, QMainWindow):
    #making constructor
    def __init__(self, mass, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.mass = mass
        self.submittedOrders = [i for i in self.mass.orders if i.order_status == 's']
        self.updateOrderSlots()
        self.show()



    def clickDone(self):
        pass
        



    def setupDisplay(self):
        #set up buttons to reset each slot everytime it is presses
        self.doneButton1.clicked.connect(self.updateOrderSlot1)     #update slot 1
        self.doneButton2.clicked.connect(self.updateOrderSlot2)     #update slot 2
        self.doneButton3.clicked.connect(self.updateOrderSlot3)     #update slot 3
        self.doneButton4.clicked.connect(self.updateOrderSlot4)     #update slot 4


    #edit slot 1
    def updateOrderSlots(self):
        try:
            self.orderNum1.setText(self.submittedOrders[3].queue_number)
            for item in self.mass[self.submittedOrders[3].order_id]:
                self.listWidget.addItem("x" + item.quantity + "  " + next(i.item_name for i in self.mass.menu_items if i.item_id == item.item_id) + "\n" +item.notes)
        except:
            print("No orders in queue 4")
        try:
            self.orderNum2.setText(self.submittedOrders[2].queue_number)
            for item in self.mass[self.submittedOrders[2].order_id]:
                self.listWidget_2.addItem("x" + item.quantity + "  " + next(i.item_name for i in self.mass.menu_items if i.item_id == item.item_id) + "\n" +item.notes)
        except:
            print("No orders in queue 3")

        try:
            self.orderNum3.setText(self.submittedOrders[1].queue_number)
            for item in self.mass[self.submittedOrders[1].order_id]:
                self.listWidget_3.addItem("x" + item.quantity + "  " + next(i.item_name for i in self.mass.menu_items if i.item_id == item.item_id) + "\n" +item.notes)
        except:
            print("No orders in queue 2")
        try:
            self.orderNum4.setText(self.submittedOrders[0].queue_number)
            for item in self.mass[self.submittedOrders[0].order_id]:
                self.listWidget_4.addItem("x" + item.quantity + "  " + next(i.item_name for i in self.mass.menu_items if i.item_id == item.item_id) + "\n" +item.notes)
        except:
            print("No orders in queue 1")


    def updateOrderSlot1(self, order):
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

'''
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = cookAttached(MainWindow)
    app.exec_()
    '''