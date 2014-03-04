# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ticketorderdlg1.ui'
#
# Created: Tue Mar  4 17:36:40 2014
#      by: PyQt5 UI code generator 5.1.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TicketOrderDlg(object):
    def setupUi(self, TicketOrderDlg):
        TicketOrderDlg.setObjectName("TicketOrderDlg")
        TicketOrderDlg.resize(379, 140)
        self.gridlayout = QtWidgets.QGridLayout(TicketOrderDlg)
        self.gridlayout.setContentsMargins(9, 9, 9, 9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(TicketOrderDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.NoButton|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox, 4, 0, 1, 6)
        spacerItem = QtWidgets.QSpacerItem(361, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem, 3, 0, 1, 6)
        self.amountLabel = QtWidgets.QLabel(TicketOrderDlg)
        self.amountLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.amountLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.amountLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.amountLabel.setObjectName("amountLabel")
        self.gridlayout.addWidget(self.amountLabel, 2, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(TicketOrderDlg)
        self.label_4.setObjectName("label_4")
        self.gridlayout.addWidget(self.label_4, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(TicketOrderDlg)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(TicketOrderDlg)
        self.label_5.setObjectName("label_5")
        self.gridlayout.addWidget(self.label_5, 2, 4, 1, 1)
        self.priceSpinBox = QtWidgets.QDoubleSpinBox(TicketOrderDlg)
        self.priceSpinBox.setAlignment(QtCore.Qt.AlignRight)
        self.priceSpinBox.setMaximum(5000.0)
        self.priceSpinBox.setObjectName("priceSpinBox")
        self.gridlayout.addWidget(self.priceSpinBox, 2, 1, 1, 1)
        self.quantitySpinBox = QtWidgets.QSpinBox(TicketOrderDlg)
        self.quantitySpinBox.setAlignment(QtCore.Qt.AlignRight)
        self.quantitySpinBox.setMaximum(50)
        self.quantitySpinBox.setMinimum(1)
        self.quantitySpinBox.setProperty("value", 1)
        self.quantitySpinBox.setObjectName("quantitySpinBox")
        self.gridlayout.addWidget(self.quantitySpinBox, 2, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(81, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem1, 1, 4, 1, 2)
        self.label_2 = QtWidgets.QLabel(TicketOrderDlg)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.whenDateTimeEdit = QtWidgets.QDateTimeEdit(TicketOrderDlg)
        self.whenDateTimeEdit.setObjectName("whenDateTimeEdit")
        self.gridlayout.addWidget(self.whenDateTimeEdit, 1, 1, 1, 2)
        self.customerLineEdit = QtWidgets.QLineEdit(TicketOrderDlg)
        self.customerLineEdit.setObjectName("customerLineEdit")
        self.gridlayout.addWidget(self.customerLineEdit, 0, 1, 1, 5)
        self.label = QtWidgets.QLabel(TicketOrderDlg)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4.setBuddy(self.quantitySpinBox)
        self.label_3.setBuddy(self.priceSpinBox)
        self.label_2.setBuddy(self.whenDateTimeEdit)
        self.label.setBuddy(self.customerLineEdit)

        self.retranslateUi(TicketOrderDlg)
        self.buttonBox.accepted.connect(TicketOrderDlg.accept)
        self.buttonBox.rejected.connect(TicketOrderDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(TicketOrderDlg)
        TicketOrderDlg.setTabOrder(self.customerLineEdit, self.whenDateTimeEdit)
        TicketOrderDlg.setTabOrder(self.whenDateTimeEdit, self.priceSpinBox)
        TicketOrderDlg.setTabOrder(self.priceSpinBox, self.quantitySpinBox)
        TicketOrderDlg.setTabOrder(self.quantitySpinBox, self.buttonBox)

    def retranslateUi(self, TicketOrderDlg):
        _translate = QtCore.QCoreApplication.translate
        TicketOrderDlg.setWindowTitle(_translate("TicketOrderDlg", "Ticket Order #1"))
        self.amountLabel.setText(_translate("TicketOrderDlg", "$"))
        self.label_4.setText(_translate("TicketOrderDlg", "&Quantity:"))
        self.label_3.setText(_translate("TicketOrderDlg", "&Price:"))
        self.label_5.setText(_translate("TicketOrderDlg", "Amount"))
        self.priceSpinBox.setPrefix(_translate("TicketOrderDlg", "$ "))
        self.label_2.setText(_translate("TicketOrderDlg", "&When:"))
        self.label.setText(_translate("TicketOrderDlg", "&Customer:"))

