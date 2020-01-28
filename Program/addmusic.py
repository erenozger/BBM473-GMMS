# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addmusic.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import pymysql
import pymysql.cursors
from main import *

class Ui_MainWindowM(object):
    def addMusic(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gmm"
        )
        mycursor = db.cursor()

        music_name = self.musicName.text()
        music_artist = self.musicArtist.text()
        music_genre = self.musicGenre.text()
        music_language = self.musicLanguage.text()
        rating = 0
        mod_id1 = self.lineEdit.text()
        mod_id = int(mod_id1)

        query = "SELECT moderator.mod_id FROM moderator WHERE mod_id=%s"
        data = mycursor.execute(query, (mod_id1,))
        print(data)
        if (len(mycursor.fetchall()) > 0):
            mycursor.callproc('addmusic', (mod_id, music_artist, music_name, rating, music_genre, music_language,))
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
        MainWindow.resize(454, 353)
        MainWindow.setMinimumSize(QtCore.QSize(454, 353))
        MainWindow.setMaximumSize(QtCore.QSize(454, 353))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.musicName = QtWidgets.QLineEdit(self.centralwidget)
        self.musicName.setGeometry(QtCore.QRect(90, 30, 281, 41))
        self.musicName.setObjectName("musicName")
        self.musicArtist = QtWidgets.QLineEdit(self.centralwidget)
        self.musicArtist.setGeometry(QtCore.QRect(90, 80, 281, 41))
        self.musicArtist.setObjectName("musicArtist")
        self.musicGenre = QtWidgets.QLineEdit(self.centralwidget)
        self.musicGenre.setGeometry(QtCore.QRect(90, 130, 281, 41))
        self.musicGenre.setObjectName("musicGenre")
        self.musicLanguage = QtWidgets.QLineEdit(self.centralwidget)
        self.musicLanguage.setGeometry(QtCore.QRect(90, 180, 281, 41))
        self.musicLanguage.setObjectName("musicLanguage")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 270, 141, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.addMusic)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 230, 131, 31))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.musicName.setPlaceholderText(_translate("MainWindow", "Music Name"))
        self.musicArtist.setPlaceholderText(_translate("MainWindow", "Music Artist"))
        self.musicGenre.setPlaceholderText(_translate("MainWindow", "Genre"))
        self.musicLanguage.setPlaceholderText(_translate("MainWindow", "Music Language"))
        self.pushButton.setText(_translate("MainWindow", "Add Music"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Mod Id"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowM()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
