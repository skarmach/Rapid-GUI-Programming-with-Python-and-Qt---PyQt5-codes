import sys
from math import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QApplication, QTextBrowser,
                             QLineEdit, QVBoxLayout, QDialog)

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.browser = QTextBrowser()
        self.lineedit = QLineEdit("Type an expression and <Enter>")
        self.lineedit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.lineedit.setFocus()
        self.lineedit.returnPressed.connect(self.updateUi)
        self.setWindowTitle("Calculate")

    def updateUi(self):
        try:
            text = self.lineedit.text()
            self.browser.append("{0} = <b>{1}</b>".format(text, eval(text)))
        except:
            self.browser.append(
                "<font color=red>{0} is invalid!</font>".format(text))

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
