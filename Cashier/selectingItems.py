# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectingItems.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_selectingItems(object):
    def setupUi(self, selectingItems):
        selectingItems.setObjectName("selectingItems")
        selectingItems.resize(1598, 900)
        selectingItems.setAutoFillBackground(False)
        selectingItems.setStyleSheet("QMainWindow#selectingItems{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.449, x2:0, y2:1, stop:0.60199 rgba(255, 255, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.centralwidget = QtWidgets.QWidget(selectingItems)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.topSide = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topSide.sizePolicy().hasHeightForWidth())
        self.topSide.setSizePolicy(sizePolicy)
        self.topSide.setObjectName("topSide")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.topSide)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menu = QtWidgets.QWidget(self.topSide)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu.sizePolicy().hasHeightForWidth())
        self.menu.setSizePolicy(sizePolicy)
        self.menu.setObjectName("menu")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.menu)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_2 = QtWidgets.QWidget(self.menu)
        self.widget_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setStyleSheet("border: none;\n"
"color: rgb(255, 0, 0);\n"
"font: 26pt \"Forte\";\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setStyleSheet("border: none;\n"
"color: rgb(255, 0, 0);\n"
"font: 26pt \"Forte\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setStyleSheet("border: none;\n"
"color: rgb(255, 0, 0);\n"
"font: 26pt \"Forte\";")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout_6.addWidget(self.widget_2, 0, QtCore.Qt.AlignTop)
        self.widget_3 = QtWidgets.QWidget(self.menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(self.widget_3)
        self.widget.setObjectName("widget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_7.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_8 = QtWidgets.QWidget(self.widget)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label = QtWidgets.QLabel(self.widget_8)
        self.label.setStyleSheet("image: url(:/images/menuImages/chickSan.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_8)
        self.pushButton_5.setStyleSheet("border: none;\n"
"color: rgb(255, 0, 0);\n"
"font: 20pt \"Forte\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_8.addWidget(self.pushButton_5)
        self.verticalLayout_7.addWidget(self.widget_8)
        self.widget_7 = QtWidgets.QWidget(self.widget)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_2 = QtWidgets.QLabel(self.widget_7)
        self.label_2.setStyleSheet("image: url(:/images/menuImages/waltersNuggies.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_9.addWidget(self.label_2)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_6.setStyleSheet("border: none;\n"
"color: rgb(255, 0, 0);\n"
"font: 20pt \"Forte\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_9.addWidget(self.pushButton_6)
        self.verticalLayout_7.addWidget(self.widget_7)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_3 = QtWidgets.QLabel(self.widget_6)
        self.label_3.setStyleSheet("image: url(:/images/menuImages/wangBang.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_10.addWidget(self.label_3)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_7.setStyleSheet("border: none;\n"
"color: rgb(255, 0, 0);\n"
"font: 20pt \"Forte\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_10.addWidget(self.pushButton_7)
        self.verticalLayout_7.addWidget(self.widget_6)
        self.horizontalLayout_2.addWidget(self.widget)
        self.widget_5 = QtWidgets.QWidget(self.widget_3)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_12.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_12.setSpacing(20)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.widget_9 = QtWidgets.QWidget(self.widget_5)
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.widget_9)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_5 = QtWidgets.QLabel(self.widget_9)
        self.label_5.setStyleSheet("image: url(:/images/menuImages/lastFridaysFries.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_13.addWidget(self.label_5)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget_9)
        self.pushButton_9.setStyleSheet("border: none;\n"
"color: rgb(255, 0, 0);\n"
"font: 20pt \"Forte\";")
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_13.addWidget(self.pushButton_9)
        self.verticalLayout_12.addWidget(self.widget_9)
        self.widget_10 = QtWidgets.QWidget(self.widget_5)
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_6 = QtWidgets.QLabel(self.widget_10)
        self.label_6.setStyleSheet("image: url(:/images/menuImages/holyBread.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_14.addWidget(self.label_6)
        self.pushButton_10 = QtWidgets.QPushButton(self.widget_10)
        self.pushButton_10.setStyleSheet("border: none;\n"
"color: rgb(255, 0, 0);\n"
"font: 20pt \"Forte\";")
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_14.addWidget(self.pushButton_10)
        self.verticalLayout_12.addWidget(self.widget_10)
        self.widget_11 = QtWidgets.QWidget(self.widget_5)
        self.widget_11.setObjectName("widget_11")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.widget_11)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_7 = QtWidgets.QLabel(self.widget_11)
        self.label_7.setStyleSheet("image: url(:/images/menuImages/mack.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_15.addWidget(self.label_7)
        self.pushButton_11 = QtWidgets.QPushButton(self.widget_11)
        self.pushButton_11.setStyleSheet("border: none;\n"
"color: rgb(255, 0, 0);\n"
"font: 20pt \"Forte\";")
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_15.addWidget(self.pushButton_11)
        self.verticalLayout_12.addWidget(self.widget_11)
        self.horizontalLayout_2.addWidget(self.widget_5)
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_16.setContentsMargins(20, 20, 20, 200)
        self.verticalLayout_16.setSpacing(20)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.widget_12 = QtWidgets.QWidget(self.widget_4)
        self.widget_12.setObjectName("widget_12")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.widget_12)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_8 = QtWidgets.QLabel(self.widget_12)
        self.label_8.setStyleSheet("image: url(:/images/menuImages/seasonedWater.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_17.addWidget(self.label_8)
        self.pushButton_12 = QtWidgets.QPushButton(self.widget_12)
        self.pushButton_12.setStyleSheet("border: none;\n"
"color: rgb(255, 0, 0);\n"
"font: 20pt \"Forte\";")
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_17.addWidget(self.pushButton_12)
        self.verticalLayout_16.addWidget(self.widget_12)
        self.widget_13 = QtWidgets.QWidget(self.widget_4)
        self.widget_13.setObjectName("widget_13")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.widget_13)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_9 = QtWidgets.QLabel(self.widget_13)
        self.label_9.setStyleSheet("image: url(:/images/menuImages/dihydrogenMonoxide.png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_18.addWidget(self.label_9)
        self.pushButton_13 = QtWidgets.QPushButton(self.widget_13)
        self.pushButton_13.setStyleSheet("border: none;\n"
"color: rgb(255, 0, 0);\n"
"font: 14pt \"Forte\";")
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_18.addWidget(self.pushButton_13)
        self.verticalLayout_16.addWidget(self.widget_13)
        self.horizontalLayout_2.addWidget(self.widget_4)
        self.verticalLayout_6.addWidget(self.widget_3)
        self.horizontalLayout.addWidget(self.menu)
        self.summary = QtWidgets.QWidget(self.topSide)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.summary.sizePolicy().hasHeightForWidth())
        self.summary.setSizePolicy(sizePolicy)
        self.summary.setStyleSheet("QWidget#summary{\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"}")
        self.summary.setObjectName("summary")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.summary)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_15 = QtWidgets.QWidget(self.summary)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy)
        self.widget_15.setStyleSheet("border-bottom: 2px solid black;")
        self.widget_15.setObjectName("widget_15")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_15)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame = QtWidgets.QFrame(self.widget_15)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.orderLabel = QtWidgets.QLabel(self.frame)
        self.orderLabel.setStyleSheet("border: none;\n"
"color: rgb(0, 0, 0);\n"
"font: 26pt \"Arial\";")
        self.orderLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.orderLabel.setObjectName("orderLabel")
        self.horizontalLayout_6.addWidget(self.orderLabel)
        self.horizontalLayout_5.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.widget_15)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.orderNumLabel = QtWidgets.QLabel(self.frame_2)
        self.orderNumLabel.setStyleSheet("border: none;\n"
"color: rgb(0, 0, 0);\n"
"font: 26pt \"Arial\";")
        self.orderNumLabel.setObjectName("orderNumLabel")
        self.horizontalLayout_7.addWidget(self.orderNumLabel)
        self.horizontalLayout_5.addWidget(self.frame_2)
        self.verticalLayout_5.addWidget(self.widget_15)
        self.widget_14 = QtWidgets.QWidget(self.summary)
        self.widget_14.setObjectName("widget_14")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_14)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.widget_14)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_10 = QtWidgets.QFrame(self.widget_14)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_2.addWidget(self.frame_10)
        self.frame_4 = QtWidgets.QFrame(self.widget_14)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_9 = QtWidgets.QFrame(self.widget_14)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_2.addWidget(self.frame_9)
        self.frame_5 = QtWidgets.QFrame(self.widget_14)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_8 = QtWidgets.QFrame(self.widget_14)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_2.addWidget(self.frame_8)
        self.frame_6 = QtWidgets.QFrame(self.widget_14)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.widget_14)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_2.addWidget(self.frame_7)
        self.verticalLayout_5.addWidget(self.widget_14)
        self.pushButton_4 = QtWidgets.QPushButton(self.summary)
        self.pushButton_4.setStyleSheet("border: none;\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"Arial\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_5.addWidget(self.pushButton_4)
        self.horizontalLayout.addWidget(self.summary, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.topSide)
        self.buttomSide = QtWidgets.QWidget(self.centralwidget)
        self.buttomSide.setObjectName("buttomSide")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.buttomSide)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cancelbtn = QtWidgets.QPushButton(self.buttomSide)
        self.cancelbtn.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(111, 210, 255);\n"
"font: 75 26pt \"Arial\";\n"
"border-style: outset;\n"
"border-width: 5px;\n"
"border-color: rgb(21, 76, 152);")
        self.cancelbtn.setObjectName("cancelbtn")
        self.horizontalLayout_3.addWidget(self.cancelbtn)
        spacerItem = QtWidgets.QSpacerItem(800, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.finishbtn = QtWidgets.QPushButton(self.buttomSide)
        self.finishbtn.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(111, 210, 255);\n"
"font: 75 26pt \"Arial\";\n"
"border-style: outset;\n"
"border-width: 5px;\n"
"border-color: rgb(21, 76, 152);")
        self.finishbtn.setObjectName("finishbtn")
        self.horizontalLayout_3.addWidget(self.finishbtn)
        self.verticalLayout.addWidget(self.buttomSide)
        selectingItems.setCentralWidget(self.centralwidget)

        self.retranslateUi(selectingItems)
        QtCore.QMetaObject.connectSlotsByName(selectingItems)

    def retranslateUi(self, selectingItems):
        _translate = QtCore.QCoreApplication.translate
        selectingItems.setWindowTitle(_translate("selectingItems", "MainWindow"))
        self.pushButton_3.setText(_translate("selectingItems", "Foods"))
        self.pushButton_2.setText(_translate("selectingItems", "Sides"))
        self.pushButton.setText(_translate("selectingItems", "Drinks"))
        self.pushButton_5.setText(_translate("selectingItems", "Chick San"))
        self.pushButton_6.setText(_translate("selectingItems", "Walter\'s Nuggies"))
        self.pushButton_7.setText(_translate("selectingItems", "Wang Bang"))
        self.pushButton_9.setText(_translate("selectingItems", "Last Friday\'s Fries"))
        self.pushButton_10.setText(_translate("selectingItems", "Holy Bread"))
        self.pushButton_11.setText(_translate("selectingItems", "Mack"))
        self.pushButton_12.setText(_translate("selectingItems", "Seasoned Water"))
        self.pushButton_13.setText(_translate("selectingItems", "Dihydrogen Monoxide"))
        self.orderLabel.setText(_translate("selectingItems", "Order: "))
        self.orderNumLabel.setText(_translate("selectingItems", "00"))
        self.pushButton_4.setText(_translate("selectingItems", "this is a space maker for the summary sections to be displayed in a proper width. This text is not meant to be seen by anyone."))
        self.cancelbtn.setText(_translate("selectingItems", "Cancel Order"))
        self.finishbtn.setText(_translate("selectingItems", "Finish Order"))
import menuImages


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    selectingItems = QtWidgets.QMainWindow()
    ui = Ui_selectingItems()
    ui.setupUi(selectingItems)
    selectingItems.show()
    sys.exit(app.exec_())
