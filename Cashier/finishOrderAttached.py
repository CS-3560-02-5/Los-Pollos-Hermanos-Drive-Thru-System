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

        name = self.inputNameLineEdit.text()

    def goBack(self):
        self.orderTableWidget.clearContents()
        row = self.orderTableWidget.rowCount()
        for i in range(row):
            self.orderTableWidget.removeRow(0)
        self.hide()

    def sendToDatabase(self):
        self.hide()
