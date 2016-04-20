# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'webTextDialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_WebTextDialog(object):
    def setupUi(self, WebTextDialog):
        WebTextDialog.setObjectName(_fromUtf8("WebTextDialog"))
        WebTextDialog.resize(778, 473)
        self.gridLayout = QtGui.QGridLayout(WebTextDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(WebTextDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.urlEdit = QtGui.QLineEdit(WebTextDialog)
        self.urlEdit.setObjectName(_fromUtf8("urlEdit"))
        self.horizontalLayout.addWidget(self.urlEdit)
        self.urlButton = QtGui.QPushButton(WebTextDialog)
        self.urlButton.setObjectName(_fromUtf8("urlButton"))
        self.horizontalLayout.addWidget(self.urlButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(WebTextDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.mainTextBrowser = QtGui.QTextBrowser(WebTextDialog)
        self.mainTextBrowser.setObjectName(_fromUtf8("mainTextBrowser"))
        self.verticalLayout.addWidget(self.mainTextBrowser)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_3 = QtGui.QLabel(WebTextDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.tableWidget = QtGui.QTableWidget(WebTextDialog)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        self.cancelButton = QtGui.QPushButton(WebTextDialog)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.gridLayout.addWidget(self.cancelButton, 0, 1, 1, 1)
        self.label.setBuddy(self.urlEdit)
        self.label_2.setBuddy(self.mainTextBrowser)
        self.label_3.setBuddy(self.tableWidget)

        self.retranslateUi(WebTextDialog)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), WebTextDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(WebTextDialog)

    def retranslateUi(self, WebTextDialog):
        WebTextDialog.setWindowTitle(_translate("WebTextDialog", "Dialog", None))
        self.label.setText(_translate("WebTextDialog", "url：", None))
        self.urlButton.setText(_translate("WebTextDialog", "确定", None))
        self.label_2.setText(_translate("WebTextDialog", "文本：", None))
        self.label_3.setText(_translate("WebTextDialog", "其他", None))
        self.cancelButton.setText(_translate("WebTextDialog", "退出", None))

