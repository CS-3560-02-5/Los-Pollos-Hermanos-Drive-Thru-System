import cookGUI
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
import sys

# compile cookGUI.py file on cmd: pyuic5 -x cookGUI.ui -o cookGUI.py

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    cook_win = QtWidgets.QMainWindow()
    (cook_win)
    sys.exit(app.exec_())

app = QtWidgets.QApplication(sys.argv)
cook_win = QtWidgets.QMainWindow()
