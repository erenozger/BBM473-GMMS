# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from main import Ui_main
import mysql.connector
import pymysql
import pymysql.cursors
from news import *
from addcontent import *
from addgame import *
from addmovie import *
from addmusic import *
from addseries import *
from statistics import *
from statistics import *
from single import *
from singlenews import *
from delete import *

class Ui_MainWindow(object):
    def signInControl(self):
        email = str(self.uMail.text())
        password = str(self.uPw.text())
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gmm"
        )
        mycursor = db.cursor()
        query = "SELECT user.user_mail,user.password FROM user WHERE user_mail=%s AND password=%s"
        data = mycursor.execute(query, (email,password,))
        if (len(mycursor.fetchall()) > 0):
            self.Messagebox("Congrats", "Successfully logged in")
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_main(email,password)
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            self.Warning("Alert", "Sorry, we couldn't find an account with that usermail or password.")

    def Warning(self,title,messege):

        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(messege)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    def Messagebox(self,title,messege):
        mess = QtWidgets.QMessageBox()

        mess.setWindowTitle(title)
        mess.setText(messege)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(490, 312)
        MainWindow.setMinimumSize(QtCore.QSize(490, 312))
        MainWindow.setMaximumSize(QtCore.QSize(490, 312))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.uMail = QtWidgets.QLineEdit(self.centralwidget)
        self.uMail.setGeometry(QtCore.QRect(120, 50, 251, 41))
        self.uMail.setObjectName("uMail")
        self.uPw = QtWidgets.QLineEdit(self.centralwidget)
        self.uPw.setGeometry(QtCore.QRect(120, 110, 251, 41))
        self.uPw.setInputMask("")
        self.uPw.setObjectName("uPw")
        self.uPw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signInB = QtWidgets.QPushButton(self.centralwidget)
        self.signInB.setGeometry(QtCore.QRect(190, 170, 101, 41))
        self.signInB.setObjectName("signInB")
        self.signInB.clicked.connect(self.signInControl)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.uPw.setPlaceholderText(_translate("MainWindow", "Password"))
        self.uMail.setPlaceholderText(_translate("MainWindow", "E-Mail"))
        self.signInB.setText(_translate("MainWindow", "Sign In"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
