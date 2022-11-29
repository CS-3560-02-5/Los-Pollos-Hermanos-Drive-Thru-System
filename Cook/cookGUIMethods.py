import cookGUI
from PyQt5 import QtCore, QtWidgets
import sys

# compile cookGUI.py file on cmd: pyuic5 -x cookGUI.ui -o cookGUI.py

class cookAttached(cookGUI.Ui_Dialog):
    def __init__(self, window):
        self.setupUi(window)
        

    # change frame 1 on cookGUI
    def changelabeltitle1(self):
        test1 = 1
        test2 = "Walter's Nuggies"
        test3 = 14
        test4 = "medium rare"

        orderlength = 10
        orderStr = ""
        for item in range(orderlength):
            quantity = str(test3)
            name = str(test2)
            note = str(test4)
            orderStr += (quantity + "  " + name + "\n" + note + "\n\n")

        self.labeltitle1.setText("Order : " + str(test1))
        self.label1.setText(orderStr)
        print(orderStr)

    # change frame 2 on cookGUI
    def changelabeltitle2(self):
        orderNum = 2
        menuItem = "Chick San"
        quantity = 1
        itemNotes = ""
        self.labeltitle2.setText("Order : " + str(orderNum))
        self.label2.setText(str(quantity) + ' : ' + menuItem + "\nnotes: " + itemNotes)

    # change frame 3 on cookGUI
    def changelabeltitle3(self):
        orderNum = 3
        menuItem = ""
        quantity = 1
        itemNotes = ""
        self.labeltitle3.setText("Order : " + str(orderNum))
        self.label3.setText(str(quantity) + ' : ' + menuItem + "\nnotes: " + itemNotes)

    # change frame 4 on cookGUI
    def changelabeltitle4(self):
        orderNum = 4
        menuItem = ""
        quantity = 1
        itemNotes = ""
        self.labeltitle4.setText("Order : " + str(orderNum))
        self.label4.setText(str(quantity) + ' : ' + menuItem + "\nnotes: " + itemNotes)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    cook_win = QtWidgets.QMainWindow()
    cookAttached(cook_win)
    sys.exit(app.exec_())