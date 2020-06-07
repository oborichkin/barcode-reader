import copy
import datetime
import os
import sys
import time
from random import choice

import design
import serial
from comport import ComPortManager
from database import BarcodeDatabase, ProductInfo
from PyQt5.QtCore import QObject, Qt, QThread, QUrl, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtWidgets import QAction, QApplication, QFileDialog, QListWidgetItem, QMainWindow


class ExampleApp(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.db = BarcodeDatabase()

        self.bruh = QSoundEffect()
        self.bruh.setSource(QUrl.fromLocalFile(os.path.join("resources", "bruh.wav")))
        self.bruh.setLoopCount(1)
        self.yuh = QSoundEffect()
        self.yuh.setSource(QUrl.fromLocalFile(os.path.join("resources", "yuh.wav")))
        self.yuh.setLoopCount(1)

        self.comManager = ComPortManager()
        self.comThread = QThread()
        self.comManager.newCodeRead.connect(self.onNewCode)
        self.comManager.moveToThread(self.comThread)
        self.comThread.started.connect(self.comManager.ComReader)
        self.comThread.start()

        self.setupUi(self)
        self.menuCOM.aboutToShow.connect(self.loadComPortMenu)
        self.loadDb.triggered.connect(self.loadNewDatabase)
        self.reloadDb.triggered.connect(self.db.reload)
        self.BarcodeHistory.itemClicked.connect(self.onItemClicked)
        self.BarcodeHistory.currentItemChanged.connect(self.onItemClicked)

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
                    port_action.triggered.connect(lambda *args, portName=port: self.comManager.SwitchComPort(portName))
                self.menuCOM.addAction(port_action)
        else:
            self.menuCOM.addAction(self.no_ports)

    def onNewCode(self, code):
        try:
            product = self.dispatchBarcode(code)
            item = QListWidgetItem(product.name, self.BarcodeHistory)
            item.setData(32, product)
            self.BarcodeHistory.addItem(item)
            self.BarcodeHistory.setCurrentItem(item)
        except Exception:
            pass

    def onItemClicked(self, item):
        product = item.data(32)
        self.Name.setText(str(product.name))
        self.Packaging.setText(str(product.packaging))
        self.Weight.setText(str(product.weight))
        self.StorageType.setText(str(product.storage_type))

    def loadNewDatabase(self):
        fname = QFileDialog.getOpenFileName(self, "Open file", "c:\\", "Database files (*.xls)")
        self.db.read_db_file(fname[0])

    def dispatchBarcode(self, code: str):
        if len(code) == 13:
            return self.db[int(code)]
        elif len(code) == 32:
            code, weight, date = code[:13], code[13:19], code[19:25]
            product = self.db[int(code)]
            product.weight = float(weight)
            product.date = datetime.datetime.strptime(date, "%d%m%Y").date()
            return product
        else:
            raise Exception


def main():
    app = QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
