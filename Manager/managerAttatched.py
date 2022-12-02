from managerGUI import Ui_manager_QWidget
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QDialog
import sys
from editDialog import Ui_edit_Dialog


class managerAttatched(Ui_manager_QWidget, QMainWindow):
    def __init__(self, menu_items, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.menu_items = menu_items
        self.edit_dlg = editDialog(self)
        self.connectSignalsSlots()
        self.load(self.menu_items)
        self.show()

    def load(self, menu_items):
        self.menuItems_listWidget.addItems([x.item_name for x in menu_items])


    def connectSignalsSlots(self):
        self.addItem_pushButton.clicked.connect(self.addMenuItem_GUI)
        self.editItem_pushButton.clicked.connect(self.editMenuItem_GUI)
        self.removeItem_pushButton.clicked.connect(self.removeMenuItem_GUI)

    def addMenuItem_GUI(self):
        print(self.data)

    def removeMenuItem_GUI(self):
        print("works")

    def editMenuItem_GUI(self):
        try:
            index = next((i for i, item in enumerate(self.menu_items) if item.item_name == self.menuItems_listWidget.currentItem().text()), -1)
            current_item = self.menu_items[index]
            self.edit_dlg.ui.itemName_plainTextEdit.setPlainText(current_item.item_name)
            self.edit_dlg.ui.description_plainTextEdit.setPlainText(current_item.item_description)
            self.edit_dlg.ui.price_plainTextEdit.setPlainText(str(current_item.price))
            self.edit_dlg.exec_()
            current_item.item_name = self.edit_dlg.ui.itemName_plainTextEdit.toPlainText()
            current_item.item_description = self.edit_dlg.ui.description_plainTextEdit.toPlainText()
            current_item.price = float(self.edit_dlg.ui.price_plainTextEdit.toPlainText())
            self.menu_items[index] = current_item
        except:
            pass


class editDialog(QDialog):
    """edit a menu item"""
    def __init__(self, item , parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_edit_Dialog()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        
        