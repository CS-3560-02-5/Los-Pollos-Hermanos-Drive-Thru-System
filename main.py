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
from traits.api import *


####### Initial setup of running environment


mass = data_bridge.bridge("sql.json")

app = QtWidgets.QApplication(sys.argv)
manage_order = QtWidgets.QMainWindow()
