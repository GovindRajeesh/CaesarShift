from PyQt5.QtCore import (QCoreApplication, QMetaObject,
    QRect, QSize, Qt)
from PyQt5.QtGui import (QFont)
from PyQt5.QtWidgets import *
from os import system

class ui(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(432, 318)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.heading = QLabel(self.centralwidget)
        self.heading.setObjectName(u"heading")
        self.heading.setEnabled(True)
        self.heading.setGeometry(QRect(10, 0, 411, 41))
        font = QFont()
        font.setPointSize(16)
        self.heading.setFont(font)
        self.heading.setAlignment(Qt.AlignCenter)
        self.heading_2 = QLabel(self.centralwidget)
        self.heading_2.setObjectName(u"heading_2")
        self.heading_2.setEnabled(True)
        self.heading_2.setGeometry(QRect(10, 210, 411, 41))
        font1 = QFont()
        font1.setPointSize(10)
        self.heading_2.setFont(font1)
        self.heading_2.setAlignment(Qt.AlignCenter)
        self.heading_3 = QLabel(self.centralwidget)
        self.heading_3.setObjectName(u"heading_3")
        self.heading_3.setEnabled(True)
        self.heading_3.setGeometry(QRect(10, 250, 411, 41))
        self.heading_3.setFont(font1)
        self.heading_3.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 30, 431, 131))
        self.label.setMinimumSize(QSize(0, 81))
        self.label.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 140, 431, 23))
        self.pushButton.setStyleSheet(u"background-color:transparent;\n"
"color:rgb(0, 153, 255)")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.heading.setText(QCoreApplication.translate("MainWindow", u"Caesar Shift", None))
        self.heading_2.setText(QCoreApplication.translate("MainWindow", u"A Govind Rajeesh Production", None))
        self.heading_3.setText(QCoreApplication.translate("MainWindow", u"\u00a9 2021-present  Caesar shift", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"This program encrypts/decrypts a string using caesar shift method.\n"
" This program is written in python", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Click here to know about caesar shift method.", None))

        self.pushButton.clicked.connect(lambda:system("start https://en.wikipedia.org/wiki/Caesar_cipher"))
    # retranslateUi
