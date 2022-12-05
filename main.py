import MenuItem
import OrderItem
import data_bridge
import Order
import sys
from PyQt5 import QtCore, QtWidgets 
sys.path.append("Manager")
sys.path.append("Cook")
sys.path.append("Cashier")
import manageOrderAttached
import managerAttatched


####### Initial setup of running environment


mass = data_bridge.bridge("sql.json")

app = QtWidgets.QApplication(sys.argv)
manage_win = QtWidgets.QMainWindow()
manage_ui = manageOrderAttached.manageOrderAttached(mass, manage_win)
app.exec_()

# app = QtWidgets.QApplication(sys.argv)
# manage_win = QtWidgets.QMainWindow()
# manage_ui = managerAttatched.managerAttatched(mass, manage_win)
# app.exec_()
