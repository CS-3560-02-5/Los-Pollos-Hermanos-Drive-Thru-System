import MenuItem
import OrderItem
import Order
import data_bridge

############ Open all interfaces here


###################################
running = True

####### Initial setup of running environment
bridge = data_bridge.bridge("sql.json")

# Rebuild all currently active orders
active_orders = []
for index, order in bridge.get_active_orders().sort_values(by=["queue_num"]).iterrows():
    #active_orders.append(Order.Order(order["customer_name"], order_id=order["order_id"], order_status=order["order_status"]))
    active_orders.append(Order.Order(**order))


# Rebuild all items attatched to the active orders
active_order_items = []
for order in active_orders:
    for index, item in bridge.get_order_items(order).iterrows():
        active_order_items.append(OrderItem.OrderItem(**item))

# Rebuild all menu items
menu_items = []
for index, item in bridge.get_menu_items().iterrows():
    menu_items.append(MenuItem.MenuItem(**item))


#### TESTING
print([x.__dict__ for x in active_orders])
print([x.__dict__ for x in active_order_items])
print([(x.item_name + ": " + str(x.item_id)) for x in menu_items])

'''
bridge.add_menu_item(9, "The Tester", "Purely to test the add function", 4.20, menu_items[0].image)        # create menu_items test
bridge.edit_menu_item(menu_items[8], "item_description", "This is the updated value!")                    # update menu_items test
bridge.remove_menu_item(menu_items[8])                                                                 # delete menu_items test
'''

'''
bridge.add_order_item(active_orders[1], menu_items[7], notes="This is seasoned water for eddard stark")    # create order_items test
bridge.edit_order_item(active_order_items[-1], "quantity", 6)                                           # update order_items test
bridge.remove_order_item(active_order_items[-1])                                                       # delete order_items test
'''

'''
test = Order.Order("Test Tester")
bridge.add_order(test.order_id, test.queue_num, test.customer_name, test.order_status)                    # create orders test
bridge.add_order_item(active_orders[1], menu_items[3], notes="this will be deleted soon!")
bridge.add_order_item(active_orders[1], menu_items[2], notes="this will be deleted as well!")
bridge.edit_order(active_orders[1], "order_status", 'x')                                               # update orders test
bridge.remove_order(active_orders[1])                                                                 # delete orders test
'''

'''
while running:
    pass
'''
