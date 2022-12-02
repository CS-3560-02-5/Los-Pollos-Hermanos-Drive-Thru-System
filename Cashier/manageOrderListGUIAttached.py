from manageOrderListGUI import *
import sys

class manageOrderListGUIAttached(Ui_MainWindow):
    #constructor
    def __init__(self, orderItems, window):
        self.setupUi(window)
        #calls clickEdit function
        self.editOrder_but.clicked.connect(self.clickEdit)
        #calls clickVoid function
        self.voidOrder_but.clicked.connect(self.clickVoid)
        #calls clickBack function
        self.back_but.clicked.connect(self.clickBack)
        #sets the order number label text
        self.manageOrderList_label.setText("Order #Bar")
        #Order list widget
        #self.orderList_ListWidget
        
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
ui = manageOrderListGUIAttached(MainWindow)
MainWindow.show()
app.exec_()