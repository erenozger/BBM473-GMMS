


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import mysql.connector
from mysql.connector.cursor import MySQLCursor
from PyQt5.QtWidgets import QMessageBox




class Ui_deleteWindow(object):

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

    def search(self):

        searchbar = self.searchBar.toPlainText()

        if self.filterGames.isChecked():
            self.showGroup.clear()
            self.showGroup.setColumnCount(6)
            self.showGroup.setRowCount(1)
            self.showGroup.horizontalHeader().setDefaultSectionSize(160)
            self.showGroup.setHorizontalHeaderLabels(['CONTENT ID','GAME NAME', 'GAME FIRM', 'GAME GENRE','RATING','GAME TYPE'])
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gmm"
            )
            mycursor = db.cursor()

            query = "SELECT g.game_id,g.game_name,g.game_firm,c.contentdetails,g.rating,g.gametype FROM games as g , creategamesrel as c, moderator as m WHERE g.game_id = c.game_id AND c.mod_id = m.mod_id AND g.game_name LIKE %s ORDER BY g.rating DESC;"
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
            self.showGroup.setHorizontalHeaderLabels(['CONTENT ID','MOVIE NAME', 'MOVIE GENRE', 'MOVIE DETAILS', 'RATING'])
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gmm"
            )
            mycursor = db.cursor()

            query = "SELECT m.movie_id,m.movie_name,m.movie_type,c.contentdetails,m.rating FROM movies as m, createmoviesrel as c, moderator as d WHERE m.movie_id = c.movie_id AND c.mod_id = d.mod_id AND m.movie_name LIKE %s ORDER BY m.rating DESC;"
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
            self.showGroup.setHorizontalHeaderLabels(['CONTENT ID','MUSIC NAME', 'MUSIC ARTIST', 'MUSIC GENRE', 'RATING'])

            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gmm"
            )
            mycursor = db.cursor()

            query = "SELECT m.music_id,m.music_name,m.music_artist,c.contentdetails,m.rating FROM music as m, createmusicrel as c, moderator as d WHERE m.music_id = c.music_id AND c.mod_id = d.mod_id AND m.music_name LIKE %s ORDER BY m.rating DESC;"

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
            self.showGroup.setHorizontalHeaderLabels(['CONTENT ID','SERIES NAME', 'SERIES GENRE', 'SERIES DETAILS', 'RATING',])

            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gmm"
            )
            mycursor = db.cursor()

            query = "SELECT s.series_id,s.series_name,c.contenttype,c.contentdetails,s.rating FROM series as s, createseriesrel as c, moderator as m WHERE s.series_id = c.series_id AND c.mod_id = m.mod_id AND s.series_name LIKE %s ORDER BY s.rating DESC;"

            mycursor.execute(query, ("%" + searchbar + "%",))
            result = mycursor.fetchall()
            self.current = result
            self.showGroup.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.showGroup.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.showGroup.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            mycursor.close()

        elif self.filterNews.isChecked():
            self.showGroup.clear()
            self.showGroup.setColumnCount(3)
            self.showGroup.setRowCount(1)
            self.showGroup.horizontalHeader().setDefaultSectionSize(325)
            self.showGroup.setHorizontalHeaderLabels(
                ['NEWS ID ','NEWSTITLE', 'NEWS DETAILS'])
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gmm"
            )
            mycursor = db.cursor()

            query = "SELECT news.news_id,news.newstitle,news.text,news.newsdate FROM news WHERE news.newstitle LIKE  %s ORDER BY newsdate DESC LIMIT 5;"
            mycursor.execute(query,("%" + searchbar + "%",))
            result = mycursor.fetchall()

            self.showGroup.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.showGroup.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.showGroup.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            mycursor.close()

        else:
            self.showGroup.clear()
            self.showGroup.setColumnCount(5)
            self.showGroup.setRowCount(1)# self.showGroup.setRowCount(len(arrayin))
            self.showGroup.horizontalHeader().setDefaultSectionSize(192)
            self.showGroup.setHorizontalHeaderLabels(['NAME', 'GENRE','TYPE', 'RATING', 'CONTENT ID'])
            self.Warning("alert", "Please choose the filter. ")
            print("nothing")


    def deletefunc(self):
        msgBox = QMessageBox()
        msgBox.setText("                                The content has been deleted.                              ")
        msgBox.setInformativeText("\n                           Do you want to save your changes?                           \n"" \"Reminder you have to choose filter same as its content type \"")
        msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard)
        msgBox.setDefaultButton(QMessageBox.Save)
        ret = msgBox.exec_()
        deletebar = self.deleteBar.toPlainText()

        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gmm"
        )
        mycursor = db.cursor()

        if ret == QMessageBox.Save:
            if self.filterGames.isChecked():
                query = "SELECT * FROM games WHERE game_id = %s"
                mycursor.execute(query,(deletebar,))
                if (len(mycursor.fetchall()) > 0):
                    self.Messagebox("Congrats", "Content deleted")
                    deletequery = "DELETE FROM games WHERE game_id = %s"
                    mycursor.execute(deletequery,(deletebar,))
                    db.commit()
                else:
                    self.Warning("Alert", "Incorrect content id please try again")



            elif self.filterMovies.isChecked():
                query = "SELECT * FROM movies WHERE movie_id = %s"
                mycursor.execute(query, (deletebar,))
                if (len(mycursor.fetchall()) > 0):
                    self.Messagebox("Congrats", "Content deleted")
                    deletequery = "DELETE FROM movies WHERE movie_id = %s"
                    mycursor.execute(deletequery, (deletebar,))
                    db.commit()

                else:
                    self.Warning("Alert", "Incorrect content id please try again")





            elif self.filterMusic.isChecked():
                query = "SELECT * FROM music WHERE music_id = %s"
                mycursor.execute(query, (deletebar,))
                if (len(mycursor.fetchall()) > 0):
                    self.Messagebox("Congrats", "Content deleted")
                    deletequery = "DELETE FROM music WHERE music_id = %s"
                    mycursor.execute(deletequery, (deletebar,))
                    db.commit()

                else:
                    self.Warning("Alert", "Incorrect content id please try again")


            elif self.filterSeries.isChecked():
                query = "SELECT * FROM series WHERE series_id = %s"
                mycursor.execute(query, (deletebar,))
                if (len(mycursor.fetchall()) > 0):
                    self.Messagebox("Congrats", "Content deleted")
                    deletequery = "DELETE FROM series WHERE series_id = %s"
                    mycursor.execute(deletequery, (deletebar,))
                    db.commit()

                else:
                    self.Warning("Alert", "Incorrect content id please try again")


            elif self.filterNews.isChecked():
                query = "SELECT * FROM news WHERE news_id = %s"
                mycursor.execute(query, (deletebar,))
                if (len(mycursor.fetchall()) > 0):
                    self.Messagebox("Congrats", "Content deleted")
                    deletequery = "DELETE FROM news WHERE news_id = %s"
                    mycursor.execute(deletequery, (deletebar,))
                    db.commit()

                else:
                    self.Warning("Alert", "Incorrect content id please try again")


            else:
                self.Warning("alert", "Please choose the filter. ")







    def setupUi(self, deleteWindow):

        deleteWindow.setObjectName("deleteWindow")
        deleteWindow.resize(1063, 500)
        deleteWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(deleteWindow)
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
        self.label_3.setGeometry(QtCore.QRect(20, 400, 350, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 1011, 111))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")


        self.DELETE = QtWidgets.QPushButton(self.centralwidget)
        self.DELETE.setGeometry(QtCore.QRect(200, 450, 121, 31))
        self.DELETE.setObjectName("DELETE")
        self.searchFilterGroup = QtWidgets.QGroupBox(self.groupBox)
        self.searchFilterGroup.setGeometry(QtCore.QRect(10, 40, 701, 61))
        self.searchFilterGroup.setObjectName("searchFilterGroup")
        self.filterMovies = QtWidgets.QRadioButton(self.searchFilterGroup)
        self.filterMovies.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.filterMovies.setObjectName("filterMovies")
        self.filterSeries = QtWidgets.QRadioButton(self.searchFilterGroup)
        self.filterSeries.setGeometry(QtCore.QRect(90, 30, 82, 17))
        self.filterSeries.setObjectName("filterSeries")
        self.filterGames = QtWidgets.QRadioButton(self.searchFilterGroup)
        self.filterGames.setGeometry(QtCore.QRect(190, 30, 82, 17))
        self.filterGames.setObjectName("filterGames")
        self.filterMusic = QtWidgets.QRadioButton(self.searchFilterGroup)
        self.filterMusic.setGeometry(QtCore.QRect(290, 30, 82, 17))
        self.filterMusic.setObjectName("filterMusic")
        self.filterNews = QtWidgets.QRadioButton(self.searchFilterGroup)
        self.filterNews.setGeometry(QtCore.QRect(375, 30, 82, 17))
        self.filterNews.setObjectName("filterMusic")
        self.searchBar = QtWidgets.QTextEdit(self.searchFilterGroup)
        self.searchBar.setGeometry(QtCore.QRect(480, 20, 181, 31))
        self.searchBar.setObjectName("searchBar")
        self.deleteBar = QtWidgets.QTextEdit(self.centralwidget)
        self.deleteBar.setGeometry(QtCore.QRect(20, 450, 150, 31))
        self.deleteBar.setObjectName("searchBar")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.showGroup = QtWidgets.QTableWidget(self.centralwidget)
        self.showGroup.setGeometry(QtCore.QRect(20, 150, 1001, 231))
        self.showGroup.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.showGroup.setGridStyle(QtCore.Qt.DashLine)
        self.showGroup.setRowCount(10)
        self.showGroup.setColumnCount(5)
        self.showGroup.setObjectName("showGroup")
        self.showGroup.horizontalHeader().setDefaultSectionSize(192)

        self.DELETE.clicked.connect(self.deletefunc)
        self.searchBar.textChanged.connect(self.search)

        deleteWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(deleteWindow)

        QtCore.QMetaObject.connectSlotsByName(deleteWindow)

    def retranslateUi(self, deleteWindow):
        _translate = QtCore.QCoreApplication.translate
        deleteWindow.setWindowTitle(_translate("deleteWindow", "CONTENT DELETE PAGE"))
        self.label.setText(_translate("deleteWindow", "Contents"))
        self.label_2.setText(_translate("deleteWindow", "Latest Uploaded Games"))
        self.label_3.setText(_translate("deleteWindow", "Enter the content id what you want to delete"))

        self.DELETE.setText(_translate("deleteWindow", "DELETE"))


        self.searchFilterGroup.setTitle(_translate("deleteWindow", "Filter"))
        self.filterMovies.setText(_translate("deleteWindow", "Movies"))
        self.filterSeries.setText(_translate("deleteWindow", "TV Series"))
        self.filterGames.setText(_translate("deleteWindow", "Games"))
        self.filterMusic.setText(_translate("deleteWindow", "Music"))
        self.filterNews.setText(_translate("deleteWindow", "News"))
        self.searchBar.setPlaceholderText(_translate("deleteWindow", "Search by content name"))
        self.deleteBar.setPlaceholderText(_translate("deleteWindow", "Content id"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    deleteWindow = QtWidgets.QMainWindow()
    ui = Ui_deleteWindow()
    ui.setupUi(deleteWindow)
    deleteWindow.show()
    sys.exit(app.exec_())