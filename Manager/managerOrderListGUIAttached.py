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
        #calls clickBack function
        self.back_but.clicked.connect(self.clickBack)
        #sets the order number label text
        self.manageOrderList_label.setText("Order #Bar")
        #Order list
        #self.orderList_View
        
    #allows the editing of order    
    def clickEdit(self):
        print("edit works")
    
    #deletes order from db
    def clickVoid(self):
        print("void works")
        
    def clickBack(self):
        print("back works")
    
#runs the application
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = managerOrderListGUIAttached(MainWindow)
MainWindow.show()
app.exec_()