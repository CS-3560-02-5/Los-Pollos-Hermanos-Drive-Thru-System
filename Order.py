import uuid
from itertools import cycle
import OrderItem
import MenuItem
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow
import sys


class Order:
    queue = cycle(range(1, 200))

    def __init__(self, customer_name: str, *, order_id=uuid.uuid1().hex, order_status='s', queue_num=-1):
        self.customer_name = customer_name
        self.order_id = order_id
        self.queue_num = next(self.queue)
        self.order_status = order_status

    def prepare(self):
        self.order_status = 'p'
        return self

    def complete(self):
        self.order_status = "c"
        self.queue_num = 0

    def cancel(self):
        self.order_status = 'x'
        self.queue_num = 0

    def createOrderItem(self, menuItem: MenuItem, *, quantity=1, notes=None):
        return OrderItem.OrderItem(self.order_id, menuItem.item_id, quantity=quantity, notes=notes)
        
        
