import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Арифмометр.ui', self)
        self.lineEdit_3.setEnabled(False)
        self.pushButton.clicked.connect(self.addition)
        self.pushButton_2.clicked.connect(self.subtraction)
        self.pushButton_3.clicked.connect(self.multiplication)

    def addition(self):
        if self.lineEdit.text() == '':
            first_digit = 0
        else:
            first_digit = int(self.lineEdit.text())
        if self.lineEdit_2.text() == '':
            second_digit = 0
        else:
            second_digit = int(self.lineEdit_2.text())
        self.lineEdit_3.setText(str(first_digit + second_digit))

    def subtraction(self):
        if self.lineEdit.text() == '':
            first_digit = 0
        else:
            first_digit = int(self.lineEdit.text())
        if self.lineEdit_2.text() == '':
            second_digit = 0
        else:
            second_digit = int(self.lineEdit_2.text())
        self.lineEdit_3.setText(str(first_digit - second_digit))

    def multiplication(self):
        if self.lineEdit.text() == '':
            first_digit = 0
        else:
            first_digit = int(self.lineEdit.text())
        if self.lineEdit_2.text() == '':
            second_digit = 0
        else:
            second_digit = int(self.lineEdit_2.text())
        self.lineEdit_3.setText(str(first_digit * second_digit))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    ex.setWindowTitle("Арифмометр")
    sys.exit(app.exec())