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
from traits.api import *

############ Open all interfaces here


###################################
running = True

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

'''
#### TESTING
print([x.__dict__ for x in orders])
print([x.__dict__ for x in active_order_items])
print([(x.item_name + ": " + str(x.item_id)) for x in menu_items])
'''



# app = QtWidgets.QApplication(sys.argv)
# manager_win = QtWidgets.QMainWindow()
# managerAttatched.managerAttatched(mass.menu_items, manager_win)
# app.exec_()
# print([x.item_name for x in mass.menu_items])
app = QtWidgets.QApplication(sys.argv)
manageOrderList_win = QtWidgets.QMainWindow()
manageOrderListGUIAttached.manageOrderListGUIAttached(mass.log[mass.orders[0].order_id], mass.menu_items, manageOrderList_win)
app.exec_()
##### FIND A WAY TO SYNC THE ATTRTIBUTES TO THE DATABASE



'''
bridge.add_menu_item(9, "The Tester", "Purely to test the add function", 4.20, menu_items[0].image)        # create menu_items test
bridge.edit_menu_item(menu_items[8], "item_description", "This is the updated value!")                    # update menu_items test
bridge.remove_menu_item(menu_items[8])                                                                 # delete menu_items test
'''

'''
bridge.add_order_item(orders[1], menu_items[7], notes="This is seasoned water for eddard stark")    # create order_items test
bridge.edit_order_item(active_order_items[-1], "quantity", 6)                                           # update order_items test
bridge.remove_order_item(active_order_items[-1])                                                       # delete order_items test
'''

'''
test = Order.Order("Test Tester")
bridge.add_order(test.order_id, test.queue_num, test.customer_name, test.order_status)                    # create orders test
bridge.add_order_item(orders[1], menu_items[3], notes="this will be deleted soon!")
bridge.add_order_item(orders[1], menu_items[2], notes="this will be deleted as well!")
bridge.edit_order(orders[1], "order_status", 'x')                                               # update orders test
bridge.remove_order(orders[1])                                                                 # delete orders test
'''

'''
while running:
    pass
'''
