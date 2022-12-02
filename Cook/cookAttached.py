from cookGUI import *
import sys


class cookGUIAttached(Ui_cookGUI):
    #constructor
    def __init__(self, window):
        self.setupUi(window)

        self.doneButton1.clicked.connect(self.updateOrderSlot1)
        self.doneButton2.clicked.connect(self.updateOrderSlot2)
        self.doneButton3.clicked.connect(self.updateOrderSlot3)
        self.doneButton4.clicked.connect(self.updateOrderSlot4)

    def updateOrderSlot1(self):
        test1 = 1
        test2 = "Walter's Nuggies"
        test3 = 14
        test4 = "medium rare"

        orderlength = 3
        orderStr = ""
        for item in range(orderlength):
                quantity = str(test3)
                name = str(test2)
                note = str(test4)
                orderStr += (quantity + "  " + name + "\n" + note + "\n\n")

        self.orderNum1.setText(str(test1))
        self.textArea1.setText(orderStr)
        print(orderStr)

    def updateOrderSlot2(self):
        test1 = 2
        test2 = "glizzy"
        test3 = 420
        test4 = "extra small"

        orderlength = 3
        orderStr = ""
        for item in range(orderlength):
                quantity = str(test3)
                name = str(test2)
                note = str(test4)
                orderStr += (quantity + "  " + name + "\n" + note + "\n\n")

        self.orderNum2.setText(str(test1))
        self.textArea2.setText(orderStr)
        print(orderStr)

    def updateOrderSlot3(self):
        test1 = 3
        test2 = "dirt water"
        test3 = 2
        test4 = "extra dirty"

        orderlength = 3
        orderStr = ""
        for item in range(orderlength):
                quantity = str(test3)
                name = str(test2)
                note = str(test4)
                orderStr += (quantity + "  " + name + "\n" + note + "\n\n")

        self.orderNum3.setText(str(test1))
        self.textArea3.setText(orderStr)
        print(orderStr)

    def updateOrderSlot4(self):
        test1 = 4
        test2 = "poop"
        test3 = 14
        test4 = "ur mom"

        orderlength = 3
        orderStr = ""
        for item in range(orderlength):
                quantity = str(test3)
                name = str(test2)
                note = str(test4)
                orderStr += (quantity + "  " + name + "\n" + note + "\n\n")

        self.orderNum4.setText(str(test1))
        self.textArea4.setText(orderStr)
        print(orderStr)

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = cookGUIAttached(MainWindow)
MainWindow.show()
app.exec_()

