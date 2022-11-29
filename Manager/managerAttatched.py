from managerGUI import Ui_manager_QWidget
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow
import sys

class managerAttatched(Ui_manager_QWidget, QMainWindow):
    def __init__(self, df, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.load(df)
        self.show()

    def load(self, df):
        model = PandasModel(df)
        self.menuItems_tableView.setModel(model)


    def connectSignalsSlots(self):
        self.addItem_pushButton.clicked.connect(self.addMenuItem_GUI)
        self.editItem_pushButton.clicked.connect(self.editMenuItem_GUI)
        self.removeItem_pushButton.clicked.connect(self.removeMenuItem_GUI)
        
    def addMenuItem_GUI(self):
        pass
    def removeMenuItem_GUI(self):
        print("works")

    def editMenuItem_GUI(self):
        print("works")

class PandasModel(QtGui.QStandardItemModel):
    def __init__(self, data, parent=None):
        QtGui.QStandardItemModel.__init__(self, parent)
        self._data = data
        for col in data.columns:
            data_col = [QtGui.QStandardItem("{}".format(x)) for x in data[col].values]
            self.appendColumn(data_col)
        return

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def headerData(self, x, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[x]
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return self._data.index[x]
        return None