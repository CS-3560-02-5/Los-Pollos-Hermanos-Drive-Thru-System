import mysql.connector
import json
import pandas as pd
import Order
import MenuItem
import OrderItem


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

    ################# Getter Operations #################

    def get_active_orders(self) -> pd.DataFrame:
        return pd.read_sql("select * from orders where order_status != 'c' and order_status != 'x'", self.mydb)

    def get_order_items(self, Order: Order) -> pd.DataFrame:
        return pd.read_sql("select * from order_items where order_id = \"" + Order.order_id + "\"", self.mydb)

    def get_menu_items(self) -> pd.DataFrame:
        return pd.read_sql("select * from menu_items", self.mydb)

    ################# MenuItem Operations #################

    def add_menu_item(self, item_id: int, item_name: str, item_description: str, price: float, image: str):
        with self.mydb.cursor() as cursor:
            cursor.execute("insert into menu_items (item_id, item_name, item_description, price, image) values ("
                           + str(item_id) + ", "
                           + "\"" + item_name + "\", "
                           + "\"" + item_description + "\", "
                           + str(price) + ", "
                           + "%s)", [image])
        self.mydb.commit()

    def remove_menu_item(self, MenuItem: MenuItem):
        with self.mydb.cursor() as cursor:
            cursor.execute("delete from menu_items where item_id = "
                           + str(MenuItem.item_id))
        self.mydb.commit()

    def edit_menu_item(self, MenuItem: MenuItem, attribute: str, value):
        if attribute == "price":
            with self.mydb.cursor() as cursor:
                cursor.execute("update menu_items set "
                               + attribute + " = "
                               + str(value) + " where item_id = "
                               + MenuItem.item_id)
            self.mydb.commit()
        elif attribute == "item_name" or attribute == "item_description":
            with self.mydb.cursor() as cursor:
                cursor.execute("update menu_items set "
                               + attribute + " = "
                               + "\"" + value + "\" where item_id = "
                               + str(MenuItem.item_id))
            self.mydb.commit()
        else:
            print("The attribute " + str(attribute) + " is not a valid value")

    ################# Order Operations #################

    def add_order(self, order_id: str, queue_num: int, customer_name: str, order_status: chr):
        with self.mydb.cursor() as cursor:
            cursor.execute("insert into orders (order_id, queue_num, customer_name, order_status) values ("
                           + "\"" + order_id + "\", "
                           + str(queue_num) + ", "
                           + "\"" + customer_name + "\", "
                           + "\'" + order_status + "\')")
        self.mydb.commit()

    def remove_order(self, Order: Order):
        with self.mydb.cursor() as cursor:
            for index, item in self.get_order_items(Order).iterrows():
                cursor.execute("delete from order_items where order_id = \""
                               + item["order_id"] + "\" and item_id = "
                               + str(item["item_id"]))
            cursor.execute("delete from orders where order_id = \""
                           + Order.order_id + "\"")
        self.mydb.commit()

    def edit_order(self, Order: Order, attribute: str, value):
        if attribute == "queue_num":
            with self.mydb.cursor() as cursor:
                cursor.execute("update orders set "
                               + attribute + " = "
                               + str(value) + " where order_id = \""
                               + Order.order_id + "\"")
            self.mydb.commit()
        elif attribute == "customer_name" or attribute == "order_status":
            with self.mydb.cursor() as cursor:
                cursor.execute("update orders set "
                               + attribute + " = "
                               + "\"" + value + "\" where order_id = \""
                               + Order.order_id + "\"")
            self.mydb.commit()
        else:
            print("The attribute " + str(attribute) + " is not a valid value")

    ################# OrderItem Operations #################

    def add_order_item(self, Order: Order, MenuItem: MenuItem, *, quantity=1, notes=None):
        with self.mydb.cursor() as cursor:
            cursor.execute("insert into order_items (order_id, item_id, quantity, notes) values ("
                           + "\"" + Order.order_id + "\", "
                           + str(MenuItem.item_id) + ", "
                           + str(quantity) + ", "
                           + "\"" + str(notes) + "\")")
        self.mydb.commit()

    def remove_order_item(self, OrderItem: OrderItem):
        with self.mydb.cursor() as cursor:
            cursor.execute("delete from order_items where order_id = \""
                           + OrderItem.order_id + "\" and item_id = \""
                           + str(OrderItem.item_id) + "\"")
        self.mydb.commit()

    def edit_order_item(self, OrderItem: OrderItem, attribute: str, value):
        if attribute == "quantity":
            with self.mydb.cursor() as cursor:
                cursor.execute("update order_items set "
                               + attribute + " = "
                               + str(value) + " where order_id = \""
                               + OrderItem.order_id + "\" and item_id = "
                               + str(OrderItem.item_id))
            self.mydb.commit()
        elif attribute == "notes":
            with self.mydb.cursor() as cursor:
                cursor.execute("update order_items set "
                               + attribute + " = "
                               + "\"" + str(value) + "\" where order_id = \""
                               + OrderItem.order_id + "\" and item_id = "
                               + str(OrderItem.item_id))
            self.mydb.commit()
        else:
            print("The attribute " + str(attribute) + " is not a valid value")
