from PyQt5.QtCore import (Qt, pyqtSlot, pyqtSignal)
from PyQt5.QtWidgets import (QApplication, QDialog, QDialogButtonBox)
import ui_ticketorderdlg1

MAC = True
try:
    from PyQt5.QtGui import qt_mac_set_native_menubar
except ImportError:
    MAC = False

class TicketOrderDlg1(QDialog,
                      ui_ticketorderdlg1.Ui_TicketOrderDlg1):
    def __init__(self, parent=None):
        super(TicketOrderDlg1, self).__init__(parent)
        self.amount = 0
        self.setupUi(self)
        self.updateUi()
    @pyqtSlot()
    def on_customerLineEdit_textEdited(self):
        self.updateUi()
    @pyqtSlot("double")
    def on_priceDoubleSpinBox_valueChanged(self, value):
        self.updateUi()
    @pyqtSlot("int")
    def on_quantitySpinBox_valueChanged(self):
        self.updateUi()
    def updateUi(self):
        self.amount = (self.priceDoubleSpinBox.value() *
                       self.quantitySpinBox.value())
        self.amountLineEdit.setText("$ {:-8.2f}".format(self.amount))
        enable = bool(self.customerLineEdit.text() and self.amount > 0)
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(enable)
    def result(self):
        return (self.customerLineEdit.text(),
                self.whenDateTimeEdit.dateTime(),
                self.priceDoubleSpinBox.value(),
                self.quantitySpinBox.value(),
                self.amount)
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    form = TicketOrderDlg1()
    form.show()
    app.exec_()
    print(form.result())
