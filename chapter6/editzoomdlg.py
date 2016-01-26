from PyQt5.QtWidgets import (QDialog,  QApplication)
import ui_editzoomdlg
class EditZoomDlg(QDialog, ui_editzoomdlg.Ui_EditZoomDlg):
    def __init__(self, width, height, parent=None):
        super(EditZoomDlg, self).__init__(parent)
        self.setupUi(self)
        self.w = width
        self.h = height
        self.widthSpinBox.setValue(width)
        self.heightSpinBox.setValue(height)
        #self.buttonBox.accepted.connect(self.accept)
        #self.buttonBox.rejected.connect(self.reject)
    def accept(self):
        self.w = (self.widthSpinBox.value())
        self.h = (self.heightSpinBox.value())
        QDialog.accept(self)
    def size(self):
        return (self.w, self.h)
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    form = EditZoomDlg(50, 100)
    form.show()
    app.exec_()
    print(form.size())
    
