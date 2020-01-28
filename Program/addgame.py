# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addgame.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import pymysql
import PyQt5
import pymysql.cursors
from main import *

class Ui_MainWindowG(object):
    def addGame(self):

        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gmm"
        )
        mycursor = db.cursor()


        game_name = self.gameName.text()
        game_firm = self.gameFirm.text()
        rating = 0
        game_type = self.gameType.text()
        mod_id1 = self.modId.text()
        mod_id = int(mod_id1)

        game_language = self.gameLanguage.text()

        if self.pcRadioB.isChecked():
            game_platform = 'pc'
        elif self.consoleRadioB.isChecked():
            game_platform = 'console'
        elif self.mobileRadioB.isChecked():
            game_platform = 'mobile'
        else:
            game_platform = 'no platform'
        query = "SELECT moderator.mod_id FROM moderator WHERE mod_id=%s"
        data = mycursor.execute(query, (mod_id1,))
        print(data)
        if (len(mycursor.fetchall()) > 0):
            mycursor.callproc('addgame',
            (mod_id, game_name, game_firm, rating, game_platform, game_type, game_language,))
            db.commit()
            print(mycursor.rowcount, "record inserted")
            self.Messagebox("congrats", "Oyun eklenmistir")
            
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
        MainWindow.resize(464, 413)
        MainWindow.setMinimumSize(QtCore.QSize(464, 413))
        MainWindow.setMaximumSize(QtCore.QSize(464, 413))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pcRadioB = QtWidgets.QRadioButton(self.centralwidget)
        self.pcRadioB.setGeometry(QtCore.QRect(80, 40, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pcRadioB.setFont(font)
        self.pcRadioB.setObjectName("pcRadioB")
        self.consoleRadioB = QtWidgets.QRadioButton(self.centralwidget)
        self.consoleRadioB.setGeometry(QtCore.QRect(200, 40, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.consoleRadioB.setFont(font)
        self.consoleRadioB.setObjectName("consoleRadioB")
        self.mobileRadioB = QtWidgets.QRadioButton(self.centralwidget)
        self.mobileRadioB.setGeometry(QtCore.QRect(330, 40, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mobileRadioB.setFont(font)
        self.mobileRadioB.setObjectName("mobileRadioB")
        self.gameName = QtWidgets.QLineEdit(self.centralwidget)
        self.gameName.setGeometry(QtCore.QRect(80, 90, 321, 41))
        self.gameName.setObjectName("gameName")
        self.gameFirm = QtWidgets.QLineEdit(self.centralwidget)
        self.gameFirm.setGeometry(QtCore.QRect(80, 140, 321, 41))
        self.gameFirm.setObjectName("gameFirm")
        self.gameType = QtWidgets.QLineEdit(self.centralwidget)
        self.gameType.setGeometry(QtCore.QRect(80, 190, 321, 41))
        self.gameType.setText("")
        self.gameType.setObjectName("gameType")
        self.gameLanguage = QtWidgets.QLineEdit(self.centralwidget)
        self.gameLanguage.setGeometry(QtCore.QRect(80, 240, 321, 31))
        self.gameLanguage.setObjectName("gameLanguage")
        self.modId = QtWidgets.QLineEdit(self.centralwidget)
        self.modId.setGeometry(QtCore.QRect(80, 280, 121, 31))
        self.modId.setObjectName("modId")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 320, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.addGame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pcRadioB.setText(_translate("MainWindow", "PC"))
        self.consoleRadioB.setText(_translate("MainWindow", "Console"))
        self.mobileRadioB.setText(_translate("MainWindow", "Mobile"))
        self.gameName.setPlaceholderText(_translate("MainWindow", "Game Name"))
        self.gameFirm.setPlaceholderText(_translate("MainWindow", "Game Firm"))
        self.gameType.setPlaceholderText(_translate("MainWindow", "Game Type"))
        self.gameLanguage.setPlaceholderText(_translate("MainWindow", "Game Language"))
        self.modId.setPlaceholderText(_translate("MainWindow", "Mod Id"))
        self.pushButton.setText(_translate("MainWindow", "Add Game"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowG()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
