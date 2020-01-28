# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statistics.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import pymysql
import mysql.connector
from mysql.connector.cursor import MySQLCursor
import pymysql.cursors


class Ui_statisticWindow(object):
    def showstatistics(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gmm"
        )
        mycursor = db.cursor()

        query = " SELECT COUNT(*) FROM games"
        mycursor.execute(query)
        result = mycursor.fetchone()
        gamecount = result[0]
        self.gamesLCD.setProperty("intValue",gamecount)

        query = " SELECT COUNT(*) FROM movies"
        mycursor.execute(query)
        result = mycursor.fetchone()
        moviecount = result[0]
        self.moviesLCD.setProperty("intValue", moviecount)

        query = " SELECT COUNT(*) FROM music"
        mycursor.execute(query)
        result = mycursor.fetchone()
        musiccount = result[0]
        self.musicsLCD.setProperty("intValue", musiccount)

        query = " SELECT COUNT(*) FROM series"
        mycursor.execute(query)
        result = mycursor.fetchone()
        seriescount = result[0]
        self.seriesLCD.setProperty("intValue", seriescount)

        numberofcontents = gamecount + moviecount + musiccount + seriescount
        self.contentLCD.setProperty("intValue",numberofcontents)

        query = " SELECT COUNT(*) FROM news"
        mycursor.execute(query)
        result = mycursor.fetchone()
        newscount = result[0]
        self.newsLCD.setProperty("intValue", newscount)

        query = " SELECT COUNT(*) FROM general_user"
        mycursor.execute(query)
        result = mycursor.fetchone()
        usercount = result[0]
        self.usersLCD.setProperty("intValue", usercount)

        query = " SELECT COUNT(*) FROM moderator"
        mycursor.execute(query)
        result = mycursor.fetchone()
        moderatorcount = result[0]
        self.lcdNumber_8.setProperty("intValue", moderatorcount)

        query = " SELECT COUNT(*) FROM news_writer"
        mycursor.execute(query)
        result = mycursor.fetchone()
        writerscount = result[0]
        self.lcdNumber_9.setProperty("intValue", writerscount)




        mycursor.close()

    def setupUi(self, statisticWindow):

        statisticWindow.setObjectName("statisticWindow")
        statisticWindow.resize(461, 471)
        self.centralwidget = QtWidgets.QWidget(statisticWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.contentLabel = QtWidgets.QLabel(self.centralwidget)
        self.contentLabel.setGeometry(QtCore.QRect(30, 10, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.contentLabel.setFont(font)
        self.contentLabel.setObjectName("contentLabel")
        self.newsLabel = QtWidgets.QLabel(self.centralwidget)
        self.newsLabel.setGeometry(QtCore.QRect(30, 60, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.newsLabel.setFont(font)
        self.newsLabel.setObjectName("newsLabel")
        self.moviesLabel = QtWidgets.QLabel(self.centralwidget)
        self.moviesLabel.setGeometry(QtCore.QRect(30, 110, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.moviesLabel.setFont(font)
        self.moviesLabel.setObjectName("moviesLabel")
        self.gamesLabel = QtWidgets.QLabel(self.centralwidget)
        self.gamesLabel.setGeometry(QtCore.QRect(30, 160, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.gamesLabel.setFont(font)
        self.gamesLabel.setObjectName("gamesLabel")
        self.musicsLabel = QtWidgets.QLabel(self.centralwidget)
        self.musicsLabel.setGeometry(QtCore.QRect(30, 260, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.musicsLabel.setFont(font)
        self.musicsLabel.setObjectName("musicsLabel")
        self.seriesLabel = QtWidgets.QLabel(self.centralwidget)
        self.seriesLabel.setGeometry(QtCore.QRect(30, 210, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.seriesLabel.setFont(font)
        self.seriesLabel.setObjectName("seriesLabel")
        self.usersLabel = QtWidgets.QLabel(self.centralwidget)
        self.usersLabel.setGeometry(QtCore.QRect(30, 310, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.usersLabel.setFont(font)
        self.usersLabel.setObjectName("usersLabel")
        self.moderatorsLabel = QtWidgets.QLabel(self.centralwidget)
        self.moderatorsLabel.setGeometry(QtCore.QRect(30, 360, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.moderatorsLabel.setFont(font)
        self.moderatorsLabel.setObjectName("moderatorsLabel")
        self.writersLabel = QtWidgets.QLabel(self.centralwidget)
        self.writersLabel.setGeometry(QtCore.QRect(30, 410, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.writersLabel.setFont(font)
        self.writersLabel.setObjectName("writersLabel")
        self.contentLCD = QtWidgets.QLCDNumber(self.centralwidget)
        self.contentLCD.setGeometry(QtCore.QRect(260, 10, 101, 31))
        self.contentLCD.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.contentLCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.contentLCD.setProperty("value", 123.0)
        self.contentLCD.setProperty("intValue", 123)
        self.contentLCD.setObjectName("contentLCD")
        self.newsLCD = QtWidgets.QLCDNumber(self.centralwidget)
        self.newsLCD.setGeometry(QtCore.QRect(240, 60, 101, 31))
        self.newsLCD.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.newsLCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.newsLCD.setProperty("value", 123.0)
        self.newsLCD.setProperty("intValue", 123)
        self.newsLCD.setObjectName("newsLCD")
        self.moviesLCD = QtWidgets.QLCDNumber(self.centralwidget)
        self.moviesLCD.setGeometry(QtCore.QRect(250, 110, 101, 31))
        self.moviesLCD.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.moviesLCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.moviesLCD.setProperty("value", 123.0)
        self.moviesLCD.setProperty("intValue", 123)
        self.moviesLCD.setObjectName("moviesLCD")
        self.gamesLCD = QtWidgets.QLCDNumber(self.centralwidget)
        self.gamesLCD.setGeometry(QtCore.QRect(250, 160, 101, 31))
        self.gamesLCD.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gamesLCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.gamesLCD.setProperty("value", 123.0)
        self.gamesLCD.setProperty("intValue", 123)
        self.gamesLCD.setObjectName("gamesLCD")
        self.seriesLCD = QtWidgets.QLCDNumber(self.centralwidget)
        self.seriesLCD.setGeometry(QtCore.QRect(270, 210, 101, 31))
        self.seriesLCD.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.seriesLCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.seriesLCD.setProperty("value", 123.0)
        self.seriesLCD.setProperty("intValue", 123)
        self.seriesLCD.setObjectName("seriesLCD")
        self.musicsLCD = QtWidgets.QLCDNumber(self.centralwidget)
        self.musicsLCD.setGeometry(QtCore.QRect(250, 260, 101, 31))
        self.musicsLCD.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.musicsLCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.musicsLCD.setProperty("value", 123.0)
        self.musicsLCD.setProperty("intValue", 123)
        self.musicsLCD.setObjectName("musicsLCD")
        self.usersLCD = QtWidgets.QLCDNumber(self.centralwidget)
        self.usersLCD.setGeometry(QtCore.QRect(240, 310, 101, 31))
        self.usersLCD.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.usersLCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.usersLCD.setProperty("value", 123.0)
        self.usersLCD.setProperty("intValue", 123)
        self.usersLCD.setObjectName("usersLCD")
        self.lcdNumber_8 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_8.setGeometry(QtCore.QRect(290, 360, 101, 31))
        self.lcdNumber_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber_8.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_8.setProperty("value", 123.0)
        self.lcdNumber_8.setProperty("intValue", 123)
        self.lcdNumber_8.setObjectName("lcdNumber_8")
        self.lcdNumber_9 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_9.setGeometry(QtCore.QRect(255, 410, 101, 31))
        self.lcdNumber_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber_9.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_9.setProperty("value", 123.0)
        self.lcdNumber_9.setProperty("intValue", 123)
        self.lcdNumber_9.setObjectName("lcdNumber_8")

        statisticWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(statisticWindow)
        self.showstatistics()
        QtCore.QMetaObject.connectSlotsByName(statisticWindow)

    def retranslateUi(self, statisticWindow):
        _translate = QtCore.QCoreApplication.translate
        statisticWindow.setWindowTitle(_translate("statisticWindow", "MainWindow"))
        self.contentLabel.setText(_translate("statisticWindow", "Total Number of Content: "))
        self.newsLabel.setText(_translate("statisticWindow", "Total Number of News: "))
        self.moviesLabel.setText(_translate("statisticWindow", "Total Number of Movies: "))
        self.gamesLabel.setText(_translate("statisticWindow", "Total Number of Games: "))
        self.musicsLabel.setText(_translate("statisticWindow", "Total Number of Musics: "))
        self.seriesLabel.setText(_translate("statisticWindow", "Total Number of TV Series: "))
        self.usersLabel.setText(_translate("statisticWindow", "Total Number of Users: "))
        self.moderatorsLabel.setText(_translate("statisticWindow", "Total Number of Moderators: "))
        self.writersLabel.setText(_translate("statisticWindow", "Total Number of Writers: "))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    statisticWindow = QtWidgets.QMainWindow()
    ui = Ui_statisticWindow()
    ui.setupUi(statisticWindow)
    statisticWindow.show()
    sys.exit(app.exec_())
