# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'singlenews.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SingleNews(object):
    newsTitle = ""
    newsDetails = ""

    def __init__(self,newsTitle_,newsDetails_,authorname_,authornick_,newsdate_):
        self.newsTitle = newsTitle_
        self.newsDetails = newsDetails_
        self.authorname = authorname_
        self.authornick = authornick_
        self.newsdate = newsdate_

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(786, 628)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 20, 350, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText(self.newsTitle)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(90, 110, 631, 411))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setPlainText(self.newsDetails)
        self.plainTextEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 540, 200, 31))
        self.label_2.setObjectName("label_2")
        self.label_2.setText(self.authorname)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", self.newsTitle + '\n'+ 'Date :' + str(self.newsdate)))
        self.label_2.setText(_translate("MainWindow", "Author : " + self.authorname + " / " + self.authornick))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_SingleNews()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
