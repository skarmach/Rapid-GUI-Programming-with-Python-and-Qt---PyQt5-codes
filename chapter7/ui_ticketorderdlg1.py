# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ticketorderdlg1.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TicketOrderDlg1(object):
    def setupUi(self, TicketOrderDlg1):
        TicketOrderDlg1.setObjectName("TicketOrderDlg1")
        TicketOrderDlg1.resize(360, 127)
        self.widget = QtWidgets.QWidget(TicketOrderDlg1)
        self.widget.setGeometry(QtCore.QRect(10, 10, 341, 111))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.priceDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.widget)
        self.priceDoubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.priceDoubleSpinBox.setMaximum(5000.0)
        self.priceDoubleSpinBox.setObjectName("priceDoubleSpinBox")
        self.gridLayout.addWidget(self.priceDoubleSpinBox, 2, 1, 2, 1)
        self.quantitySpinBox = QtWidgets.QSpinBox(self.widget)
        self.quantitySpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.quantitySpinBox.setObjectName("quantitySpinBox")
        self.gridLayout.addWidget(self.quantitySpinBox, 2, 3, 2, 1)
        self.customerLineEdit = QtWidgets.QLineEdit(self.widget)
        self.customerLineEdit.setObjectName("customerLineEdit")
        self.gridLayout.addWidget(self.customerLineEdit, 0, 1, 1, 5)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 2, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 2, 2, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 4, 2, 1)
        self.amountLineEdit = QtWidgets.QLineEdit(self.widget)
        self.amountLineEdit.setEnabled(False)
        self.amountLineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.amountLineEdit.setObjectName("amountLineEdit")
        self.gridLayout.addWidget(self.amountLineEdit, 2, 5, 2, 1)
        self.whenDateTimeEdit = QtWidgets.QDateTimeEdit(self.widget)
        self.whenDateTimeEdit.setObjectName("whenDateTimeEdit")
        self.gridLayout.addWidget(self.whenDateTimeEdit, 1, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.customerLineEdit)
        self.label_2.setBuddy(self.whenDateTimeEdit)
        self.label_3.setBuddy(self.priceDoubleSpinBox)
        self.label_4.setBuddy(self.quantitySpinBox)
        self.label_5.setBuddy(self.amountLineEdit)

        self.retranslateUi(TicketOrderDlg1)
        self.buttonBox.accepted.connect(TicketOrderDlg1.accept)
        self.buttonBox.rejected.connect(TicketOrderDlg1.reject)
        QtCore.QMetaObject.connectSlotsByName(TicketOrderDlg1)

    def retranslateUi(self, TicketOrderDlg1):
        _translate = QtCore.QCoreApplication.translate
        TicketOrderDlg1.setWindowTitle(_translate("TicketOrderDlg1", "Dialog"))
        self.label.setText(_translate("TicketOrderDlg1", "&Customer"))
        self.label_2.setText(_translate("TicketOrderDlg1", "&When"))
        self.priceDoubleSpinBox.setPrefix(_translate("TicketOrderDlg1", "$ "))
        self.label_3.setText(_translate("TicketOrderDlg1", "&Price"))
        self.label_4.setText(_translate("TicketOrderDlg1", "&Quantity"))
        self.label_5.setText(_translate("TicketOrderDlg1", "Amount"))

