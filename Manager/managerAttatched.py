from managerGUI import Ui_manager_QWidget
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import sys

class managerAttatched(Ui_manager_QWidget, QMainWindow):
    def __init__(self, df, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.load(df)
        self.show()

    def load(self, df):
        for index, order in df.iterrows():
            print(str(index) + ": " + order.customer_name)


    def connectSignalsSlots(self):
        self.addItem_pushButton.clicked.connect(self.addMenuItem_GUI)
        self.editItem_pushButton.clicked.connect(self.editMenuItem_GUI)
        self.removeItem_pushButton.clicked.connect(self.removeMenuItem_GUI)
        
    def addMenuItem_GUI(self):
        pass
    def removeMenuItem_GUI(self):
        print("works")

    def editMenuItem_GUI(self):
        print("works")
     
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    manager_win = QtWidgets.QMainWindow()
    managerAttatched(manager_win)
    sys.exit(app.exec_())