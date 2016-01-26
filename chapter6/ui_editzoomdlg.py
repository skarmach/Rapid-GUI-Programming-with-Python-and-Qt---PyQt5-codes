# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editzoomdlg.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditZoomDlg(object):
    def setupUi(self, EditZoomDlg):
        EditZoomDlg.setObjectName("EditZoomDlg")
        EditZoomDlg.resize(218, 111)
        self.buttonBox = QtWidgets.QDialogButtonBox(EditZoomDlg)
        self.buttonBox.setGeometry(QtCore.QRect(30, 70, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(EditZoomDlg)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 201, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widthLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.widthLabel.setObjectName("widthLabel")
        self.gridLayout.addWidget(self.widthLabel, 0, 0, 1, 1)
        self.heightLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.heightLabel.setObjectName("heightLabel")
        self.gridLayout.addWidget(self.heightLabel, 1, 0, 1, 1)
        self.widthSpinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.widthSpinBox.setMaximum(2000)
        self.widthSpinBox.setObjectName("widthSpinBox")
        self.gridLayout.addWidget(self.widthSpinBox, 0, 1, 1, 1)
        self.heightSpinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.heightSpinBox.setMaximum(2000)
        self.heightSpinBox.setObjectName("heightSpinBox")
        self.gridLayout.addWidget(self.heightSpinBox, 1, 1, 1, 1)

        self.retranslateUi(EditZoomDlg)
        self.buttonBox.accepted.connect(EditZoomDlg.accept)
        self.buttonBox.rejected.connect(EditZoomDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(EditZoomDlg)

    def retranslateUi(self, EditZoomDlg):
        _translate = QtCore.QCoreApplication.translate
        EditZoomDlg.setWindowTitle(_translate("EditZoomDlg", "Dialog"))
        self.widthLabel.setText(_translate("EditZoomDlg", "Width"))
        self.heightLabel.setText(_translate("EditZoomDlg", "Height"))

