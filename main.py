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
import managerGUI
import managerAttatched


####### Initial setup of running environment


mass = data_bridge.bridge("sql.json")

app = QtWidgets.QApplication(sys.argv)
#manager_win = QtWidgets.QMainWindow()
#manager_ui = managerAttatched.managerAttatched(mass, manager_win)
manageOrder = QtWidgets.QMainWindow()
manage_ui = manageOrderAttached.manageOrderAttached(mass, manageOrder)
app.exec_()
