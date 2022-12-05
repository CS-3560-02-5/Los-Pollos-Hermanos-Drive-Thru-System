import sys
from PyQt5 import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt

from selectingItemsAttached import *
from finishOrder import *
import Order

class finishOrderAttatched(Ui_finishOrder, QMainWindow):

    def __init__(self, mass, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.mass = mass

        self.orderTableWidget.setColumnWidth(0, 200)
        self.orderTableWidget.setColumnWidth(1, 200)
        self.orderTableWidget.setColumnWidth(2, 400)
        self.backBtn.clicked.connect(self.goBack)
        self.orderNumLabel.setText(str(self.mass.orders[-1].queue_num+1))
        self.submitOrderBtn.clicked.connect(self.sendToDatabase)

    def goBack(self):
        self.orderTableWidget.clearContents()
        row = self.orderTableWidget.rowCount()
        for i in range(row):
            self.orderTableWidget.removeRow(0)
        self.hide()

    def sendToDatabase(self):
        self.hide()
        newOrder = Order.Order(self.inputNameLineEdit.text())
        self.mass.add_order(newOrder)
        row = self.orderTableWidget.rowCount()
        for row in range(row):
            orderItem = self.orderTableWidget.item(row, 0).text()
            orderId = next(i.item_id for i in self.mass.menu_items if i.item_name == orderItem)
            orderQty = self.orderTableWidget.item(row, 1).text()
            orderNotes = self.orderTableWidget.item(row, 2).text()
            temp = newOrder.createOrderItem(int(orderId), quantity=int(orderQty), notes=orderNotes)
            self.mass.add_order_item(temp)
