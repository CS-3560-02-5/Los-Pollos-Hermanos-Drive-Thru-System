import MenuItem
import OrderItem
import Order
import data_bridge
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



class collector(HasTraits):
    def __init__(self):
        self.bridge = data_bridge.bridge("sql.json")
        # Rebuild all currently active orders
        self.orders = []
        for index, order in self.bridge.get_active_orders().sort_values(by=["queue_num"]).iterrows():
            self.orders.append(Order.Order(**order))

        # Rebuild all items attatched to the active orders
        self.log = {}
        for order in self.orders:
            self.log[order.order_id] = []
            for index, item in self.bridge.get_order_items(order).iterrows():
                self.log[order.order_id].append(OrderItem.OrderItem(**item))
        # Rebuild all menu items
        self.menu_items = []
        for index, item in self.bridge.get_menu_items().iterrows():
            self.menu_items.append(MenuItem.MenuItem(**item))

    @observe("menu_items")
    def update_menu_items(self, event):
        print("Menu items changed")
        pass
    
    @observe("orders")
    def update_orders(self, event):
        print("Orders changed")
        pass

    @observe("log")
    def update_order_items(self, event):
        print("Order items changed")
        pass


mass = collector()
mass.orders[1].complete()
print(mass.orders[1].__dict__)



app = QtWidgets.QApplication(sys.argv)
manager_win = QtWidgets.QMainWindow()
managerAttatched.managerAttatched(mass.menu_items, manager_win)
manage_order = QtWidgets.QMainWindow()
manageOrderBrains.manageOrder(mass, manage_order)
app.exec()