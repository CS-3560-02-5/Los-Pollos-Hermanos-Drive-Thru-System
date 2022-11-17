import MenuItem
import OrderItem
import Order
import data_bridge

############ Open all interfaces here


###################################
running = True

# Initial setup of running environment
bridge = data_bridge.bridge("sql.json")

## Rebuild all currently active orders
active_orders = []
for index, order in bridge.get_active_orders().sort_values(by=["queue_num"]).iterrows():
    active_orders.append(Order.Order(order["customer_name"], order_id=order["order_id"], status=order["order_status"]))

## Rebuild all items attatched to the active orders
active_order_items = []
for order in active_orders:
    for index, item in bridge.get_items(order).iterrows():
        active_order_items.append(OrderItem.OrderItem(item["order_id"], item["item_id"], item["quantity"], item["notes"]))

## Rebuild all menu items
menu_items = []
for index, item in bridge.get_menu_items().iterrows():
    menu_items.append(MenuItem.MenuItem(item["item_name"], item["item_id"], item["price"], item["item_description"], item["image"]))

print([x.__dict__ for x in active_orders])
print([x.item_id for x in menu_items])
#### TESTING
bridge.remove_order_item(active_orders[0], menu_items[4])

'''
while running:
    pass
'''
