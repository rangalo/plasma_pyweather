# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/configForm.ui'
#
# Created: Thu Aug  6 09:49:51 2009
#      by: PyQt4 UI code generator 4.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(594, 348)
        self.lblCity = QtGui.QLabel(Dialog)
        self.lblCity.setGeometry(QtCore.QRect(60, 60, 161, 20))
        self.lblCity.setObjectName("lblCity")
        self.lblCountry = QtGui.QLabel(Dialog)
        self.lblCountry.setGeometry(QtCore.QRect(60, 160, 161, 20))
        self.lblCountry.setObjectName("lblCountry")
        self.txtCity = QtGui.QLineEdit(Dialog)
        self.txtCity.setGeometry(QtCore.QRect(260, 60, 301, 24))
        self.txtCity.setObjectName("txtCity")
        self.txtCountry = QtGui.QLineEdit(Dialog)
        self.txtCountry.setGeometry(QtCore.QRect(260, 160, 301, 24))
        self.txtCountry.setObjectName("txtCountry")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCity.setText(QtGui.QApplication.translate("Dialog", "Enter Your City:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCountry.setText(QtGui.QApplication.translate("Dialog", "Enter Your Country:", None, QtGui.QApplication.UnicodeUTF8))

