from manageOrder import *
import sys

class manageOrder(Ui_MainWindow):
    def __init__(self, window):
        self.setupUi(window)


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = manageOrder(MainWindow)
MainWindow.show()
app.exec_()