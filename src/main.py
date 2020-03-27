import sys
from random import choice

import comport
import design
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QApplication, QMainWindow

current_serial = None
random_data = ["123456", "1234643456", "4234125"]


class ExampleApp(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.menuCOM.aboutToShow.connect(self.test)

    def test(self):
        self.menuCOM.clear()
        ports = comport.get_available_ports()
        if ports:
            for port in ports:
                self.menuCOM.addAction(port)
        else:
            self.menuCOM.addAction(self.no_ports)


def main():
    app = QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
