# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\src\design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.currentPositionName = QtWidgets.QLabel(self.centralwidget)
        self.currentPositionName.setGeometry(QtCore.QRect(30, 30, 81, 21))
        self.currentPositionName.setObjectName("currentPositionName")
        self.currentPositionWeight = QtWidgets.QLabel(self.centralwidget)
        self.currentPositionWeight.setGeometry(QtCore.QRect(30, 60, 81, 21))
        self.currentPositionWeight.setObjectName("currentPositionWeight")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(520, 10, 256, 192))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.settings = QtWidgets.QMenu(self.menubar)
        self.settings.setObjectName("settings")
        self.menuCOM = QtWidgets.QMenu(self.settings)
        self.menuCOM.setObjectName("menuCOM")
        MainWindow.setMenuBar(self.menubar)
        self.no_ports = QtWidgets.QAction(MainWindow)
        self.no_ports.setEnabled(False)
        self.no_ports.setObjectName("no_ports")
        self.menuCOM.addAction(self.no_ports)
        self.settings.addAction(self.menuCOM.menuAction())
        self.menubar.addAction(self.settings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.currentPositionName.setText(_translate("MainWindow", "Название"))
        self.currentPositionWeight.setText(_translate("MainWindow", "Вес"))
        self.settings.setTitle(_translate("MainWindow", "Настройки"))
        self.menuCOM.setTitle(_translate("MainWindow", "COM порт"))
        self.no_ports.setText(_translate("MainWindow", "(нет доступных портов)"))
