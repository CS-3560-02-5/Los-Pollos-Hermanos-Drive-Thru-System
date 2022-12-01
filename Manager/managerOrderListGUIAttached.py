from managerOrderListGUI import *
import sys

class managerOrderListGUIAttached(Ui_MainWindow):
    #constructor
    def __init__(self, window):
        self.setupUi(window)
        #calls clickEdit function
        self.editOrder_but.clicked.connect(self.clickEdit)
        #calls clickVoid function
        self.voidOrder_but.clicked.connect(self.clickVoid)
        self.manageOrderList_label.setText("Order #Bar")
        
    #allows the editing of order    
    def clickEdit(self):
        print("edit works")
    
    #deletes order from db
    def clickVoid(self):
        print("void works")
    
#runs the application
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = managerOrderListGUIAttached(MainWindow)
MainWindow.show()
app.exec_()