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
import welcomeScreenAttatched
from traits.api import *


####### Initial setup of running environment


mass = data_bridge.bridge("sql.json")

app = QtWidgets.QApplication(sys.argv)
welcome_win = QtWidgets.QMainWindow()
welcomeUI = welcomeScreenAttatched.welcomeScreenAttatched(mass, welcome_win)
app.exec_()
