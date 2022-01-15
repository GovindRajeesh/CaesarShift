# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerCdKUkX.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5 import QtCore
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *


class ui(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 700)
        font = QFont()
        font.setFamily(u"Calibri")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color:white")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 781, 61))
        font1 = QFont()
        font1.setPointSize(16)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 100, 381, 451))
        self.plainTextEdit_2 = QPlainTextEdit(self.groupBox)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(10, 20, 361, 281))
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(170, 310, 51, 20))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 310, 151, 21))
        font2 = QFont()
        font2.setPointSize(10)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Encrypt_btn = QPushButton(self.groupBox)
        self.Encrypt_btn.setObjectName(u"Encrypt_btn")
        self.Encrypt_btn.setGeometry(QRect(116, 390, 75, 23))
        self.Encrypt_btn.setStyleSheet(u"border:1px solid rgb(247, 246, 255);\n"
"background-color:rgb(0, 76, 255);\n"
"color:white;\n"
"border-radius:5px;\n")
        self.Decrypt_btn = QPushButton(self.groupBox)
        self.Decrypt_btn.setObjectName(u"Decrypt_btn")
        self.Decrypt_btn.setGeometry(QRect(190, 390, 71, 23))
        self.Decrypt_btn.setStyleSheet(u"border:1px solid rgb(247, 246, 255);\n"
"background-color:rgb(255, 0, 4);\n"
"color:white;\n"
"border-radius:5px;\n")
        self.isWhiteChecked = QCheckBox(self.groupBox)
        self.isWhiteChecked.setObjectName(u"isWhiteChecked")
        self.isWhiteChecked.setGeometry(QRect(110, 340, 181, 17))
        self.isWhiteChecked.setFont(font2)
        self.isWhiteChecked.setChecked(False)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(410, 100, 381, 451))
        self.plainTextEdit = QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(10, 20, 361, 311))
        self.move_bottom = QPushButton(self.groupBox_2)
        self.move_bottom.setObjectName(u"move_bottom")
        self.move_bottom.setGeometry(QRect(20, 350, 351, 41))
        self.move_bottom.setStyleSheet(u"border:1px solid rgb(247, 246, 255);\n"
"background-color:rgb(0, 76, 255);\n"
"color:white;\n"
"border-radius:5px;\n")
        self.status = QLabel(self.centralwidget)
        self.status.setObjectName(u"status")
        self.status.setGeometry(QRect(10, 556, 781, 20))
        font3 = QFont()
        font3.setFamily(u"Calibri")
        font3.setPointSize(9)
        self.status.setFont(font3)
        self.status.setStyleSheet(u"border:1px solid rgb(84, 84, 76);")
        self.aboutBtn = QPushButton(self.centralwidget)
        self.aboutBtn.setObjectName(u"aboutBtn")
        self.aboutBtn.setGeometry(QRect(20, 600, 75, 23))
        self.aboutBtn.setStyleSheet(u"border:0px solid rgb(247, 246, 255);\n"
"background-color:transparent;\n"
"color:rgb(20, 153, 255);\n"
"border-radius:5px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.label.setText(QCoreApplication.translate("MainWindow", u"Caesar Shift", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Input", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Key:", None))
        self.Encrypt_btn.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.Decrypt_btn.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Output", None))
        self.move_bottom.setText(QCoreApplication.translate("MainWindow", u"Move cursor to bottom", None))
        self.isWhiteChecked.setText(QCoreApplication.translate("MainWindow", u"Decrypt/encrypt spaces also", None))
        self.aboutBtn.setText(QCoreApplication.translate("MainWindow", u"About this app", None))
        self.status.setText("")

        
    # retranslateUi
