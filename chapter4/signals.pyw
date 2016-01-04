import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QDial, QSpinBox,
                             QHBoxLayout)

class Form(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        dial = QDial()
        dial.setNotchesVisible(True)
        spinbox = QSpinBox()

        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinbox)
        self.setLayout(layout)
        dial.valueChanged.connect(spinbox.setValue)
        spinbox.valueChanged.connect(dial.setValue)
        self.setWindowTitle("Signals and Slots")

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
