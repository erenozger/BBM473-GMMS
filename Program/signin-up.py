# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signin-up.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from signin import Ui_MainWindow
from signup import *
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from main import *
from news import *
from addcontent import *
from addgame import *
from addmovie import *
from addmusic import *
from addseries import *
from statistics import *
from delete import *
from single import *
from singlenews import *

class Ui_LoginWindow(object):

    def signIn(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        LoginWindow.hide()

    def signUp(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_LoginWindow2()
        self.ui.setupUi(self.window)
        self.window.show()
        LoginWindow.hide()

    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(510, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginWindow.sizePolicy().hasHeightForWidth())
        LoginWindow.setSizePolicy(sizePolicy)
        LoginWindow.setMinimumSize(QtCore.QSize(500, 400))
        LoginWindow.setMaximumSize(QtCore.QSize(700, 400))
        LoginWindow.setAutoFillBackground(False)
        LoginWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 50, 150, 40))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid rgb(5, 0, 0)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 50, 150, 40))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid rgb(0, 0, 0)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 90, 761, 401))
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("loginlogo.png"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        LoginWindow.setCentralWidget(self.centralwidget)


        self.pushButton.clicked.connect(self.signIn)
        self.pushButton_2.clicked.connect(self.signUp)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "GMM"))
        self.pushButton.setText(_translate("LoginWindow", "Sign In"))
        self.pushButton_2.setText(_translate("LoginWindow", "Sign Up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
