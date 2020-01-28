# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'single.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

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
from singlenews import *



class Ui_singleWindow(object):

    uId = 0
    single = []
    content_id = 0
    content_type = 0
    #tpye 1 = game // type 2 = movie // type = 3 music // type = 4 series


    def __init__(self,single_,user_id):
        self.uId = user_id
        self.single = single_



    def getcontenttitle(self):

        self.contentNameLabel.setText(self.single[0])
        #self.ratingLabel.setText(str("{0:.2f}".format(self.single[3])))





    def getcontentid(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gmm"
        )
        mycursor = db.cursor()

        a = self.single[0]
        b = self.single[1]
        c = self.single[2]
        query1 = "SELECT g.game_id FROM games as g, creategamesrel as c WHERE g.game_name = %s AND g.game_firm = %s AND c.contentdetails = %s"
        mycursor.execute(query1,(a,b,c,))
        result = mycursor.fetchall()

        if (len(result) > 0):
            self.content_id = result[0][0]
            self.content_type = 1
            self.typeLabel.setText('Game')
        else:
            self.content_id = 0
            self.content_type = 0
            query2 = "SELECT m.movie_id FROM movies as m , createmoviesrel as c WHERE m.movie_name = %s AND m.movie_type = %s AND c.contentdetails = %s"
            mycursor.execute(query2, (a, b, c,))
            result2 = mycursor.fetchall()
            if (len(result2) > 0):
                self.content_id = result2[0][0]
                self.content_type = 2
                self.typeLabel.setText('Movie')
            else:
                self.content_id = 0
                self.content_type = 0
                query3 = "SELECT m.music_id FROM music as m , createmusicrel as c WHERE m.music_name = %s AND m.music_artist = %s AND c.contentdetails = %s"
                mycursor.execute(query3, (a, b, c,))
                result3 = mycursor.fetchall()
                if (len(result3) > 0):
                    self.content_id = result3[0][0]
                    self.content_type = 3
                    self.typeLabel.setText('Music')
                else:
                    self.content_id = 0
                    self.content_type = 0
                    query4 = "SELECT s.series_id FROM series as s , createseriesrel as c WHERE s.series_name = %s AND c.contenttype = %s AND c.contentdetails = %s"
                    mycursor.execute(query4, (a, b, c,))
                    result4 = mycursor.fetchall()
                    if (len(result4) > 0):
                        self.content_id = result4[0][0]
                        self.content_type = 4
                        self.typeLabel.setText('Series')
                    else:
                        self.content_id = 0
                        self.content_type = 0
                        self.typeLabel.setText('There is no content like this')


        self.review()























        mycursor.close()

    def review(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gmm"
        )
        mycursor = db.cursor()
        contentid = self.content_id
        userid = self.uId

        contenttpye = self.content_type

        if(contenttpye == 1):
            query1 = "SELECT * FROM games as g, creategamesrel as c WHERE g.game_id = %s AND g.game_id = c.game_id"
            mycursor.execute(query1,(contentid,))
            resultset = mycursor.fetchall()
            gamename = resultset[0][1]
            gamefirm = resultset[0][2]
            gamerating = resultset[0][3]
            self.ratingLabel.setText(str("{0:.2f}".format(gamerating)))
            gameplatform = resultset[0][4]
            gameratingcount = resultset[0][5]
            gamegenre = resultset[0][8]
            gamelanguage = resultset[0][9]
            gameaddeddate = resultset[0][10]

            self.detailsTextArea.setPlainText('Game Name : '+str(gamename)+'\n'+'\n'+'Game Firm : '+ str(gamefirm) + '\n'+'\n'+
                                              'Game Platform : '+ str(gameplatform) +'\n'+'\n'+ 'Game Genre :' + str(gamegenre) +'\n'+'\n'+
                                              'Game Rating : ' + str("{0:.2f}".format(gamerating)) + '\n'+'\n'+ 'Rating count by users : ' + str(gameratingcount) + '\n'+'\n'+
                                              'Game Language : ' + str(gamelanguage+'\n'+'\n'+'Game added date :' + str(gameaddeddate))
                                              )




        elif(contenttpye == 2):
            query2 = "SELECT * FROM movies as m, createmoviesrel as c WHERE m.movie_id = %s AND m.movie_id = c.movie_id"
            mycursor.execute(query2, (contentid,))
            resultset = mycursor.fetchall()
            moviename = resultset[0][1]
            moviegenre = resultset[0][2]
            movierating = resultset[0][3]
            self.ratingLabel.setText(str("{0:.2f}".format(movierating)))
            movieratingcount = resultset[0][4]
            Moviedetails = resultset[0][7]
            MovieLanguage = resultset[0][8]
            self.detailsTextArea.setPlainText(
                'Movie Name : ' + str(moviename) + '\n' + '\n' + 'Movie Genre : ' + str(moviegenre) + '\n' + '\n' +
                'Movie Rating : ' + str("{0:.2f}".format(movierating)) + '\n' + '\n' + 'Rating count by users :' + str(movieratingcount) + '\n' + '\n' +
                'Movie Language : ' + str(MovieLanguage) + '\n' + '\n' + 'Movie Details : ' + str(
                    Moviedetails)
                )



        elif(contenttpye == 3):
            query3 = "SELECT * FROM music as m, createmusicrel as c WHERE m.music_id = %s AND m.music_id = c.music_id"
            mycursor.execute(query3, (contentid,))
            resultset = mycursor.fetchall()
            musicartist = resultset[0][1]
            musicname = resultset[0][2]
            musicrating = resultset[0][3]
            self.ratingLabel.setText(str("{0:.2f}".format(musicrating)))
            musicratingcount = resultset[0][4]
            musicgenre = resultset[0][7]
            musiclanguage = resultset[0][8]
            self.detailsTextArea.setPlainText(
                'Music Name : ' + str(musicname) + '\n' + '\n' + 'Music Artist : ' + str(musicartist) + '\n' + '\n' +
                'Music Rating : ' + str("{0:.2f}".format(musicrating)) + '\n' + '\n' + 'Rating count by users :' + str(
                    musicratingcount) + '\n' + '\n' +
                'Music Genre : ' + str(musicgenre) + '\n' + '\n' + 'Music Details : ' + str(
                    musiclanguage)
            )


        elif(contenttpye == 4):
            query4 = "SELECT * FROM series as s, createseriesrel as c WHERE s.series_id = %s AND s.series_id = c.series_id"
            mycursor.execute(query4, (contentid,))
            resultset = mycursor.fetchall()
            seriesname = resultset[0][1]
            seriesrating = resultset[0][2]
            self.ratingLabel.setText(str("{0:.2f}".format(seriesrating)))
            seriesratingcount = resultset[0][3]
            seriesdetails = resultset[0][6]
            seriesgenre = resultset[0][7]
            self.detailsTextArea.setPlainText(
                'Series Name : ' + str(seriesname) + '\n' + '\n' +
                'Series Rating : ' + str("{0:.2f}".format(seriesrating)) + '\n' + '\n' + 'Rating count by users :' + str(
                    seriesratingcount) + '\n' + '\n' +
                'Series Details : ' + str(seriesdetails) + '\n' + '\n' + 'Series Genre : ' + str(
                    seriesgenre)
            )

        else:
            print('nothing')


        mycursor.close()
        self.commentsbox()






    def commentsbox(self):
        contenttype = self.content_type
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gmm"
        )
        mycursor = db.cursor()
        contentid = self.content_id
        userid = self.uId




        if(contenttype == 1):
            query1 = "SELECT g.user_nick,r.commenttext,r.givenrating FROM general_user as g, reviewgame as r WHERE g.user_id = r.user_id AND r.game_id = %s"
            mycursor.execute(query1,(contentid,))
            resultset = mycursor.fetchall()
            totalstring = ""

            for i in range (len(resultset)):
                string = "Review "+ str(i+1) +" : " + "by " +str(resultset[i][0])+ '\n' + "Comment : " +str(resultset[i][1]) + '\n' + "Rating : " + str(resultset[i][2]) + '\n' + "------------------" + '\n'
                totalstring = totalstring + string

            self.commentsTextArea.setPlainText(totalstring)

        elif(contenttype == 2):
            query1 = "SELECT g.user_nick,r.commenttext,r.givenrating FROM general_user as g, reviewmovies as r WHERE g.user_id = r.user_id  AND r.movie_id = %s"
            mycursor.execute(query1, (contentid,))
            resultset = mycursor.fetchall()
            totalstring = ""

            for i in range(len(resultset)):
                string = "Review " + str(i + 1) + " : " + "by " + str(resultset[i][0]) + '\n' + "Comment : " + str(
                    resultset[i][1]) + '\n' + "Rating : " + str(resultset[i][2]) + '\n' + "------------------" + '\n'
                totalstring = totalstring + string

            self.commentsTextArea.setPlainText(totalstring)

        elif(contenttype == 3):
            query1 = "SELECT g.user_nick,r.commenttext,r.givenrating FROM general_user as g, reviewmusic as r WHERE g.user_id = r.user_id  AND r.music_id = %s"
            mycursor.execute(query1, (contentid,))
            resultset = mycursor.fetchall()
            totalstring = ""

            for i in range(len(resultset)):
                string = "Review " + str(i + 1) + " : " + "by " + str(resultset[i][0]) + '\n' + "Comment : " + str(
                    resultset[i][1]) + '\n' + "Rating : " + str(resultset[i][2]) + '\n' + "------------------" + '\n'
                totalstring = totalstring + string

            self.commentsTextArea.setPlainText(totalstring)


        elif(contenttype == 4):
            query1 = "SELECT g.user_nick,r.commenttext,r.givenrating FROM general_user as g, reviewseries as r WHERE g.user_id = r.user_id  AND r.series_id = %s"
            mycursor.execute(query1, (contentid,))
            resultset = mycursor.fetchall()
            totalstring = ""

            for i in range(len(resultset)):
                string = "Review " + str(i + 1) + " : " + "by " + str(resultset[i][0]) + '\n' + "Comment : " + str(
                    resultset[i][1]) + '\n' + "Rating : " + str(resultset[i][2]) + '\n' + "------------------" + '\n'
                totalstring = totalstring + string

            self.commentsTextArea.setPlainText(totalstring)

        else:
            print('nothing')


        mycursor.close()


    def userreview(self):

        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gmm"
        )
        mycursor = db.cursor()
        commenttext = str(self.commentArea.toPlainText())
        givenrate = self.rateSpinBox.value()
        contentid = self.content_id
        contenttype = self.content_type
        userid = self.uId

        msgBox = QMessageBox()
        msgBox.setText("The document has been modified.")
        msgBox.setInformativeText("Do you want to save your changes?")
        msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard)
        msgBox.setDefaultButton(QMessageBox.Save)
        ret = msgBox.exec_()





        if ret == QMessageBox.Save:
            if(contenttype == 1):
                mycursor.callproc('gamereviewpro', (userid, contentid, commenttext, givenrate,))
                db.commit()
                print(mycursor.rowcount, "record inserted")
            if(contenttype == 2):
                mycursor.callproc('moviereviewpro', (userid, contentid, commenttext, givenrate,))
                db.commit()
                print(mycursor.rowcount, "record inserted")
            if(contenttype == 3):
                mycursor.callproc('musicreviewpro', (userid, contentid, commenttext, givenrate,))
                db.commit()
                print(mycursor.rowcount, "record inserted")
            if(contenttype == 4):
                mycursor.callproc('seriesreviewpro', (userid, contentid, commenttext, givenrate,))
                db.commit()
                print(mycursor.rowcount, "record inserted")
            else:
                print('okey')
        elif ret == QMessageBox.Discard:
            print('discard')

        else:
            print('nothing')
        mycursor.close()
    def refreshpage(self):

        self.commentsbox()
        self.review()


    def setupUi(self, singleWindow):
        singleWindow.setObjectName("singleWindow")
        singleWindow.resize(826, 674)
        self.centralwidget = QtWidgets.QWidget(singleWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.contentNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.contentNameLabel.setGeometry(QtCore.QRect(60, 40, 350, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        self.contentNameLabel.setFont(font)
        self.contentNameLabel.setObjectName("contentNameLabel")
        self.typeLabel = QtWidgets.QLabel(self.centralwidget)
        self.typeLabel.setGeometry(QtCore.QRect(650, 50, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.typeLabel.setFont(font)
        self.typeLabel.setObjectName("typeLabel")
        self.ratingLabel = QtWidgets.QLabel(self.centralwidget)
        self.ratingLabel.setGeometry(QtCore.QRect(450, 50, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ratingLabel.setFont(font)
        self.ratingLabel.setObjectName("ratingLabel")
        self.commentArea = QtWidgets.QTextEdit(self.centralwidget)
        self.commentArea.setGeometry(QtCore.QRect(40, 480, 341, 131))
        self.commentArea.setObjectName("commentArea")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(284, 620, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.submitButton.setFont(font)
        self.submitButton.setObjectName("submitButton")
        self.refreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshButton.setGeometry(QtCore.QRect(400, 620, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.refreshButton.setFont(font)
        self.refreshButton.setObjectName("submitButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 470, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 120, 421, 331))
        self.groupBox.setObjectName("groupBox")
        self.detailsTextArea = QtWidgets.QPlainTextEdit(self.groupBox)
        self.detailsTextArea.setGeometry(QtCore.QRect(10, 20, 401, 301))
        self.detailsTextArea.setObjectName("detailsTextArea")
        self.detailsTextArea.isReadOnly()
        self.detailsTextArea.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.detailsTextArea.setPlainText("ajksdasd\naskdlajsdkas")
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.detailsTextArea.setFont(font)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(520, 130, 281, 521))
        self.groupBox_2.setObjectName("groupBox_2")
        self.commentsTextArea = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.commentsTextArea.setGeometry(QtCore.QRect(10, 20, 261, 491))
        self.commentsTextArea.setObjectName("commentsTextArea")
        self.commentsTextArea.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.commentsTextArea.setPlainText("aasdkjasd\nasjdkasdlasd")
        self.commentsTextArea.isReadOnly()
        self.rateSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.rateSpinBox.setGeometry(QtCore.QRect(400, 510, 81, 31))
        self.rateSpinBox.setDecimals(1)
        self.rateSpinBox.setMaximum(10.0)
        self.rateSpinBox.setObjectName("rateSpinBox")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(40, 90, 751, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        singleWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(singleWindow)
        self.getcontenttitle()
        self.getcontentid()
        self.submitButton.clicked.connect(self.userreview)
        self.submitButton.clicked.connect(self.refreshpage)
        #self.refreshButton.clicked.connect(self.refreshpage)
        QtCore.QMetaObject.connectSlotsByName(singleWindow)

    def retranslateUi(self, singleWindow):
        _translate = QtCore.QCoreApplication.translate
        singleWindow.setWindowTitle(_translate("singleWindow", self.single[0]))
        self.contentNameLabel.setText(_translate("singleWindow", "Content Name Here"))
        self.typeLabel.setText(_translate("singleWindow", "Content Type Here"))
        self.ratingLabel.setText(_translate("singleWindow", "Rating Here"))
        self.commentArea.setPlaceholderText(_translate("singleWindow", "Your Comment Here"))
        self.submitButton.setText(_translate("singleWindow", "Submit"))
        self.refreshButton.setText(_translate("singleWindow", "Refresh"))
        self.label_4.setText(_translate("singleWindow", "Your Rating"))
        self.groupBox.setTitle(_translate("singleWindow", "Details"))
        self.groupBox_2.setTitle(_translate("singleWindow", "Comments"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    singleWindow = QtWidgets.QMainWindow()
    ui = Ui_singleWindow()
    ui.setupUi(singleWindow)
    singleWindow.show()
    sys.exit(app.exec_())
