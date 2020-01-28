# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addcontent.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from addgame import *
from addmovie import *
from addmusic import *
from addseries import *
from delete import *


class Ui_MainWindowC(object):
    def deleteContent(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_deleteWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def addGame(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowG()
        self.ui.setupUi(self.window)
        self.window.show()

    def addMovie(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowMov()
        self.ui.setupUi(self.window)
        self.window.show()

    def addMusic(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowM()
        self.ui.setupUi(self.window)
        self.window.show()

    def addSeries(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowS()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(240, 320)
        MainWindow.setMinimumSize(QtCore.QSize(240, 320))
        MainWindow.setMaximumSize(QtCore.QSize(240, 320))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addSeriesB = QtWidgets.QPushButton(self.centralwidget)
        self.addSeriesB.setGeometry(QtCore.QRect(50, 140, 141, 41))
        self.addSeriesB.setObjectName("addSeriesB")
        self.addSeriesB.clicked.connect(self.addSeries)
        self.addMusicB = QtWidgets.QPushButton(self.centralwidget)
        self.addMusicB.setGeometry(QtCore.QRect(50, 200, 141, 41))
        self.addMusicB.setObjectName("addMusicB")
        self.addMusicB.clicked.connect(self.addMusic)
        self.addGameB = QtWidgets.QPushButton(self.centralwidget)
        self.addGameB.setGeometry(QtCore.QRect(50, 80, 141, 41))
        self.addGameB.setObjectName("addGameB")
        self.addGameB.clicked.connect(self.addGame)
        self.addMovieB = QtWidgets.QPushButton(self.centralwidget)
        self.addMovieB.setGeometry(QtCore.QRect(50, 20, 141, 41))
        self.addMovieB.setObjectName("addMovieB")
        self.addMovieB.clicked.connect(self.addMovie)
        self.deleteB = QtWidgets.QPushButton(self.centralwidget)
        self.deleteB.setGeometry(QtCore.QRect(50, 260, 141, 41))
        self.deleteB.setObjectName("deleteB")
        self.deleteB.clicked.connect(self.deleteContent)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addSeriesB.setText(_translate("MainWindow", "Add TV Series"))
        self.addMusicB.setText(_translate("MainWindow", "Add Music"))
        self.addGameB.setText(_translate("MainWindow", "Add Game"))
        self.addMovieB.setText(_translate("MainWindow", "Add Movie"))
        self.deleteB.setText(_translate("MainWindow", "Delete Content"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowC()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
