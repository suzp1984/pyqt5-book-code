# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newimagedlg.ui'
#
# Created: Mon Mar  3 16:54:02 2014
#      by: PyQt5 UI code generator 5.1.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewImageDlg(object):
    def setupUi(self, NewImageDlg):
        NewImageDlg.setObjectName("NewImageDlg")
        NewImageDlg.resize(287, 214)
        self.gridlayout = QtWidgets.QGridLayout(NewImageDlg)
        self.gridlayout.setContentsMargins(9, 9, 9, 9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(NewImageDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.NoButton|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox, 5, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(269, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem, 4, 0, 1, 3)
        self.colorLabel = QtWidgets.QLabel(NewImageDlg)
        self.colorLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.colorLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.colorLabel.setText("")
        self.colorLabel.setScaledContents(True)
        self.colorLabel.setObjectName("colorLabel")
        self.gridlayout.addWidget(self.colorLabel, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(NewImageDlg)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.colorButton = QtWidgets.QPushButton(NewImageDlg)
        self.colorButton.setObjectName("colorButton")
        self.gridlayout.addWidget(self.colorButton, 3, 2, 1, 1)
        self.brushComboBox = QtWidgets.QComboBox(NewImageDlg)
        self.brushComboBox.setObjectName("brushComboBox")
        self.gridlayout.addWidget(self.brushComboBox, 2, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(NewImageDlg)
        self.label_4.setObjectName("label_4")
        self.gridlayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(NewImageDlg)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(NewImageDlg)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.heightSpinBox = QtWidgets.QSpinBox(NewImageDlg)
        self.heightSpinBox.setAlignment(QtCore.Qt.AlignRight)
        self.heightSpinBox.setMaximum(512)
        self.heightSpinBox.setMinimum(8)
        self.heightSpinBox.setSingleStep(4)
        self.heightSpinBox.setProperty("value", 64)
        self.heightSpinBox.setObjectName("heightSpinBox")
        self.gridlayout.addWidget(self.heightSpinBox, 1, 1, 1, 1)
        self.widthSpinBox = QtWidgets.QSpinBox(NewImageDlg)
        self.widthSpinBox.setAlignment(QtCore.Qt.AlignRight)
        self.widthSpinBox.setMaximum(512)
        self.widthSpinBox.setMinimum(8)
        self.widthSpinBox.setSingleStep(4)
        self.widthSpinBox.setProperty("value", 64)
        self.widthSpinBox.setObjectName("widthSpinBox")
        self.gridlayout.addWidget(self.widthSpinBox, 0, 1, 1, 1)
        self.label_4.setBuddy(self.brushComboBox)
        self.label.setBuddy(self.widthSpinBox)
        self.label_2.setBuddy(self.heightSpinBox)

        self.retranslateUi(NewImageDlg)
        self.buttonBox.accepted.connect(NewImageDlg.accept)
        self.buttonBox.rejected.connect(NewImageDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(NewImageDlg)
        NewImageDlg.setTabOrder(self.widthSpinBox, self.heightSpinBox)
        NewImageDlg.setTabOrder(self.heightSpinBox, self.brushComboBox)
        NewImageDlg.setTabOrder(self.brushComboBox, self.colorButton)
        NewImageDlg.setTabOrder(self.colorButton, self.buttonBox)

    def retranslateUi(self, NewImageDlg):
        _translate = QtCore.QCoreApplication.translate
        NewImageDlg.setWindowTitle(_translate("NewImageDlg", "Image Chooser - New Image"))
        self.label_3.setText(_translate("NewImageDlg", "Color"))
        self.colorButton.setText(_translate("NewImageDlg", "&Color..."))
        self.label_4.setText(_translate("NewImageDlg", "&Brush pattern:"))
        self.label.setText(_translate("NewImageDlg", "&Width:"))
        self.label_2.setText(_translate("NewImageDlg", "&Height:"))
        self.heightSpinBox.setSuffix(_translate("NewImageDlg", " px"))
        self.widthSpinBox.setSuffix(_translate("NewImageDlg", " px"))

