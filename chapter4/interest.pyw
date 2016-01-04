import sys
from PyQt5.QtWidgets import (QApplication, QSpinBox, QLabel, QDialog,
                             QDoubleSpinBox, QGridLayout)

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        label_principal = QLabel()
        label_principal.setText("Principal:")
        label_rate = QLabel()
        label_rate.setText("Rate:")
        label_years = QLabel()
        label_years.setText("Years:")
        label_amount_name = QLabel()
        label_amount_name.setText("Amount:")
        self.spin_principal = QDoubleSpinBox()
        self.spin_principal.setRange(1000.00, 10000000.00)
        self.spin_principal.setPrefix("$ ")
        self.spin_rate = QDoubleSpinBox()
        self.spin_rate.setRange(0.00, 100.00)
        self.spin_rate.setValue(1.00)
        self.spin_rate.setSuffix(" %")
        self.spin_years = QSpinBox()
        self.spin_years.setRange(1, 50)
        self.spin_years.setSuffix(" years")
        self.label_amount = QLabel()
        self.label_amount.setText("$ 0.00")
        layout = QGridLayout()
        layout.addWidget(label_principal, 0, 0)
        layout.addWidget(label_rate, 1, 0)
        layout.addWidget(label_years, 2, 0)
        layout.addWidget(label_amount_name, 3, 0)
        layout.addWidget(self.spin_principal, 0, 1)
        layout.addWidget(self.spin_rate, 1, 1)
        layout.addWidget(self.spin_years, 2, 1)
        layout.addWidget(self.label_amount, 3, 1)
        self.spin_principal.valueChanged.connect(self.updateAmount)
        self.spin_rate.valueChanged.connect(self.updateAmount)
        self.spin_years.valueChanged.connect(self.updateAmount)
        self.setLayout(layout)
        self.updateAmount()

    def updateAmount(self):
        self.label_amount.setText("{0:.2f}".format(self.spin_principal.value() *
                                 ((1 + (self.spin_rate.value() / 100)) **
                                  self.spin_years.value())))

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
