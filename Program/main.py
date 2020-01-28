# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from news import *
import pymysql
import mysql.connector
from mysql.connector.cursor import MySQLCursor
import pymysql.cursors
from addcontent import *
from addgame import *
from addmovie import *
from addmusic import *
from addseries import *
from statistics import *
from delete import *
from single import *
from singlenews import *


class Ui_main(object):
    current = []
    userMail = ""
    userPassword = ""
    user_id = 0
    user_role = 0
    latestNews = []

    def __init__(self, user_mail, user_password):
        self.userMail = user_mail
        self.userPassword = user_password

    def getuserid(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gmm"
        )
        mycursor = db.cursor()

        query = "select g.user_id FROM user as u, general_user as g WHERE u.user_mail = g.usermail AND user_mail = %s"
        mycursor.execute(query,(self.userMail,))
        result = mycursor.fetchone()


        self.user_id = result[0]


        query1 = "select role FROM general_user WHERE user_id = %s"
        mycursor.execute(query1,(self.user_id,))
        result1 = mycursor.fetchall()

        self.user_role = result1[0][0]



        mycursor.close()

    def loaddatanews(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gmm"
        )
        mycursor = db.cursor()

        query = "SELECT news.newstitle,news.text FROM news ORDER BY newsdate DESC LIMIT 5;"
        mycursor.execute(query)
        result = mycursor.fetchall()
        self.latestNews = result

        self.latestNewsGroup.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.latestNewsGroup.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.latestNewsGroup.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))

        mycursor.close()

    def loaddatagames(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gmm"
        )
        mycursor = db.cursor()

        query = "SELECT g.game_name, g.game_firm, c.contentdetails,g.gametype, c.date FROM games as g, creategamesrel as c WHERE g.game_id =  c.game_id ORDER BY c.date DESC LIMIT 5;"
        mycursor.execute(query)
        result = mycursor.fetchall()
        self.latestUploadGroup.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.latestUploadGroup.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.latestUploadGroup.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))

        mycursor.close()

    def loaddatatopratedcontents(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gmm"
        )
        mycursor = db.cursor()

        query1 = "SELECT g.game_name,'Game' as contenttype,c.contentdetails,g.rating, m.mod_nick FROM games as g , creategamesrel as c, moderator as m WHERE g.game_id = c.game_id AND c.mod_id = m.mod_id ORDER BY g.rating DESC LIMIT 4;"

        mycursor.execute(query1)
        result1 = mycursor.fetchall()


        query2 = "SELECT m.movie_name,'Movie ' as contenttype,m.movie_type,m.rating,d.mod_nick FROM movies as m, createmoviesrel as c, moderator as d WHERE m.movie_id = c.movie_id AND c.mod_id = d.mod_id ORDER BY m.rating DESC LIMIT 4;"
        mycursor.execute(query2)
        result2 = mycursor.fetchall()


        query3 = "SELECT s.series_name,'Series ' as contenttype,c.contenttype,s.rating,m.mod_nick FROM series as s, createseriesrel as c, moderator as m WHERE s.series_id = c.series_id AND c.mod_id = m.mod_id ORDER BY s.rating DESC LIMIT 4;"
        mycursor.execute(query3)
        result3 = mycursor.fetchall()


        query4 = "SELECT m.music_name,'Music' as contenttype,c.contentdetails,m.rating,d.mod_nick FROM music as m, createmusicrel as c, moderator as d WHERE m.music_id = c.music_id AND c.mod_id = d.mod_id ORDER BY m.rating DESC LIMIT 4;"
        mycursor.execute(query4)
        result4 = mycursor.fetchall()


        self.topRatedGroup.setRowCount(0)

        resultset = []
        resultset = result1 + result2 + result3 + result4
        resultset.sort(key=lambda x: x[3])
        resultset.reverse()
        resultset = resultset[:len(resultset) - 6]


        for row_number, row_data in enumerate(resultset):
            self.topRatedGroup.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.topRatedGroup.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


        mycursor.close()

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

    def clicktable(self):
        single = self.current[self.showGroup.currentRow()]
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_singleWindow(single, self.user_id)
        self.ui.setupUi(self.window)
        self.window.show()


    def refresh(self):
        self.loaddatanews()
        self.loaddatagames()
        self.loaddatatopratedcontents()

    def showMovies(self):
        self.showGroup.clear()
        self.showGroup.setColumnCount(5)
        self.showGroup.horizontalHeader().setDefaultSectionSize(192)
        self.showGroup.setHorizontalHeaderLabels(['MOVIE NAME', 'MOVIE GENRE','MOVIE DETAILS','RATING','ADDED BY'])

        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gmm"
        )
        mycursor = db.cursor()

        query = "SELECT m.movie_name,m.movie_type,c.contentdetails,m.rating,d.mod_nick FROM movies as m, createmoviesrel as c, moderator as d WHERE m.movie_id = c.movie_id AND c.mod_id = d.mod_id ORDER BY m.rating DESC LIMIT 10;"
        mycursor.execute(query)
        result = mycursor.fetchall()
        self.current = result
        self.showGroup.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.showGroup.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.showGroup.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        mycursor.close()




    def showGames(self):
        self.showGroup.clear()
        self.showGroup.setColumnCount(6)
        self.showGroup.horizontalHeader().setDefaultSectionSize(160)
        self.showGroup.setHorizontalHeaderLabels(['GAME NAME', 'GAME FIRM','GAME GENRE','RATING','GAME DETAILS','ADDED BY'])

        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gmm"
        )
        mycursor = db.cursor()

        query = "SELECT g.game_name,g.game_firm,c.contentdetails,g.rating,g.gametype,m.mod_nick FROM games as g , creategamesrel as c, moderator as m WHERE g.game_id = c.game_id AND c.mod_id = m.mod_id ORDER BY g.rating DESC LIMIT 10;"
        mycursor.execute(query)
        result = mycursor.fetchall()
        self.current = result
        self.showGroup.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.showGroup.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.showGroup.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        mycursor.close()


    def showSeries(self):
        self.showGroup.clear()
        self.showGroup.setColumnCount(5)
        self.showGroup.horizontalHeader().setDefaultSectionSize(192)
        self.showGroup.setHorizontalHeaderLabels(['SERIES NAME', 'SERIES GENRE', 'SERIES DETAILS', 'RATING', 'ADDED BY'])

        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gmm"
        )
        mycursor = db.cursor()

        query = "SELECT s.series_name,c.contenttype,c.contentdetails,s.rating,m.mod_nick FROM series as s, createseriesrel as c, moderator as m WHERE s.series_id = c.series_id AND c.mod_id = m.mod_id ORDER BY s.rating DESC LIMIT 10;"
        mycursor.execute(query)
        result = mycursor.fetchall()
        self.current = result
        self.showGroup.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.showGroup.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.showGroup.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        mycursor.close()






    def showMusics(self):
        self.showGroup.clear()
        self.showGroup.setColumnCount(5)
        self.showGroup.horizontalHeader().setDefaultSectionSize(192)
        self.showGroup.setHorizontalHeaderLabels(['MUSIC NAME', 'MUSIC ARTIST', 'MUSIC GENRE', 'RATING', 'ADDED BY'])

        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gmm"
        )
        mycursor = db.cursor()

        query = "SELECT m.music_name,m.music_artist,c.contentdetails,m.rating,d.mod_nick FROM music as m, createmusicrel as c, moderator as d WHERE m.music_id = c.music_id AND c.mod_id = d.mod_id ORDER BY m.rating DESC LIMIT 10;"
        mycursor.execute(query)
        result = mycursor.fetchall()
        self.current = result
        self.showGroup.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.showGroup.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.showGroup.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        mycursor.close()




    def search(self):

        searchbar = self.searchBar.toPlainText()
        if self.filterGames.isChecked():
            self.showGroup.clear()
            self.showGroup.setColumnCount(6)
            self.showGroup.setRowCount(1)
            self.showGroup.horizontalHeader().setDefaultSectionSize(160)
            self.showGroup.setHorizontalHeaderLabels(['GAME NAME', 'GAME FIRM', 'GAME GENRE','RATING','GAME TYPE', 'ADDED BY'])
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gmm"
            )
            mycursor = db.cursor()

            query = "SELECT g.game_name,g.game_firm,c.contentdetails,g.rating,g.gametype,m.mod_nick FROM games as g , creategamesrel as c, moderator as m WHERE g.game_id = c.game_id AND c.mod_id = m.mod_id AND g.game_name LIKE %s ORDER BY g.rating DESC;"
            mycursor.execute(query,("%" + searchbar + "%",))
            result = mycursor.fetchall()
            self.current = result
            self.showGroup.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.showGroup.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.showGroup.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            mycursor.close()



        elif self.filterMovies.isChecked():
            self.showGroup.clear()
            self.showGroup.setColumnCount(5)
            self.showGroup.setRowCount(1)
            self.showGroup.horizontalHeader().setDefaultSectionSize(192)
            self.showGroup.setHorizontalHeaderLabels(['MOVIE NAME', 'MOVIE GENRE', 'MOVIE DETAILS', 'RATING', 'ADDED BY'])
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gmm"
            )
            mycursor = db.cursor()

            query = "SELECT m.movie_name,m.movie_type,c.contentdetails,m.rating,d.mod_nick FROM movies as m, createmoviesrel as c, moderator as d WHERE m.movie_id = c.movie_id AND c.mod_id = d.mod_id AND m.movie_name LIKE %s ORDER BY m.rating DESC;"
            mycursor.execute(query, ("%" + searchbar + "%",))
            result = mycursor.fetchall()
            self.current = result
            self.showGroup.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.showGroup.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.showGroup.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            mycursor.close()



        elif self.filterMusic.isChecked():
            self.showGroup.clear()
            self.showGroup.setColumnCount(5)
            self.showGroup.setRowCount(1)
            self.showGroup.horizontalHeader().setDefaultSectionSize(192)
            self.showGroup.setHorizontalHeaderLabels(['MUSIC NAME', 'MUSIC ARTIST', 'MUSIC GENRE', 'RATING', 'ADDED BY'])

            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gmm"
            )
            mycursor = db.cursor()

            query = "SELECT m.music_name,m.music_artist,c.contentdetails,m.rating,d.mod_nick FROM music as m, createmusicrel as c, moderator as d WHERE m.music_id = c.music_id AND c.mod_id = d.mod_id AND m.music_name LIKE %s ORDER BY m.rating DESC;"

            mycursor.execute(query, ("%" + searchbar + "%",))
            result = mycursor.fetchall()
            self.current = result
            self.showGroup.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.showGroup.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.showGroup.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            mycursor.close()



        elif self.filterSeries.isChecked():
            self.showGroup.clear()
            self.showGroup.setColumnCount(5)
            self.showGroup.setRowCount(1)
            self.showGroup.horizontalHeader().setDefaultSectionSize(192)
            self.showGroup.setHorizontalHeaderLabels(['SERIES NAME', 'SERIES GENRE', 'SERIES DETAILS', 'RATING', 'ADDED BY'])

            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gmm"
            )
            mycursor = db.cursor()

            query = "SELECT s.series_name,c.contenttype,c.contentdetails,s.rating,m.mod_nick FROM series as s, createseriesrel as c, moderator as m WHERE s.series_id = c.series_id AND c.mod_id = m.mod_id AND s.series_name LIKE %s ORDER BY s.rating DESC;"

            mycursor.execute(query, ("%" + searchbar + "%",))
            result = mycursor.fetchall()
            self.current = result
            self.showGroup.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.showGroup.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.showGroup.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            mycursor.close()


        elif self.filterAll.isChecked():
            self.showGroup.clear()
            self.showGroup.setColumnCount(6)
            self.showGroup.setRowCount(1)  # self.showGroup.setRowCount(len(arrayin))
            self.showGroup.horizontalHeader().setDefaultSectionSize(160)
            self.showGroup.setHorizontalHeaderLabels(['NAME', 'GENRE','SOME DETAILS', 'RATING', 'TYPE', 'ADDED BY'])

            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gmm"
            )
            mycursor = db.cursor()


            query1 = "SELECT g.game_name,g.game_firm,c.contentdetails,g.rating,'Game' as contenttype,m.mod_nick FROM games as g , creategamesrel as c, moderator as m WHERE g.game_id = c.game_id AND c.mod_id = m.mod_id AND g.game_name LIKE %s ORDER BY g.rating DESC;"
            mycursor.execute(query1, ("%" + searchbar + "%",))
            result1 = mycursor.fetchall()

            query2 = "SELECT m.movie_name,m.movie_type,c.contentdetails,m.rating,'Movie' as contenttype,d.mod_nick FROM movies as m, createmoviesrel as c, moderator as d WHERE m.movie_id = c.movie_id AND c.mod_id = d.mod_id AND m.movie_name LIKE %s ORDER BY m.rating DESC;"
            mycursor.execute(query2, ("%" + searchbar + "%",))
            result2 = mycursor.fetchall()

            query3 = "SELECT m.music_name,m.music_artist,c.contentdetails,m.rating,'Music' as contenttype,d.mod_nick FROM music as m, createmusicrel as c, moderator as d WHERE m.music_id = c.music_id AND c.mod_id = d.mod_id AND m.music_name LIKE %s ORDER BY m.rating DESC;"
            mycursor.execute(query3, ("%" + searchbar + "%",))
            result3 = mycursor.fetchall()

            query4 = "SELECT s.series_name,c.contenttype,c.contentdetails,s.rating,'Series' as contenttype,m.mod_nick FROM series as s, createseriesrel as c, moderator as m WHERE s.series_id = c.series_id AND c.mod_id = m.mod_id AND s.series_name LIKE %s ORDER BY s.rating DESC;"
            mycursor.execute(query4, ("%" + searchbar + "%",))
            result4 = mycursor.fetchall()

            resultset = []
            resultset = result1 + result2 + result3 + result4

            resultset.sort(key=lambda x: x[3])
            resultset.reverse()
            #resultset = resultset[:len(resultset) - 6]

            self.current = resultset
            self.showGroup.setRowCount(0)

            for row_number, row_data in enumerate(resultset):
                self.showGroup.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.showGroup.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            mycursor.close()




        else:
            self.showGroup.clear()
            self.showGroup.setColumnCount(5)
            self.showGroup.setRowCount(1)# self.showGroup.setRowCount(len(arrayin))
            self.showGroup.horizontalHeader().setDefaultSectionSize(192)
            self.showGroup.setHorizontalHeaderLabels(['NAME', 'GENRE','TYPE', 'RATING', 'ADDED BY'])
            self.Warning("alert", "Please choose the filter. ")



    def clickedNews(self):
        singleNew = self.latestNews[self.latestNewsGroup.currentRow()]
        newstitle = singleNew[0]
        newsdetail = singleNew[1]

        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gmm"
        )
        mycursor = db.cursor()
        query = "SELECT u.user_name,g.user_nick,n.newsdate FROM user as u,general_user as g,news_writer as w,news as n WHERE u.user_mail = g.usermail AND g.user_id = w.user_idfk2 AND w.writer_id = n.writer_id AND n.newstitle = %s AND n.text = %s "
        mycursor.execute(query,(newstitle,newsdetail,))
        result = mycursor.fetchall()
        authorname  = result[0][0]
        authornick = result[0][1]
        newsdate = result[0][2]
        mycursor.close()


        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SingleNews(singleNew[0],singleNew[1],authorname,authornick,newsdate)
        self.ui.setupUi(self.window)
        self.window.show()

    def statistic(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_statisticWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def addNews(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_window2(self.user_id)
        self.ui.setupUi(self.window)
        self.window.show()

    def addContent(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowC()
        self.ui.setupUi(self.window)
        self.window.show()
    def reviewbutton(self):
        self.Messagebox("Review Massage ",
                        " Yorum yapıp puan vermek istediginiz contenti search kısmından bulup üzerine cift tıklayarak gelen sayfadan yapabilirsiniz.")
    def setupUi(self, main):
        self.getuserid()
        main.setObjectName("main")
        main.resize(1063, 907)
        main.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(main)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 120, 84, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 280, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 440, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.showMoviesB = QtWidgets.QPushButton(self.centralwidget)
        self.showMoviesB.setGeometry(QtCore.QRect(20, 640, 75, 23))
        self.showMoviesB.setObjectName("showMoviesB")
        self.showGamesB = QtWidgets.QPushButton(self.centralwidget)
        self.showGamesB.setGeometry(QtCore.QRect(110, 640, 75, 23))
        self.showGamesB.setObjectName("showGamesB")
        self.showSeriesB = QtWidgets.QPushButton(self.centralwidget)
        self.showSeriesB.setGeometry(QtCore.QRect(200, 640, 91, 23))
        self.showSeriesB.setObjectName("showSeriesB")
        self.showMusicB = QtWidgets.QPushButton(self.centralwidget)
        self.showMusicB.setGeometry(QtCore.QRect(310, 640, 75, 23))
        self.showMusicB.setObjectName("showMusicB")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 1011, 111))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        self.addContentB = QtWidgets.QPushButton(self.groupBox)
        self.addContentB.setGeometry(QtCore.QRect(880, 10, 131, 31))
        self.addContentB.setObjectName("addContentB")
        if(self.user_role == 2 or self.user_role == 5):
            self.addContentB.setVisible(True)
        else:
            self.addContentB.setVisible(False)



        self.writeNewsB = QtWidgets.QPushButton(self.groupBox)
        self.writeNewsB.setGeometry(QtCore.QRect(700, 10, 121, 31))
        self.writeNewsB.setObjectName("writeNewsB")
        if (self.user_role == 3 or self.user_role == 5):
            self.writeNewsB.setVisible(True)
        else:
            self.writeNewsB.setVisible(False)

        self.userreviewB = QtWidgets.QPushButton(self.groupBox)
        self.userreviewB.setGeometry(QtCore.QRect(740, 50, 101, 31))
        self.userreviewB.setObjectName("userreviewB")
        self.statisticsB = QtWidgets.QPushButton(self.groupBox)
        self.statisticsB.setGeometry(QtCore.QRect(865, 50, 101, 31))
        self.statisticsB.setObjectName("pushButton")
        self.RELOAD = QtWidgets.QPushButton(self.groupBox)
        self.RELOAD.setGeometry(QtCore.QRect(525, 10, 121, 31))
        self.RELOAD.setObjectName("RELOAD")
        self.searchFilterGroup = QtWidgets.QGroupBox(self.groupBox)
        self.searchFilterGroup.setGeometry(QtCore.QRect(10, 40, 701, 61))
        self.searchFilterGroup.setObjectName("searchFilterGroup")
        self.filterMovies = QtWidgets.QRadioButton(self.searchFilterGroup)
        self.filterMovies.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.filterMovies.setObjectName("filterMovies")
        self.filterSeries = QtWidgets.QRadioButton(self.searchFilterGroup)
        self.filterSeries.setGeometry(QtCore.QRect(90, 10, 82, 17))
        self.filterSeries.setObjectName("filterSeries")
        self.filterGames = QtWidgets.QRadioButton(self.searchFilterGroup)
        self.filterGames.setGeometry(QtCore.QRect(190, 10, 82, 17))
        self.filterGames.setObjectName("filterGames")
        self.filterMusic = QtWidgets.QRadioButton(self.searchFilterGroup)
        self.filterMusic.setGeometry(QtCore.QRect(290, 10, 82, 17))
        self.filterMusic.setObjectName("filterMusic")
        self.filterAll = QtWidgets.QRadioButton(self.searchFilterGroup)
        self.filterAll.setGeometry(QtCore.QRect(375, 10, 82, 17))
        self.filterAll.setObjectName("filterMusic")
        self.searchBar = QtWidgets.QTextEdit(self.searchFilterGroup)
        self.searchBar.setGeometry(QtCore.QRect(480, 20, 181, 31))
        self.searchBar.setObjectName("searchBar")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 400, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.latestNewsGroup = QtWidgets.QTableWidget(self.centralwidget)
        self.latestNewsGroup.setEnabled(True)
        self.latestNewsGroup.setGeometry(QtCore.QRect(20, 150, 1001, 121))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.latestNewsGroup.sizePolicy().hasHeightForWidth())
        self.latestNewsGroup.setSizePolicy(sizePolicy)
        self.latestNewsGroup.setLineWidth(1)
        self.latestNewsGroup.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.latestNewsGroup.setDragDropOverwriteMode(True)
        self.latestNewsGroup.setShowGrid(True)
        self.latestNewsGroup.setGridStyle(QtCore.Qt.DashLine)
        self.latestNewsGroup.setWordWrap(True)
        self.latestNewsGroup.setCornerButtonEnabled(True)
        self.latestNewsGroup.setRowCount(5)
        self.latestNewsGroup.setColumnCount(2)
        self.latestNewsGroup.setObjectName("latestNewsGroup")
        self.latestNewsGroup.horizontalHeader().setCascadingSectionResizes(False)
        self.latestNewsGroup.horizontalHeader().setDefaultSectionSize(195)
        self.latestNewsGroup.horizontalHeader().setMinimumSectionSize(20)
        self.latestNewsGroup.horizontalHeader().setSortIndicatorShown(False)
        self.latestNewsGroup.horizontalHeader().setStretchLastSection(True)
        self.latestNewsGroup.verticalHeader().setCascadingSectionResizes(True)
        self.latestNewsGroup.verticalHeader().setHighlightSections(True)
        self.latestNewsGroup.verticalHeader().setMinimumSectionSize(23)
        self.latestNewsGroup.verticalHeader().setSortIndicatorShown(False)
        self.latestNewsGroup.verticalHeader().setStretchLastSection(False)
        self.latestNewsGroup.doubleClicked.connect(self.clickedNews)
        self.latestUploadGroup = QtWidgets.QTableWidget(self.centralwidget)
        self.latestUploadGroup.setGeometry(QtCore.QRect(20, 310, 1001, 131))
        self.latestUploadGroup.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.latestUploadGroup.setGridStyle(QtCore.Qt.DashLine)
        self.latestUploadGroup.setRowCount(5)
        self.latestUploadGroup.setColumnCount(5)
        self.latestUploadGroup.setObjectName("latestUploadGroup")
        item = QtWidgets.QTableWidgetItem()
        self.latestUploadGroup.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.latestUploadGroup.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.latestUploadGroup.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.latestUploadGroup.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.latestUploadGroup.setHorizontalHeaderItem(4, item)
        self.latestUploadGroup.horizontalHeader().setDefaultSectionSize(193)
        self.latestUploadGroup.horizontalHeader().setMinimumSectionSize(40)
        self.topRatedGroup = QtWidgets.QTableWidget(self.centralwidget)
        self.topRatedGroup.setGeometry(QtCore.QRect(20, 480, 1001, 151))
        self.topRatedGroup.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.topRatedGroup.setGridStyle(QtCore.Qt.DashLine)
        self.topRatedGroup.setRowCount(5)
        self.topRatedGroup.setColumnCount(5)
        self.topRatedGroup.setObjectName("topRatedGroup")
        item = QtWidgets.QTableWidgetItem()
        self.topRatedGroup.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.topRatedGroup.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.topRatedGroup.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.topRatedGroup.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.topRatedGroup.setHorizontalHeaderItem(4, item)
        self.topRatedGroup.horizontalHeader().setDefaultSectionSize(193)
        self.showGroup = QtWidgets.QTableWidget(self.centralwidget)
        self.showGroup.setGeometry(QtCore.QRect(20, 670, 1001, 231))
        self.showGroup.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.showGroup.setGridStyle(QtCore.Qt.DashLine)
        self.showGroup.setRowCount(10)
        self.showGroup.setColumnCount(5)
        self.showGroup.setObjectName("showGroup")
        self.showGroup.horizontalHeader().setDefaultSectionSize(192)
        self.showGroup.doubleClicked.connect(self.clicktable)

        self.showMoviesB.clicked.connect(self.showMovies)
        self.showGamesB.clicked.connect(self.showGames)
        self.showSeriesB.clicked.connect(self.showSeries)
        self.showMusicB.clicked.connect(self.showMusics)
        self.searchBar.textChanged.connect(self.search)
        self.addContentB.clicked.connect(self.addContent)
        self.RELOAD.clicked.connect(self.refresh)
        self.writeNewsB.clicked.connect(self.addNews)
        self.userreviewB.clicked.connect(self.reviewbutton)
        self.loaddatanews()
        self.loaddatagames()
        self.loaddatatopratedcontents()


        self.statisticsB.clicked.connect(self.statistic)
        main.setCentralWidget(self.centralwidget)

        self.retranslateUi(main,self.user_id)

        QtCore.QMetaObject.connectSlotsByName(main)
    def retranslateUi(self, main,user_id):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "GMM"))
        self.label.setText(_translate("main", "Latest News"))
        self.label_2.setText(_translate("main", "Latest Uploaded Games"))
        self.label_3.setText(_translate("main", "Top Rated Contents"))

        self.showMoviesB.setText(_translate("main", "Show Movies"))
        self.showGamesB.setText(_translate("main", "Show Games"))
        self.showSeriesB.setText(_translate("main", "Show TV Series"))
        self.showMusicB.setText(_translate("main", "Show Musics"))
        self.addContentB.setText(_translate("main", "Add - Delete Content"))
        self.writeNewsB.setText(_translate("main", "Write News"))
        self.RELOAD.setText(_translate("main", "RELOAD"))
        self.searchFilterGroup.setTitle(_translate("main", "Filter"))
        self.filterMovies.setText(_translate("main", "Movies"))
        self.filterSeries.setText(_translate("main", "TV Series"))
        self.filterGames.setText(_translate("main", "Games"))
        self.filterMusic.setText(_translate("main", "Music"))
        self.filterAll.setText(_translate("main", "All"))
        self.searchBar.setPlaceholderText(_translate("main", "Search"))
        self.statisticsB.setText(_translate("main", "Statisctics"))
        self.userreviewB.setText(_translate("main", "User Review"))
        self.label_4.setText(_translate("main", 'User mail : ' + self.userMail + ' user id : ' + str(self.user_id)))
        self.latestNewsGroup.setHorizontalHeaderLabels(['NEWS TITLE', 'NEWS DETAILS'])
        self.latestNewsGroup.setSortingEnabled(False)
        item = self.latestUploadGroup.horizontalHeaderItem(0)
        item.setText(_translate("main", "GAME NAME"))
        item = self.latestUploadGroup.horizontalHeaderItem(1)
        item.setText(_translate("main", "GAME TYPE"))
        item = self.latestUploadGroup.horizontalHeaderItem(2)
        item.setText(_translate("main", "GAME FIRM"))
        item = self.latestUploadGroup.horizontalHeaderItem(3)
        item.setText(_translate("main", "GAME GENRE"))
        item = self.latestUploadGroup.horizontalHeaderItem(4)
        item.setText(_translate("main", "DATE"))
        item = self.topRatedGroup.horizontalHeaderItem(0)
        item.setText(_translate("main", "TITLE"))
        item = self.topRatedGroup.horizontalHeaderItem(1)
        item.setText(_translate("main", "TYPE"))
        item = self.topRatedGroup.horizontalHeaderItem(2)
        item.setText(_translate("main", "GENRE"))
        item = self.topRatedGroup.horizontalHeaderItem(3)
        item.setText(_translate("main", "RATING"))
        item = self.topRatedGroup.horizontalHeaderItem(4)
        item.setText(_translate("main", "ADDED BY"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QMainWindow()
    ui = Ui_main()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())
