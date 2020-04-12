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
        MainWindow.resize(901, 697)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.MainLayout = QtWidgets.QHBoxLayout()
        self.MainLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.MainLayout.setObjectName("MainLayout")
        self.MainInfoLayout = QtWidgets.QVBoxLayout()
        self.MainInfoLayout.setObjectName("MainInfoLayout")
        self.Name = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Name.setFont(font)
        self.Name.setObjectName("Name")
        self.MainInfoLayout.addWidget(self.Name)
        self.StorageType = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.StorageType.setFont(font)
        self.StorageType.setObjectName("StorageType")
        self.MainInfoLayout.addWidget(self.StorageType)
        self.Packaging = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Packaging.setFont(font)
        self.Packaging.setObjectName("Packaging")
        self.MainInfoLayout.addWidget(self.Packaging)
        self.Weight = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Weight.setFont(font)
        self.Weight.setObjectName("Weight")
        self.MainInfoLayout.addWidget(self.Weight)
        self.InputLayout = QtWidgets.QHBoxLayout()
        self.InputLayout.setObjectName("InputLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.InputLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.InputLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.InputLayout.addWidget(self.pushButton)
        self.MainInfoLayout.addLayout(self.InputLayout)
        self.MainLayout.addLayout(self.MainInfoLayout)
        self.BarcodeHistory = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.BarcodeHistory.setFont(font)
        self.BarcodeHistory.setObjectName("BarcodeHistory")
        self.MainLayout.addWidget(self.BarcodeHistory)
        self.MainLayout.setStretch(0, 5)
        self.MainLayout.setStretch(1, 2)
        self.gridLayout.addLayout(self.MainLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 901, 26))
        self.menubar.setObjectName("menubar")
        self.settings = QtWidgets.QMenu(self.menubar)
        self.settings.setObjectName("settings")
        self.menuCOM = QtWidgets.QMenu(self.settings)
        self.menuCOM.setObjectName("menuCOM")
        self.database = QtWidgets.QMenu(self.menubar)
        self.database.setObjectName("database")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.no_ports = QtWidgets.QAction(MainWindow)
        self.no_ports.setEnabled(False)
        self.no_ports.setObjectName("no_ports")
        self.actiontest2 = QtWidgets.QAction(MainWindow)
        self.actiontest2.setObjectName("actiontest2")
        self.loadDb = QtWidgets.QAction(MainWindow)
        self.loadDb.setObjectName("loadDb")
        self.menuCOM.addAction(self.no_ports)
        self.settings.addAction(self.menuCOM.menuAction())
        self.database.addAction(self.loadDb)
        self.menubar.addAction(self.settings.menuAction())
        self.menubar.addAction(self.database.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BarcodeScanner101"))
        self.Name.setText(_translate("MainWindow", "TextLabel"))
        self.StorageType.setText(_translate("MainWindow", "TextLabel"))
        self.Packaging.setText(_translate("MainWindow", "TextLabel"))
        self.Weight.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.settings.setTitle(_translate("MainWindow", "Настройки"))
        self.menuCOM.setTitle(_translate("MainWindow", "COM порт"))
        self.database.setTitle(_translate("MainWindow", "База"))
        self.no_ports.setText(_translate("MainWindow", "(нет доступных портов)"))
        self.actiontest2.setText(_translate("MainWindow", "test2"))
        self.loadDb.setText(_translate("MainWindow", "Загрузить"))
