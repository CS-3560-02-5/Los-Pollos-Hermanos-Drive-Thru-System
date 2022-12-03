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
    
    def save(self):
        pass

class Event(HasTraits):
    def __init__(self):
        super().__init__()
        self.collector = collector()
        self.collector.on_trait_change(Event._anytrait_changed)

    def _anytrait_changed(obj, name, old, new):
        is_list = name.endswith('_items')
        if is_list:
            name = name[0:name.rindex('_items')]
        current_val = getattr(obj, name)
        if is_list:
            # new handles all the events(removed/changed/added to the list)
            if any(new.added):
                print("{} added to {} which is now {}".format(new.added, name, current_val))
            if any(new.removed):
                print("{} removed from {} which is now {}".format(new.removed, name, current_val))
        else:
            print('The {} trait changed from {} to {} '.format(name, old, (getattr(obj, name))))

mass = collector()

#This runs manageOrderListGUIAttached
app = QtWidgets.QApplication(sys.argv)
# manager_win = QtWidgets.QMainWindow()
# managerAttatched.managerAttatched(mass.menu_items, manager_win)
# manage_order = QtWidgets.QMainWindow()
# manageOrderBrains.manageOrder(mass, manage_order)
manageOrderList_win = QtWidgets.QMainWindow()
manageOrderListGUIAttached.manageOrderListGUIAttached(mass.log[mass.orders[0].order_id], mass.menu_items, manageOrderList_win)
app.exec_()
