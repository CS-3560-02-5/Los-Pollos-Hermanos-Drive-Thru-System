import mysql.connector
import json
import pandas as pd
import Order
import MenuItem

class bridge:
    def __init__(self, json_file_str: str):
        f = open(json_file_str, 'r')
        info = json.load(f)
        print("Connecting to server \""
              + info["host"] + "\"...")
        print("Using database \""
              + info["database"] + "\"...")
        self.mydb = mysql.connector.connect(**info)
        f.close()

    def get_active_orders(self) -> pd.DataFrame:
        return pd.read_sql("select * from orders where order_status != 'c' and order_status != 'x'", self.mydb)

    def get_items(self, Order: Order) -> pd.DataFrame:
        return pd.read_sql("select * from order_items where order_id = \"" + Order.order_id + "\"", self.mydb)

    def get_menu_items(self) -> pd.DataFrame:
        return pd.read_sql("select * from menu_items", self.mydb)

    def add_order_item(self, Order: Order, MenuItem: MenuItem, *, quantity=1, notes=None):
        with self.mydb.cursor() as cursor:
            cursor.execute("insert into order_items (order_id, item_id, quantity, notes) values ("
                           + "\"" + Order.order_id + "\", "
                           + str(MenuItem.item_id) + ", "
                           + str(quantity) + ", "
                           + "\"" + str(notes) + "\")")
        self.mydb.commit()

    def remove_order_item(self, Order: Order, MenuItem: MenuItem):
        with self.mydb.cursor() as cursor:
            cursor.execute("delete from order_items where order_id = \""
                           + Order.order_id + "\" and item_id = \""
                           + str(MenuItem.item_id) + "\"")
        self.mydb.commit()

    def edit_order_item(self, Order: Order, MenuItem: MenuItem, attribute: str):
        with self.mydb.cursor() as cursor:
            cursor.execute("update order_items set ")
