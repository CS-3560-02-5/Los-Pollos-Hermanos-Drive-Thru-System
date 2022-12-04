# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manageOrderList.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("QMainWindow#MainWindow\n"
"{\n"
"background-color: rgb(89, 89, 89);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.orderListWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.orderListWidget.sizePolicy().hasHeightForWidth())
        self.orderListWidget.setSizePolicy(sizePolicy)
        self.orderListWidget.setMaximumSize(QtCore.QSize(5000, 16777215))
        self.orderListWidget.setObjectName("orderListWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.orderListWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.custName_LineEdit = QtWidgets.QLineEdit(self.orderListWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.custName_LineEdit.setFont(font)
        self.custName_LineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.custName_LineEdit.setStyleSheet("color: rgb(0, 255, 0);\n"
"background-color: rgb(136, 136, 136);\n"
"border: 2px solid #ccc;\n"
"border-color: rgb(0, 0, 0);")
        self.custName_LineEdit.setText("")
        self.custName_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.custName_LineEdit.setObjectName("custName_LineEdit")
        self.verticalLayout_2.addWidget(self.custName_LineEdit)
        self.orderList_TableWidget = QtWidgets.QTableWidget(self.orderListWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.orderList_TableWidget.sizePolicy().hasHeightForWidth())
        self.orderList_TableWidget.setSizePolicy(sizePolicy)
        self.orderList_TableWidget.setMinimumSize(QtCore.QSize(400, 0))
        self.orderList_TableWidget.setMaximumSize(QtCore.QSize(10000000, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.orderList_TableWidget.setFont(font)
        self.orderList_TableWidget.setAutoFillBackground(False)
        self.orderList_TableWidget.setStyleSheet("border: 1px solid #ccc;\n"
"border-color: rgb(0, 0, 0);\n"
"font: 12pt \"Arial\";\n"
"color: rgb(0, 0, 0);")
        self.orderList_TableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.orderList_TableWidget.setAlternatingRowColors(False)
        self.orderList_TableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.orderList_TableWidget.setShowGrid(False)
        self.orderList_TableWidget.setCornerButtonEnabled(False)
        self.orderList_TableWidget.setObjectName("orderList_TableWidget")
        self.orderList_TableWidget.setColumnCount(3)
        self.orderList_TableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.orderList_TableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.orderList_TableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.orderList_TableWidget.setHorizontalHeaderItem(2, item)
        self.orderList_TableWidget.horizontalHeader().setVisible(True)
        self.orderList_TableWidget.horizontalHeader().setHighlightSections(True)
        self.orderList_TableWidget.verticalHeader().setVisible(False)
        self.orderList_TableWidget.verticalHeader().setHighlightSections(False)
        self.verticalLayout_2.addWidget(self.orderList_TableWidget)
        self.horizontalLayout.addWidget(self.orderListWidget)
        self.OrderListButtonWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OrderListButtonWidget.sizePolicy().hasHeightForWidth())
        self.OrderListButtonWidget.setSizePolicy(sizePolicy)
        self.OrderListButtonWidget.setObjectName("OrderListButtonWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.OrderListButtonWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.increment_spinBox = QtWidgets.QSpinBox(self.OrderListButtonWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.increment_spinBox.sizePolicy().hasHeightForWidth())
        self.increment_spinBox.setSizePolicy(sizePolicy)
        self.increment_spinBox.setMinimumSize(QtCore.QSize(300, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.increment_spinBox.setFont(font)
        self.increment_spinBox.setStyleSheet("font: 75 22pt \"Arial\";\n"
"border: 1px solid #ccc;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(136, 136, 136);\n"
"color: rgb(0, 255, 0);")
        self.increment_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.increment_spinBox.setMinimum(1)
        self.increment_spinBox.setMaximum(99)
        self.increment_spinBox.setObjectName("increment_spinBox")
        self.verticalLayout.addWidget(self.increment_spinBox)
        self.accept_but = QtWidgets.QPushButton(self.OrderListButtonWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accept_but.sizePolicy().hasHeightForWidth())
        self.accept_but.setSizePolicy(sizePolicy)
        self.accept_but.setMinimumSize(QtCore.QSize(300, 100))
        self.accept_but.setStyleSheet("color: rgb(0, 255, 0);\n"
"background-color: rgb(136, 136, 136);\n"
"font: 100 20pt \"Arial\";\n"
"border: 2px solid #ccc;\n"
"border-color: rgb(0, 0, 0);")
        self.accept_but.setObjectName("accept_but")
        self.verticalLayout.addWidget(self.accept_but)
        self.void_but = QtWidgets.QPushButton(self.OrderListButtonWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.void_but.sizePolicy().hasHeightForWidth())
        self.void_but.setSizePolicy(sizePolicy)
        self.void_but.setMinimumSize(QtCore.QSize(300, 100))
        self.void_but.setStyleSheet("color: rgb(0, 255, 0);\n"
"background-color: rgb(136, 136, 136);\n"
"font: 100 20pt \"Arial\";\n"
"border: 2px solid #ccc;\n"
"border-color: rgb(0, 0, 0);")
        self.void_but.setObjectName("void_but")
        self.verticalLayout.addWidget(self.void_but)
        self.back_but = QtWidgets.QPushButton(self.OrderListButtonWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_but.sizePolicy().hasHeightForWidth())
        self.back_but.setSizePolicy(sizePolicy)
        self.back_but.setMinimumSize(QtCore.QSize(100, 50))
        self.back_but.setStyleSheet("color: rgb(0, 255, 0);\n"
"background-color: rgb(136, 136, 136);\n"
"font: 100 15pt \"Arial\";\n"
"border: 2px solid #ccc;\n"
"border-color: rgb(0, 0, 0);")
        self.back_but.setObjectName("back_but")
        self.verticalLayout.addWidget(self.back_but)
        self.horizontalLayout.addWidget(self.OrderListButtonWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.orderList_TableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Item"))
        item = self.orderList_TableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Amt."))
        item = self.orderList_TableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Notes"))
        self.accept_but.setText(_translate("MainWindow", "ACCEPT CHANGES"))
        self.void_but.setText(_translate("MainWindow", "VOID ITEM"))
        self.back_but.setText(_translate("MainWindow", "BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
