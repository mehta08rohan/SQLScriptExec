# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc


class Ui_MainWindow(object):

    global dblist
    dblist=[]
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 751, 481))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(330, 170, 261, 41))
        self.comboBox.setObjectName("comboBox")

        for i in dblist:
            self.comboBox.addItem(i)

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 170, 221, 31))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        # self.getDatabasesNames('localhost')

        QtCore.QMetaObject.connectSlotsByName(MainWindow)





    def getDatabasesNames(self,server,db='master'):

        connSqlServer = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; \
                    SERVER='+ server +'; \
                    DATABASE = '+ db +';\
                    Trusted_Connection=yes;')

        cursor = connSqlServer.cursor()
        cursor.execute('SELECT * From master.dbo.sysdatabases')
        for row in cursor:
            if row[0] not in ['master','tempdb','model','msdb']:
                dblist.append(row[0])

        cursor.close()
        connSqlServer.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Sql Exec"))
        self.label.setText(_translate("MainWindow", "Select Database"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.getDatabasesNames('localhost')
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
