import manageOrder
from PyQt5 import QtCore, QtWidgets
import sys

class manageOrderBrains(manageOrder.Ui_MainWindow):
    def _init_(self, window):
        self.setupUi(window) 
        self.pushButton1.clicked.connect(self.label1Change, "label1")
        window.show()

    def label1Change(self)
        self.label1.setText("This isn't a test")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    manageOrder
