from createOrder import Ui_Dialog
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

class createOrderAttached(Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show
        
if __name__ == "__main__":
    UI = createOrderAttached()
    import sys
    app = QtWidgets.QApplication(sys.argv)
    manager_MainWindow = createOrderAttached()
    sys.exit(app.exec_())