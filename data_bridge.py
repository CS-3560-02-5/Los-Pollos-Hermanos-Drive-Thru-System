import mysql.connector
import json
import pandas as pd
import Order

class bridge:
    def __init__(self, json_file_str):
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
