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
        MainWindow.resize(279, 505)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 256, 451))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 279, 26))
        self.menubar.setObjectName("menubar")
        self.settings = QtWidgets.QMenu(self.menubar)
        self.settings.setObjectName("settings")
        self.menuCOM = QtWidgets.QMenu(self.settings)
        self.menuCOM.setObjectName("menuCOM")
        MainWindow.setMenuBar(self.menubar)
        self.no_ports = QtWidgets.QAction(MainWindow)
        self.no_ports.setEnabled(False)
        self.no_ports.setObjectName("no_ports")
        self.actiontest2 = QtWidgets.QAction(MainWindow)
        self.actiontest2.setObjectName("actiontest2")
        self.menuCOM.addAction(self.no_ports)
        self.settings.addAction(self.menuCOM.menuAction())
        self.menubar.addAction(self.settings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.settings.setTitle(_translate("MainWindow", "Настройки"))
        self.menuCOM.setTitle(_translate("MainWindow", "COM порт"))
        self.no_ports.setText(_translate("MainWindow", "(нет доступных портов)"))
        self.actiontest2.setText(_translate("MainWindow", "test2"))
