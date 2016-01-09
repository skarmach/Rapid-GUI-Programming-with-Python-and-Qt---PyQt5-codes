from PyQt5.QtCore import (Qt, QRegExp, pyqtSignal)
from PyQt5.QtWidgets import (QDialog,
                             QCheckBox,
                             QDialogButtonBox,
                             QGridLayout,
                             QLabel,
                             QLineEdit,
                             QSpinBox,
                             QMessageBox
                             )

from PyQt5.QtGui import (QRegExpValidator)

class NumberFormatDlg(QDialog):
    applied = pyqtSignal()
    
    def __init__(self, format, parent=None):
        super(NumberFormatDlg, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)

        punctuationRe = QRegExp(r"[ ,;:.]")

        thousandsLabel = QLabel("&Thousands separator")
        self.thousandsEdit = QLineEdit(format["thousandsseparator"])
        thousandsLabel.setBuddy(self.thousandsEdit)
        self.thousandsEdit.setMaxLength(1)
        self.thousandsEdit.setValidator(
            QRegExpValidator(punctuationRe, self))

        decimalMarkerLabel = QLabel("Decimal &marker")
        self.decimalMarkerEdit = QLineEdit(format["decimalmarker"])
        decimalMarkerLabel.setBuddy(self.decimalMarkerEdit)
        self.decimalMarkerEdit.setMaxLength(1)
        self.decimalMarkerEdit.setValidator(
            QRegExpValidator(punctuationRe, self))

        decimalPlacesLabel = QLabel("&Decimal places")
        self.decimalPlacesSpinBox = QSpinBox()
        decimalPlacesLabel.setBuddy(self.decimalPlacesSpinBox)
        self.decimalPlacesSpinBox.setRange(0, 6)
        self.decimalPlacesSpinBox.setValue(format["decimalplaces"])

        self.redNegativesCheckBox = QCheckBox("&Red negative numbers")
        self.redNegativesCheckBox.setChecked(format["rednegatives"])

        buttonBox = QDialogButtonBox(QDialogButtonBox.Apply|
                                     QDialogButtonBox.Close)

        self.format = format

        grid = QGridLayout()
        grid.addWidget(thousandsLabel, 0, 0)
        grid.addWidget(self.thousandsEdit, 0, 1)
        grid.addWidget(decimalMarkerLabel, 1, 0)
        grid.addWidget(self.decimalMarkerEdit, 1, 1)
        grid.addWidget(decimalPlacesLabel, 2, 0)
        grid.addWidget(self.decimalPlacesSpinBox, 2, 1)
        grid.addWidget(self.redNegativesCheckBox, 3, 0, 1, 2)
        grid.addWidget(buttonBox, 4, 0, 1, 2)
        self.setLayout(grid)

        buttonBox.button(QDialogButtonBox.Apply).clicked.connect(self.apply)
        buttonBox.rejected.connect(self.reject)
        self.setWindowTitle("Set Number Format (Modal)")

    def apply(self):
        thousands = str(self.thousandsEdit.text())
        decimal = str(self.decimalMarkerEdit.text())
        if thousands == decimal:
            QMessageBox.warning(
                self,
                "Format Error",
                "The thousands separator and decimal marker "
                "must be different.")
            self.thousandsEdit.selectAll()
            self.thousandsEdit.setFocus()
            return
        if len(decimal) == 0:
            QMessageBox.warning(
                self,
                "Format Error",
                "The decimal marker may not be empty.")
            self.decimalMarkerEdit.selectAll()
            self.decimalMarkerEdit.setFocus()
            return

        self.format["thousandsseparator"] = thousands
        self.format["decimalmarker"] = decimal
        self.format["decimalplaces"] = (self.decimalPlacesSpinBox.value())
        self.format["rednegatives"] = (self.redNegativesCheckBox.isChecked())
        self.applied.emit()

