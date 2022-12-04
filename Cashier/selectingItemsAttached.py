import sys
from PyQt5 import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt

from welcomeScreen import *
from selectingItems import *
from finishOrder import *

class selectingItemsAttatched(Ui_selectingItems, QMainWindow):

    def __init__(self, mass, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.mass = mass
        self.cancelbtn.clicked.connect(self.closeWindow)
        self.orderFrame1.hide()
        self.orderFrame2.hide()
        self.orderFrame3.hide()
        self.orderFrame4.hide()
        self.orderFrame5.hide()
        self.orderFrame6.hide()
        self.orderFrame7.hide()
        self.orderFrame8.hide()

        self.chickSanBtn.clicked.connect(self.showCSFrm)
        self.chickSanPicBtn.clicked.connect(self.showCSFrm)
        self.waltersNuggiesBtn.clicked.connect(self.showWNFrm)
        self.waltersNuggiesPicBtn.clicked.connect(self.showWNFrm)
        self.wanBangBtn.clicked.connect(self.showWBFrm)
        self.wanBangPicBtn.clicked.connect(self.showWBFrm)
        self.lastFFriesBtn.clicked.connect(self.showLFFFrm)
        self.lastFFriesPicBtn.clicked.connect(self.showLFFFrm)
        self.holyBreadBtn.clicked.connect(self.showHBFrm)
        self.holyBreadPicBtn.clicked.connect(self.showHBFrm)
        self.mackBtn.clicked.connect(self.showMFrm)
        self.mackPicBtn.clicked.connect(self.showMFrm)
        self.seaWtrBtn.clicked.connect(self.showSWFrm)
        self.seaWtrPicBtn.clicked.connect(self.showSWFrm)
        self.diMoxBtn.clicked.connect(self.showDMFrm)
        self.diMoxPicBtn.clicked.connect(self.showDMFrm)

        self.order1CancelBtn.clicked.connect(self.hideCSFrm)
        self.order2CancelBtn.clicked.connect(self.hideWNFrm)
        self.order3CancelBtn.clicked.connect(self.hideWBFrm)
        self.order4CancelBtn.clicked.connect(self.hideLFFFrm)
        self.order5CancelBtn.clicked.connect(self.hideHBFrm)
        self.order6CancelBtn.clicked.connect(self.hideMFrm)
        self.order7CancelBtn.clicked.connect(self.hideSWFrm)
        self.order8CancelBtn.clicked.connect(self.hideDMFrm)

    def closeWindow(self):
        self.hide()

    def showCSFrm(self):
        self.orderFrame1.show()
        self.chickSanWid.setStyleSheet("border-style: outset;\n"
        "border-width: 5px;\n"
        "border-color: rgb(0, 255, 0);")
    
    def showWNFrm(self):
        self.orderFrame2.show()
        self.waltersNuggiesWid.setStyleSheet("border-style: outset;\n"
        "border-width: 5px;\n"
        "border-color: rgb(0, 255, 0);")
    
    def showWBFrm(self):
        self.orderFrame3.show()
        self.wangBangWid.setStyleSheet("border-style: outset;\n"
        "border-width: 5px;\n"
        "border-color: rgb(0, 255, 0);")
    
    def showLFFFrm(self):
        self.orderFrame4.show()
        self.lastFFriesWid.setStyleSheet("border-style: outset;\n"
        "border-width: 5px;\n"
        "border-color: rgb(0, 255, 0);")
    
    def showHBFrm(self):
        self.orderFrame5.show()
        self.holyBreadWid.setStyleSheet("border-style: outset;\n"
        "border-width: 5px;\n"
        "border-color: rgb(0, 255, 0);")
    
    def showMFrm(self):
        self.orderFrame6.show()
        self.mackWid.setStyleSheet("border-style: outset;\n"
        "border-width: 5px;\n"
        "border-color: rgb(0, 255, 0);")
    
    def showSWFrm(self):
        self.orderFrame7.show()
        self.seaWtrWid.setStyleSheet("border-style: outset;\n"
        "border-width: 5px;\n"
        "border-color: rgb(0, 255, 0);")
    
    def showDMFrm(self):
        self.orderFrame8.show()
        self.diMoxWid.setStyleSheet("border-style: outset;\n"
        "border-width: 5px;\n"
        "border-color: rgb(0, 255, 0);")

    def hideCSFrm(self):
        self.orderFrame1.hide()
        self.chickSanWid.setStyleSheet("")
    
    def hideWNFrm(self):
        self.orderFrame2.hide()
        self.waltersNuggiesWid.setStyleSheet("")

    def hideWBFrm(self):
        self.orderFrame3.hide()
        self.wangBangWid.setStyleSheet("")
    
    def hideLFFFrm(self):
        self.orderFrame4.hide()
        self.lastFFriesWid.setStyleSheet("")
    
    def hideHBFrm(self):
        self.orderFrame5.hide()
        self.holyBreadWid.setStyleSheet("")
    
    def hideMFrm(self):
        self.orderFrame6.hide()
        self.mackWid.setStyleSheet("")
    
    def hideSWFrm(self):
        self.orderFrame7.hide()
        self.seaWtrWid.setStyleSheet("")
    
    def hideDMFrm(self):
        self.orderFrame8.hide()
        self.diMoxWid.setStyleSheet("")