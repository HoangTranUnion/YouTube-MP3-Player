# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\remin\PycharmProjects\yt_mp3_player\YouTube-MP3-Player\assets\SearchUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SearchWindow(object):
    def setupUi(self, SearchWindow):
        SearchWindow.setObjectName("SearchWindow")
        SearchWindow.resize(710, 449)
        self.centralwidget = QtWidgets.QWidget(SearchWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 711, 31))
        self.label.setObjectName("label")
        self.queryEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.queryEdit.setGeometry(QtCore.QRect(110, 20, 471, 31))
        self.queryEdit.setObjectName("queryEdit")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(600, 20, 91, 31))
        self.searchButton.setObjectName("searchButton")
        self.searchResultBox = QtWidgets.QListWidget(self.centralwidget)
        self.searchResultBox.setGeometry(QtCore.QRect(20, 70, 671, 281))
        self.searchResultBox.setObjectName("searchResultBox")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(20, 370, 671, 31))
        self.addButton.setObjectName("addButton")
        SearchWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SearchWindow)
        self.statusbar.setObjectName("statusbar")
        SearchWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SearchWindow)
        QtCore.QMetaObject.connectSlotsByName(SearchWindow)

    def retranslateUi(self, SearchWindow):
        _translate = QtCore.QCoreApplication.translate
        SearchWindow.setWindowTitle(_translate("SearchWindow", "Search"))
        self.label.setText(_translate("SearchWindow", "Query"))
        self.searchButton.setText(_translate("SearchWindow", "Search"))
        self.addButton.setText(_translate("SearchWindow", "Add Videos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchWindow = QtWidgets.QMainWindow()
    ui = Ui_SearchWindow()
    ui.setupUi(SearchWindow)
    SearchWindow.show()
    sys.exit(app.exec_())
