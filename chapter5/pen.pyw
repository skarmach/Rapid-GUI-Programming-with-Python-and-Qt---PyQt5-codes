import sys
from PyQt5.QtCore import (
    Qt
    )
from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QSpinBox,
    QCheckBox,
    QComboBox,
    QPushButton,
    QHBoxLayout,
    QGridLayout,
    QVBoxLayout,
    QLabel
    )

class PenPropertiesDialog(QDialog):
    def __init__(self, parent=None):
        super(PenPropertiesDialog, self).__init__(parent)
        width_label = QLabel("&Width:")
        self.width_spinbox = QSpinBox()
        width_label.setBuddy(self.width_spinbox)
        self.width_spinbox.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.width_spinbox.setRange(1, 24)
        self.beveled_checkbox = QCheckBox("&Beveled edges")
        style_label = QLabel("&Style:")
        self.style_combobox = QComboBox()
        style_label.setBuddy(self.style_combobox)
        self.style_combobox.addItems(["Solid", "Dashed", "Dotted",
                                      "DashDotted", "DashDotDotted"])
        okButton = QPushButton("&OK")
        cancelButton = QPushButton("Cancel")

        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(okButton)
        buttonLayout.addWidget(cancelButton)
        layout = QGridLayout()
        layout.addWidget(width_label, 0, 0)
        layout.addWidget(self.width_spinbox, 0, 1)
        layout.addWidget(self.beveled_checkbox, 0, 2)
        layout.addWidget(style_label, 1, 0)
        layout.addWidget(self.style_combobox, 1, 1, 1, 2)
        layout.addLayout(buttonLayout, 2, 0, 1, 3)
        self.setLayout(layout)

        okButton.clicked.connect(self.accept)
        cancelButton.clicked.connect(self.reject)

        self.setWindowTitle("Pen Properties")

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.width = 1
        self.beveled = False
        self.style = "Solid"

        pen_button = QPushButton("Set Pen ... (Dumb &class)")
        self.label = QLabel("The pen has not been set")
        self.label.setTextFormat(Qt.RichText)

        layout = QVBoxLayout()
        layout.addWidget(pen_button)
        layout.addWidget(self.label)
        self.setLayout(layout)

        pen_button.clicked.connect(self.setPenProperties)
        self.setWindowTitle("Pen")
        self.updateData()

    def updateData(self):
        bevel = ""
        if self.beveled:
            bevel = "<br>Beveled"
        self.label.setText("Width = {0}<br>Style = {1} {2}".format(
            self.width, self.style, bevel))

    def setPenProperties(self):
        dialog = PenPropertiesDialog(self)
        dialog.width_spinbox.setValue(self.width)
        dialog.beveled_checkbox.setChecked(self.beveled)
        dialog.style_combobox.setCurrentIndex(
            dialog.style_combobox.findText(self.style))
        if dialog.exec_():
            self.width = dialog.width_spinbox.value()
            self.beveled = dialog.beveled_checkbox.isChecked()
            self.style = str(dialog.style_combobox.currentText())
            self.updateData()

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
