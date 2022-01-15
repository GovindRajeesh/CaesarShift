import typing
from PyQt5 import QtWidgets, QtCore,QtGui
from sys import argv,exit

from PyQt5.QtCore import QSize,Qt


def uiApp():
    app=QtWidgets.QApplication(argv)
    app.setStyleSheet("""QScrollBar
                             {
                             background : grey;
                             width:10px;
                             }
                             QScrollBar::handle
                             {
                             background : lightgrey;
                             }
                             QScrollBar,QScrollBar::handle{
                                 border-radius:2px;
                             }
                             QScrollBar::handle::pressed
                             {
                             background : grey;
                             }"""
                             )
    return app

def createWindow():
    win=QtWidgets.QMainWindow()
    win.setWindowTitle("CaesarShift")
    win.setGeometry(100,100,200,200)
    win.setStyleSheet(u"background-color:rgb(255, 255, 255)")
    win.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
    
    return win