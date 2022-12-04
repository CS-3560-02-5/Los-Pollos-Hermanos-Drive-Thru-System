import MenuItem
import OrderItem
import data_bridge
import Order
import sys
from PyQt5 import QtCore, QtWidgets 
sys.path.append("Manager")
sys.path.append("Cook")
sys.path.append("Cashier")
import manageOrderListGUI
import manageOrderListGUIAttached
import managerAttatched
import cookAttatched
import manageOrderBrains
from traits.api import *


####### Initial setup of running environment


mass = data_bridge.bridge("sql.json")



app = QtWidgets.QApplication(sys.argv)
manager_win = QtWidgets.QMainWindow()
managerAttatched.managerAttatched(mass.menu_items, manager_win)
manage_order = QtWidgets.QMainWindow()
manageOrderBrains.manageOrder(mass, manage_order)
app.exec()