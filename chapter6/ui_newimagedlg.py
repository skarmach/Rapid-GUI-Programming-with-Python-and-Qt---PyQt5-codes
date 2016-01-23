# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newimagedlg.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewImageDlg(object):
    def setupUi(self, NewImageDlg):
        NewImageDlg.setObjectName("NewImageDlg")
        NewImageDlg.resize(399, 174)
        self.gridLayoutWidget = QtWidgets.QWidget(NewImageDlg)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 391, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.colorLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.colorLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.colorLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.colorLabel.setText("")
        self.colorLabel.setObjectName("colorLabel")
        self.gridLayout.addWidget(self.colorLabel, 5, 1, 1, 1)
        self.colorButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.colorButton.setObjectName("colorButton")
        self.gridLayout.addWidget(self.colorButton, 5, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 3)
        self.brushComboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.brushComboBox.setObjectName("brushComboBox")
        self.gridLayout.addWidget(self.brushComboBox, 3, 1, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.gridLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 7, 1, 1, 2)
        self.widthSpinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.widthSpinBox.setProperty("value", 64)
        self.widthSpinBox.setObjectName("widthSpinBox")
        self.gridLayout.addWidget(self.widthSpinBox, 0, 1, 1, 1)
        self.heightSpinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.heightSpinBox.setProperty("value", 64)
        self.heightSpinBox.setObjectName("heightSpinBox")
        self.gridLayout.addWidget(self.heightSpinBox, 1, 1, 1, 1)
        self.label_2.setBuddy(self.heightSpinBox)
        self.label.setBuddy(self.widthSpinBox)
        self.label_4.setBuddy(self.brushComboBox)

        self.retranslateUi(NewImageDlg)
        self.buttonBox.accepted.connect(NewImageDlg.accept)
        self.buttonBox.rejected.connect(NewImageDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(NewImageDlg)

    def retranslateUi(self, NewImageDlg):
        _translate = QtCore.QCoreApplication.translate
        NewImageDlg.setWindowTitle(_translate("NewImageDlg", "Image Chooser - New Image"))
        self.label_2.setText(_translate("NewImageDlg", "&Height:"))
        self.label.setText(_translate("NewImageDlg", "&Width:"))
        self.label_3.setText(_translate("NewImageDlg", "Color:"))
        self.label_4.setText(_translate("NewImageDlg", "&Brush pattern:"))
        self.colorButton.setText(_translate("NewImageDlg", "&Color..."))
        self.widthSpinBox.setSuffix(_translate("NewImageDlg", " px"))
        self.heightSpinBox.setSuffix(_translate("NewImageDlg", " px"))

