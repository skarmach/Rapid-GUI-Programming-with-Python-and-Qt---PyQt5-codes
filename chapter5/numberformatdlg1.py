from PyQt5.QtCore import (Qt)
from PyQt5.QtWidgets import (QDialog,
                             QCheckBox,
                             QDialogButtonBox,
                             QGridLayout,
                             QLabel,
                             QLineEdit,
                             QSpinBox,
                             QMessageBox
                             )

class NumberFormatDlg(QDialog):
    def __init__(self, format, parent=None):
        super(NumberFormatDlg, self).__init__(parent)

        thousandsLabel = QLabel("&Thousands separator")
        self.thousandsEdit = QLineEdit(format["thousandsseparator"])
        thousandsLabel.setBuddy(self.thousandsEdit)
        decimalMarkerLabel = QLabel("Decimal &marker")
        self.decimalMarkerEdit = QLineEdit(format["decimalmarker"])
        decimalMarkerLabel.setBuddy(self.decimalMarkerEdit)
        decimalPlacesLabel = QLabel("&Decimal places")
        self.decimalPlacesSpinBox = QSpinBox()
        decimalPlacesLabel.setBuddy(self.decimalPlacesSpinBox)
        self.decimalPlacesSpinBox.setRange(0, 6)
        self.decimalPlacesSpinBox.setValue(format["decimalplaces"])
        self.redNegativesCheckBox = QCheckBox("&Red negative numbers")
        self.redNegativesCheckBox.setChecked(format["rednegatives"])

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok|
                                     QDialogButtonBox.Cancel)
        self.format = format.copy()

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

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        self.setWindowTitle("Set Number Format (Modal)")

    def accept(self):
        class ThousandsError(Exception): pass
        class DecimalError(Exception): pass
        Punctuation = frozenset(" ,;:.")

        thousands = str(self.thousandsEdit.text())
        decimal = str(self.decimalMarkerEdit.text())
        try:
            if len(decimal) == 0:
                raise DecimalError("Decimal marker may not be empty.")

            if len(thousands) > 1:
                raise ThousandsError("Thousands separator may only be "
                                     "empty or one charactor.")

            if len(decimal) > 1:
                raise DecimalError("Decimal marker must be one "
                                   "character.")

            if thousands == decimal:
                raise ThousandsError("Thousands separator and decimal "
                                     "marker must be different.")

            if thousands and thousands not in Punctuation:
                raise ThousandsError("Thousands separator must be a "
                                     "punctuation symbol.")

            if decimal not in Punctuation:
                raise DecimalError("Decimal separator must be a "
                                   "punctuation symbol.")
        except ThousandsError as err:
            QMessageBox.warning(self, "Thousands Separator Error",
                                str(err))
            self.thousandsEdit.selectAll()
            self.thousandsEdit.setFocus()
            return
        except DecimalError as err:
            QMessageBox.warning(self, "Decimal Marker Error", str(err))
            self.decimalMarkerEdit.selectAll()
            self.decimalMarkerEdit.setFocus()
            return

        self.format["thousandsseparator"] = thousands
        self.format["decimalmarker"] = decimal
        self.format["decimalplaces"] = (self.decimalPlacesSpinBox.value())
        self.format["rednegatives"] = (self.redNegativesCheckBox.isChecked())
        QDialog.accept(self)

    def numberFormat(self):
        return self.format
