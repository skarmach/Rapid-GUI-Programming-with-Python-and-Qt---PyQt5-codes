import math
import random
import string
import sys
from PyQt5.QtCore import (Qt)
from PyQt5.QtWidgets import (
    QApplication, QDialog, QHBoxLayout, QPushButton,
    QTableWidget, QTableWidgetItem, QVBoxLayout
    )
from PyQt5.QtGui import (QBrush)
import numberformatdlg1

class Form(QDialog):
    X_MAX = 26
    Y_MAX = 60
    
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.numberFormatDlg = None
        self.format = dict(thousandsseparator = ",",
                           decimalmarker = ".",
                           decimalplaces = 2,
                           rednegatives = False)
        self.numbers = {}
        for x in range(self.X_MAX):
            for y in range(self.Y_MAX):
                self.numbers[(x, y)] = (10000 * random.random()) - 5000

        self.table = QTableWidget()
        formatButton1 = QPushButton("Set Number Format... (&Modal)")

        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(formatButton1)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addLayout(buttonLayout)
        self.setLayout(layout)

        formatButton1.clicked.connect(self.setNumberFormat1)

        self.setWindowTitle("Numbers")
        self.refreshTable()

    def refreshTable(self):
        self.table.clear()
        self.table.setColumnCount(self.X_MAX)
        self.table.setRowCount(self.Y_MAX)
        self.table.setHorizontalHeaderLabels(
            list(string.ascii_uppercase))
        for x in range(self.X_MAX):
            for y in range(self.Y_MAX):
                fraction, whole = math.modf(self.numbers[(x, y)])
                sign = "-" if whole < 0 else ""
                whole = "{0}".format(int(math.floor(abs(whole))))
                digits = []
                for i, digit in enumerate(reversed(whole)):
                    if i and i % 3 == 0:
                        digits.insert(0, self.format["thousandsseparator"])
                    digits.insert(0, digit)
                if self.format["decimalplaces"]:
                    fraction = "{0:.7f}".format(abs(fraction))
                    fraction = (self.format["decimalmarker"] +
                                fraction[2:self.format["decimalplaces"] + 2])
                else:
                    fraction = ""
                text = "{0}{1}{2}".format(sign, "".join(digits), fraction)
                item = QTableWidgetItem(text)
                item.setTextAlignment(Qt.AlignRight|
                                      Qt.AlignVCenter)
                if sign and self.format["rednegatives"]:
                    item.setBackground(QBrush(Qt.red))
                self.table.setItem(y, x, item)

    def setNumberFormat1(self):
        dialog = numberformatdlg1.NumberFormatDlg(self.format, self)
        if dialog.exec_():
            self.format = dialog.numberFormat()
            self.refreshTable()

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
