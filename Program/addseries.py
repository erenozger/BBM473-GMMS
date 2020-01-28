# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addseries.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
import mysql.connector
import pymysql
import pymysql.cursors
from main import *

class Ui_MainWindowS(object):
    def addTVSeries(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gmm"
        )
        mycursor = db.cursor()


        seriesName = self.seriesName.text()
        details = self.seriesDetails.text()
        genre = self.seriesGenre.text()
        mod_id1 = self.lineEdit.text()
        mod_id = int(mod_id1)
        rating = 0

        query = "SELECT moderator.mod_id FROM moderator WHERE mod_id=%s"
        data = mycursor.execute(query, (mod_id1,))
        print(data)
        if (len(mycursor.fetchall()) > 0):
            mycursor.callproc('addseries', (mod_id, seriesName, rating, details, genre,))
            db.commit()
            print(mycursor.rowcount, "record inserted")
            self.Messagebox("congrats", "Music eklenmistir")
        else:
            self.Warning("alert", "Mod id yanlıs girilmistir")


    def Messagebox(self,title,messege):
        mess = QtWidgets.QMessageBox()

        mess.setWindowTitle(title)
        mess.setText(messege)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def Warning(self,title,messege):

        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(messege)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(476, 332)
        MainWindow.setMinimumSize(QtCore.QSize(476, 332))
        MainWindow.setMaximumSize(QtCore.QSize(476, 332))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addSeries = QtWidgets.QPushButton(self.centralwidget)
        self.addSeries.setGeometry(QtCore.QRect(180, 280, 111, 41))
        self.addSeries.setObjectName("addSeries")
        self.addSeries.clicked.connect(self.addTVSeries)
        self.seriesName = QtWidgets.QLineEdit(self.centralwidget)
        self.seriesName.setGeometry(QtCore.QRect(80, 20, 311, 41))
        self.seriesName.setObjectName("seriesName")
        self.seriesDetails = QtWidgets.QLineEdit(self.centralwidget)
        self.seriesDetails.setGeometry(QtCore.QRect(80, 80, 311, 71))
        self.seriesDetails.setObjectName("seriesDetails")
        self.seriesGenre = QtWidgets.QLineEdit(self.centralwidget)
        self.seriesGenre.setGeometry(QtCore.QRect(80, 170, 311, 41))
        self.seriesGenre.setObjectName("seriesGenre")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 230, 131, 31))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addSeries.setText(_translate("MainWindow", "Add Series"))
        self.seriesName.setPlaceholderText(_translate("MainWindow", "TV Series Name"))
        self.seriesDetails.setPlaceholderText(_translate("MainWindow", "Details"))
        self.seriesGenre.setPlaceholderText(_translate("MainWindow", "Genre"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Mod Id"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowS()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
