import createOrder
from PyQt5 import QtCore, QTWidgets

class createOrderAttached(createOrder.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUI(self)
        self.show
        
if __name__ == "__main__":
    UI = createOrderAttached()
    import sys
    app = QTWidgets.QApplication(sys.argv)
    manager_MainWindow = createOrderAttached()
    sys.exit(app.exec_())