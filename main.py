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
import managerAttached



####### Initial setup of running environment
mass = data_bridge.bridge()

app = QtWidgets.QApplication(sys.argv)
manager_win = QtWidgets.QMainWindow()
manager_ui = managerAttached.managerAttached(mass, manager_win)
manage_win = QtWidgets.QMainWindow()
manage_ui = manageOrderAttached.manageOrderAttached(mass, manage_win)
app.exec_()

# app = QtWidgets.QApplication(sys.argv)
# manage_win = QtWidgets.QMainWindow()
# manage_ui = managerAttatched.managerAttatched(mass, manage_win)
# app.exec_()
