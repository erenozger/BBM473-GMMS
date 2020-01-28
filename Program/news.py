# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'news.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import pymysql
import PyQt5
import pymysql.cursors

class Ui_window2(object):
    newswriter_id = 0
    def __init__(self,newsid):
        self.newswriter_id = int(newsid)
    def submit(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gmm"
        )
        mycursor = db.cursor()

        dbtitle = self.title.text()
        details = self.details.toPlainText()
        details = details.replace('\n',' ').replace('\r',' ')
        newswriterid1 = self.newswriterid.text()
        newswriter_id = int(newswriterid1)

        query = "SELECT news_writer.writer_id FROM news_writer WHERE writer_id=%s"
        data = mycursor.execute(query, (newswriter_id,))


        if (len(mycursor.fetchall()) > 0):
            mycursor.callproc('addnews',(newswriter_id, dbtitle, details,))
            db.commit()
            print(mycursor.rowcount, "record inserted")
            self.Messagebox("congrats", "Successful")
        else:
            self.Warning("alert", "ID is Wrong!")



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


    def setupUi(self, window2):
        window2.setObjectName("window2")
        window2.resize(891, 670)
        window2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(window2)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLineEdit(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(160, 70, 401, 41))
        self.title.setObjectName("title")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 30, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 120, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(370, 600, 151, 51))
        self.submitButton.setObjectName("submitButton")
        self.submitButton.clicked.connect(self.submit)
        self.details = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.details.setGeometry(QtCore.QRect(160, 170, 620, 350))
        self.details.setObjectName("details")
        self.newswriterid = QtWidgets.QLineEdit(self.centralwidget)
        self.newswriterid.setGeometry(QtCore.QRect(160, 550,150, 30))
        self.newswriterid.setObjectName("newswriterid")
        window2.setCentralWidget(self.centralwidget)

        self.retranslateUi(window2)
        QtCore.QMetaObject.connectSlotsByName(window2)

    def retranslateUi(self, window2):
        _translate = QtCore.QCoreApplication.translate
        window2.setWindowTitle(_translate("window2", "WRITE NEWS"))
        self.label.setText(_translate("window2", "New\'s Title"))
        self.label_2.setText(_translate("window2", "New\'s Details"))
        self.submitButton.setText(_translate("window2", "Submit"))
        self.newswriterid.setPlaceholderText(_translate("window2", "newswriterid"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window2 = QtWidgets.QMainWindow()
    ui = Ui_window2()
    ui.setupUi(window2)
    window2.show()
    sys.exit(app.exec_())
