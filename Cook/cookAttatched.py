from cookGUI import Ui_Dialog
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

class cookAttatched(Ui_Dialog, QMainWindow):
    def __init__(self, df, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.queue = []
        self.connectSignalsSlots()
        self.load(df)
    
    def connectSignalsSlots(self):
        pass

    def load(self, df):
        for index, item in df.iterrows():
            self.queue.append(SeriesModel(item))
        self.listView_4.setModel(self.queue[0])


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

class SeriesModel(QtGui.QStandardItemModel):
    def __init__(self, data, parent=None):
        QtGui.QStandardItemModel.__init__(self, parent)
        self._data = data
        data_col = [QtGui.QStandardItem("{}".format(x)) for x in data.values]
        self.appendColumn(data_col)
        return

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return 1

    def headerData(self, x, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[x]
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return self._data.index[x]
        return None
