import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class test_PyQt(QDialog):
    def __init__(self):
        super(test_PyQt, self).__init__()
        loadUi('/home/wanchat/Python/test_ui.ui', self)
        self.setWindowTitle('test_PyQt')
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
    @pyqtSlot()
     def on_pushButton_clicked(self):
        self.label_1.setText('Welcome :' + self.lineEdit.text())

app = QApplication(sys.argv)
widget = test_PyQt()
widget.show()
sys.exit(app.exec_())

