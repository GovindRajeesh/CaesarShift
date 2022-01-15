from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget
from tools.ui import *
from tools import shifts
from views import home,about
from sys import argv,exit
from os import path

aboutwin=None

def mainProcess(**kwargs):
    # Initialize ui
    app=uiApp()
    window=createWindow()

    # Display the home page
    homeUi=home.ui()
    homeUi.setupUi(window)

    def shiftBtnsHandle(type):
        try:
            key=int(homeUi.lineEdit.text())

            if type=="encrypt":
                m=shifts.encrypt(homeUi.plainTextEdit_2.toPlainText(),key,white=homeUi.isWhiteChecked.isChecked())
                homeUi.plainTextEdit.setPlainText(m)
                homeUi.plainTextEdit.setEnabled(True)
            elif type=="decrypt":
                m=shifts.decrypt(homeUi.plainTextEdit_2.toPlainText(),key,white=homeUi.isWhiteChecked.isChecked())
                homeUi.plainTextEdit.setPlainText(m)
                homeUi.plainTextEdit.setEnabled(True)

            homeUi.status.setText(f"Successfully {type}ed with key {key}.")

        except ValueError:
            homeUi.status.setText("Invalid number ! A key should be a number without decimals.")


    homeUi.status.setText("Ready to use")

    aboutwin=aboutWindow()
    aboutwin.closeEvent=lambda e:aboutwin.hide()

    homeUi.Encrypt_btn.clicked.connect(lambda:shiftBtnsHandle("encrypt"))
    homeUi.Decrypt_btn.clicked.connect(lambda:shiftBtnsHandle("decrypt"))
    homeUi.move_bottom.clicked.connect(lambda:(homeUi.plainTextEdit.moveCursor(QtGui.QTextCursor.End),homeUi.plainTextEdit.setFocus()))
    homeUi.aboutBtn.clicked.connect(lambda:(
    aboutwin.hide(),aboutwin.show()))
    
    if "txt" in tuple(kwargs.keys()) and kwargs["txt"] is not None:
        homeUi.plainTextEdit_2.setPlainText(kwargs["txt"])
        homeUi.status.setText(f"Text loaded from the file {kwargs['file']}. Encrypt or decrypt")

    return {"window":window,"uiapp":app}

def aboutWindow():
    win=createWindow()
    about.ui().setupUi(win)

    return win



if __name__=="__main__":
    main=None

    if len(argv) != 1:
        if path.lexists(argv[1]) and path.isfile(argv[1]):
            txt=open(argv[1],"r").read()
            main=mainProcess(txt=txt,file=argv[1])

    if main is None:
        main=mainProcess()

    aboutwin=createWindow()

    main["window"].show()
    main["window"].closeEvent=lambda e:(aboutwin.close(),exit()
    )
    main["uiapp"].exec_()