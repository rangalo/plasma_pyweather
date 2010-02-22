# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/configForm.ui'
#
# Created: Mon Feb 22 21:26:47 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(310, 163)
        self.lblCity = QtGui.QLabel(Dialog)
        self.lblCity.setGeometry(QtCore.QRect(11, 33, 41, 20))
        self.lblCity.setObjectName("lblCity")
        self.lblCountry = QtGui.QLabel(Dialog)
        self.lblCountry.setGeometry(QtCore.QRect(10, 70, 71, 20))
        self.lblCountry.setObjectName("lblCountry")
        self.txtCity = QtGui.QLineEdit(Dialog)
        self.txtCity.setGeometry(QtCore.QRect(80, 30, 171, 24))
        self.txtCity.setObjectName("txtCity")
        self.txtCountry = QtGui.QLineEdit(Dialog)
        self.txtCountry.setGeometry(QtCore.QRect(80, 70, 171, 24))
        self.txtCountry.setObjectName("txtCountry")
        self.lblUnit = QtGui.QLabel(Dialog)
        self.lblUnit.setGeometry(QtCore.QRect(10, 110, 41, 20))
        self.lblUnit.setObjectName("lblUnit")
        self.cmbUnit = QtGui.QComboBox(Dialog)
        self.cmbUnit.setGeometry(QtCore.QRect(80, 110, 81, 23))
        self.cmbUnit.setObjectName("cmbUnit")
        self.cmbUnit.addItem("")
        self.cmbUnit.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCity.setText(QtGui.QApplication.translate("Dialog", "City:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCountry.setText(QtGui.QApplication.translate("Dialog", "Country:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblUnit.setText(QtGui.QApplication.translate("Dialog", "Unit:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbUnit.setItemText(0, QtGui.QApplication.translate("Dialog", "Metric", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbUnit.setItemText(1, QtGui.QApplication.translate("Dialog", "Imperial", None, QtGui.QApplication.UnicodeUTF8))

