import copy
import sys
import time
from random import choice

import design
import serial
from comport import ComPortManager
from PyQt5.QtCore import QObject, Qt, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QApplication, QMainWindow


class ExampleApp(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.comManager = ComPortManager()
        self.comThread = QThread()
        self.comManager.newCodeRead.connect(self.onNewCode)
        self.comManager.moveToThread(self.comThread)
        self.comThread.started.connect(self.comManager.ComReader)
        self.comThread.start()

        self.setupUi(self)
        self.menuCOM.aboutToShow.connect(self.loadComPortMenu)

    def loadComPortMenu(self):
        self.menuCOM.clear()
        ports = self.comManager.GetPortsList()
        if ports:
            for port, enabled in ports.items():
                port_action = self.menuCOM.addAction(port)
                port_action.setCheckable(True)
                if enabled:
                    port_action.setChecked(True)
                else:
                    receiver = lambda *args, portName=port: self.comManager.SwitchComPort(portName)
                    port_action.triggered.connect(receiver)
                self.menuCOM.addAction(port_action)
        else:
            self.menuCOM.addAction(self.no_ports)

    def onNewCode(self, code):
        self.listWidget.addItem(code)


def main():
    app = QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
