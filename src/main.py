import sys
import time
from random import choice

import comport
import design
import serial
from PyQt5.QtCore import QObject, Qt, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QApplication, QMainWindow

current_serial = None
random_data = ["123456", "1234643456", "4234125"]


class ComPortWorker(QObject):
    newCodeRead = pyqtSignal(str)
    dataRead = pyqtSignal(bytes)
    currentPort = None
    buffer = ""

    @pyqtSlot()
    def comReader(self):
        while True:
            if self.currentPort:
                data = self.currentPort.read(15)
                self.dataRead.emit(data)
                self.buffer += data.decode()
                if "\r\n" in self.buffer:
                    code, self.buffer = self.buffer.split("\r\n", 1)
                    self.newCodeRead.emit(str(code))
            else:
                time.sleep(1)

    def switchComPort(self, port):
        if port == self.currentPort:
            return
        if self.currentPort:
            self.currentPort.close()
            self.buffer = ""
        self.currentPort = serial.Serial(port)


class ExampleApp(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.comWorker = ComPortWorker()
        self.comThread = QThread()
        self.comWorker.newCodeRead.connect(self.onNewCode)
        self.comWorker.dataRead.connect(self.onDataRead)
        self.comWorker.moveToThread(self.comThread)
        self.comThread.started.connect(self.comWorker.comReader)
        self.comThread.start()

        self.setupUi(self)
        self.menuCOM.aboutToShow.connect(self.loadComPortMenu)

    def loadComPortMenu(self):
        self.menuCOM.clear()
        ports = comport.get_available_ports()
        if ports:
            for port in ports:
                port_action = QAction(port, self)
                port_action.triggered.connect(lambda: self.comWorker.switchComPort(port))
                self.menuCOM.addAction(port_action)
        else:
            self.menuCOM.addAction(self.no_ports)

    def onNewCode(self, code):
        self.listWidget.addItem(code)

    def onDataRead(self, bt):
        self.textEdit.append(str(bt))


def main():
    app = QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
