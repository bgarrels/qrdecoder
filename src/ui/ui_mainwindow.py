# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/resources/mainwindow.ui'
#
# Created: Sat Jan 07 02:56:05 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(500, 156)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEdit_location = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_location.setMinimumSize(QtCore.QSize(300, 20))
        self.lineEdit_location.setAcceptDrops(False)
        self.lineEdit_location.setObjectName(_fromUtf8("lineEdit_location"))
        self.horizontalLayout_2.addWidget(self.lineEdit_location)
        self.pushButton_browse = QtGui.QPushButton(self.groupBox)
        self.pushButton_browse.setObjectName(_fromUtf8("pushButton_browse"))
        self.horizontalLayout_2.addWidget(self.pushButton_browse)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 2, 1)
        self.pushButton_about = QtGui.QPushButton(self.centralwidget)
        self.pushButton_about.setObjectName(_fromUtf8("pushButton_about"))
        self.gridLayout_2.addWidget(self.pushButton_about, 0, 1, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit_code = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_code.setEnabled(True)
        self.lineEdit_code.setMinimumSize(QtCore.QSize(300, 0))
        self.lineEdit_code.setAcceptDrops(False)
        self.lineEdit_code.setAutoFillBackground(False)
        self.lineEdit_code.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_code.setEchoMode(QtGui.QLineEdit.Normal)
        self.lineEdit_code.setReadOnly(True)
        self.lineEdit_code.setObjectName(_fromUtf8("lineEdit_code"))
        self.horizontalLayout.addWidget(self.lineEdit_code)
        self.pushButton_copy = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_copy.setEnabled(False)
        self.pushButton_copy.setObjectName(_fromUtf8("pushButton_copy"))
        self.horizontalLayout.addWidget(self.pushButton_copy)
        self.gridLayout_2.addWidget(self.groupBox_2, 2, 0, 2, 1)
        self.pushButton_clear = QtGui.QPushButton(self.centralwidget)
        self.pushButton_clear.setEnabled(True)
        self.pushButton_clear.setObjectName(_fromUtf8("pushButton_clear"))
        self.gridLayout_2.addWidget(self.pushButton_clear, 2, 1, 1, 1)
        self.pushButton_exit = QtGui.QPushButton(self.centralwidget)
        self.pushButton_exit.setObjectName(_fromUtf8("pushButton_exit"))
        self.gridLayout_2.addWidget(self.pushButton_exit, 3, 1, 1, 1)
        self.pushButton_decode = QtGui.QPushButton(self.centralwidget)
        self.pushButton_decode.setObjectName(_fromUtf8("pushButton_decode"))
        self.gridLayout_2.addWidget(self.pushButton_decode, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "qrDecoder - v0.1", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Image Location", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_browse.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_about.setText(QtGui.QApplication.translate("MainWindow", "&About...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "QR Code", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_copy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_clear.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_exit.setText(QtGui.QApplication.translate("MainWindow", "&Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_decode.setText(QtGui.QApplication.translate("MainWindow", "&Decode", None, QtGui.QApplication.UnicodeUTF8))

import images_rc
