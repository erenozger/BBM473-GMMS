# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import mysql.connector
import pymysql
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql.cursors
from main import *


class Ui_LoginWindow2(object):

    def signup(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gmm"
        )
        mycursor = db.cursor()


        "IF SUCCESS ROUTE TO MAIN.PY ELSE NOTHING"
        email = str(self.uMail.text())
        password = str(self.uPw.text())
        userName = str(self.uName.text())
        userNick = str(self.uNick.text())
        dob = str(self.uDob.text())

        mycursor.callproc('userregister', (email, password, userName, dob, userNick,))
        db.commit()
        print(mycursor.rowcount, "record inserted")

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_main(email,password)
        self.ui.setupUi(self.window)
        self.window.show()


    def userregistercontrol(self):
        email = str(self.uMail.text())

        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gmm"
        )
        mycursor = db.cursor()
        query = "SELECT user.user_mail FROM user WHERE user_mail=%s"
        data = mycursor.execute(query,(email,))
        print(data)
        if(len(mycursor.fetchall())>0):
            self.Warning("alert", "This Email is already using ")
        else:
            self.Messagebox("congrats","Your account has been created successfully.")
            self.signup()

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

    def setupUi(self, LoginWindow2):
        LoginWindow2.setObjectName("LoginWindow2")
        LoginWindow2.resize(766, 363)
        LoginWindow2.setMinimumSize(QtCore.QSize(766, 363))
        LoginWindow2.setMaximumSize(QtCore.QSize(766, 363))
        self.centralwidget = QtWidgets.QWidget(LoginWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.uMail = QtWidgets.QLineEdit(self.centralwidget)
        self.uMail.setGeometry(QtCore.QRect(270, 50, 291, 31))
        self.uMail.setObjectName("uMail")
        self.uPw = QtWidgets.QLineEdit(self.centralwidget)
        self.uPw.setGeometry(QtCore.QRect(270, 100, 291, 31))
        self.uPw.setObjectName("uPw")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 300, 121, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.userregistercontrol)

        self.uName = QtWidgets.QLineEdit(self.centralwidget)
        self.uName.setGeometry(QtCore.QRect(270, 150, 291, 31))
        self.uName.setObjectName("uName")

        self.uNick = QtWidgets.QLineEdit(self.centralwidget)
        self.uNick.setGeometry(QtCore.QRect(270, 200, 291, 31))
        self.uNick.setObjectName("uNick")

        self.uDob = QtWidgets.QLineEdit(self.centralwidget)
        self.uDob.setGeometry(QtCore.QRect(270, 250, 291, 31))
        self.uDob.setObjectName("uDob")

        LoginWindow2.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow2)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow2)

    def retranslateUi(self, LoginWindow2):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow2.setWindowTitle(_translate("LoginWindow2", "MainWindow"))
        self.uMail.setPlaceholderText(_translate("LoginWindow2", "E-Mail"))
        self.uPw.setPlaceholderText(_translate("LoginWindow2", "Password"))
        self.pushButton.setText(_translate("LoginWindow2", "Sign Up"))
        self.uName.setPlaceholderText(_translate("LoginWindow2", "User Name"))
        self.uNick.setPlaceholderText(_translate("LoginWindow2", "User Nick"))
        self.uDob.setPlaceholderText(_translate("LoginWindow2", "Birth Date"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow2 = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow2()
    ui.setupUi(LoginWindow2)
    LoginWindow2.show()
    sys.exit(app.exec_())
