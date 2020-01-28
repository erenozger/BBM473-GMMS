# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addmovie.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from main import *


class Ui_MainWindowMov(object):
    def addMovie(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gmm"
        )
        mycursor = db.cursor()

        movieName = self.movName.text()
        movieDetails = self.movDetails.text()
        type = self.movType.text()
        mod_id1 = self.modId.text()
        rating = 0
        movieLanguage = self.movLanguage.text()
        mod_id = int(mod_id1)
        query = "SELECT moderator.mod_id FROM moderator WHERE mod_id=%s"
        data = mycursor.execute(query, (mod_id1,))
        print(data)

        if (len(mycursor.fetchall()) > 0):
            mycursor.callproc('addmovie',
                              (mod_id, movieName, type, rating, movieDetails, movieLanguage,))
            db.commit()
            print(mycursor.rowcount, "record inserted")
            self.Messagebox("congrats", "Movie eklenmistir")
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
        MainWindow.resize(445, 381)
        MainWindow.setMinimumSize(QtCore.QSize(445, 381))
        MainWindow.setMaximumSize(QtCore.QSize(445, 381))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.movName = QtWidgets.QLineEdit(self.centralwidget)
        self.movName.setGeometry(QtCore.QRect(80, 40, 271, 41))
        self.movName.setObjectName("movName")
        self.movDetails = QtWidgets.QLineEdit(self.centralwidget)
        self.movDetails.setGeometry(QtCore.QRect(80, 100, 271, 91))
        self.movDetails.setObjectName("movDetails")
        self.movType = QtWidgets.QLineEdit(self.centralwidget)
        self.movType.setGeometry(QtCore.QRect(80, 200, 271, 30))
        self.movType.setObjectName("movType")
        self.movLanguage = QtWidgets.QLineEdit(self.centralwidget)
        self.movLanguage.setGeometry(QtCore.QRect(80, 240, 271, 30))
        self.movLanguage.setObjectName("movLanguage")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 320, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.addMovie)
        self.modId = QtWidgets.QLineEdit(self.centralwidget)
        self.modId.setGeometry(QtCore.QRect(80, 280, 131, 30))
        self.modId.setObjectName("modId")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.movName.setPlaceholderText(_translate("MainWindow", "Movie Name"))
        self.movDetails.setPlaceholderText(_translate("MainWindow", "Movie Details"))
        self.movType.setPlaceholderText(_translate("MainWindow", "Movie Type"))
        self.movLanguage.setPlaceholderText(_translate("MainWindow", "Movie Language"))
        self.pushButton.setText(_translate("MainWindow", "Add Movie"))
        self.modId.setPlaceholderText(_translate("MainWindow", "Mod Id"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowMov()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
