# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addeditmoviedlg.ui'
#
# Created: Wed Mar  5 23:41:48 2014
#      by: PyQt5 UI code generator 5.1.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddEditMovieDlg(object):
    def setupUi(self, AddEditMovieDlg):
        AddEditMovieDlg.setObjectName("AddEditMovieDlg")
        AddEditMovieDlg.resize(484, 334)
        self.gridlayout = QtWidgets.QGridLayout(AddEditMovieDlg)
        self.gridlayout.setContentsMargins(9, 9, 9, 9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(AddEditMovieDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.NoButton|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox, 4, 4, 1, 2)
        self.titleLineEdit = QtWidgets.QLineEdit(AddEditMovieDlg)
        self.titleLineEdit.setObjectName("titleLineEdit")
        self.gridlayout.addWidget(self.titleLineEdit, 0, 1, 1, 5)
        self.label_5 = QtWidgets.QLabel(AddEditMovieDlg)
        self.label_5.setObjectName("label_5")
        self.gridlayout.addWidget(self.label_5, 2, 0, 1, 2)
        self.notesTextEdit = QtWidgets.QTextEdit(AddEditMovieDlg)
        self.notesTextEdit.setTabChangesFocus(True)
        self.notesTextEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.notesTextEdit.setAcceptRichText(False)
        self.notesTextEdit.setObjectName("notesTextEdit")
        self.gridlayout.addWidget(self.notesTextEdit, 3, 0, 1, 6)
        self.label_2 = QtWidgets.QLabel(AddEditMovieDlg)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.yearSpinBox = QtWidgets.QSpinBox(AddEditMovieDlg)
        self.yearSpinBox.setAlignment(QtCore.Qt.AlignRight)
        self.yearSpinBox.setMaximum(2100)
        self.yearSpinBox.setMinimum(1890)
        self.yearSpinBox.setProperty("value", 1890)
        self.yearSpinBox.setObjectName("yearSpinBox")
        self.gridlayout.addWidget(self.yearSpinBox, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(AddEditMovieDlg)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.minutesSpinBox = QtWidgets.QSpinBox(AddEditMovieDlg)
        self.minutesSpinBox.setAlignment(QtCore.Qt.AlignRight)
        self.minutesSpinBox.setMaximum(720)
        self.minutesSpinBox.setObjectName("minutesSpinBox")
        self.gridlayout.addWidget(self.minutesSpinBox, 1, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(AddEditMovieDlg)
        self.label_4.setObjectName("label_4")
        self.gridlayout.addWidget(self.label_4, 1, 4, 1, 1)
        self.acquiredDateEdit = QtWidgets.QDateEdit(AddEditMovieDlg)
        self.acquiredDateEdit.setAlignment(QtCore.Qt.AlignRight)
        self.acquiredDateEdit.setObjectName("acquiredDateEdit")
        self.gridlayout.addWidget(self.acquiredDateEdit, 1, 5, 1, 1)
        self.label = QtWidgets.QLabel(AddEditMovieDlg)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_5.setBuddy(self.notesTextEdit)
        self.label_2.setBuddy(self.yearSpinBox)
        self.label_3.setBuddy(self.minutesSpinBox)
        self.label_4.setBuddy(self.acquiredDateEdit)
        self.label.setBuddy(self.titleLineEdit)

        self.retranslateUi(AddEditMovieDlg)
        self.buttonBox.accepted.connect(AddEditMovieDlg.accept)
        self.buttonBox.rejected.connect(AddEditMovieDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(AddEditMovieDlg)
        AddEditMovieDlg.setTabOrder(self.titleLineEdit, self.yearSpinBox)
        AddEditMovieDlg.setTabOrder(self.yearSpinBox, self.minutesSpinBox)
        AddEditMovieDlg.setTabOrder(self.minutesSpinBox, self.acquiredDateEdit)
        AddEditMovieDlg.setTabOrder(self.acquiredDateEdit, self.notesTextEdit)
        AddEditMovieDlg.setTabOrder(self.notesTextEdit, self.buttonBox)

    def retranslateUi(self, AddEditMovieDlg):
        _translate = QtCore.QCoreApplication.translate
        AddEditMovieDlg.setWindowTitle(_translate("AddEditMovieDlg", "My Movies - Add Movie"))
        self.label_5.setText(_translate("AddEditMovieDlg", "&Notes:"))
        self.label_2.setText(_translate("AddEditMovieDlg", "&Year:"))
        self.yearSpinBox.setSpecialValueText(_translate("AddEditMovieDlg", "Unknown"))
        self.label_3.setText(_translate("AddEditMovieDlg", "&Minutes:"))
        self.minutesSpinBox.setSpecialValueText(_translate("AddEditMovieDlg", "Unknown"))
        self.label_4.setText(_translate("AddEditMovieDlg", "A&cquired:"))
        self.acquiredDateEdit.setDisplayFormat(_translate("AddEditMovieDlg", "ddd MMM d, yyyy"))
        self.label.setText(_translate("AddEditMovieDlg", "&Title:"))

