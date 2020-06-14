import os
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot


class Session(QObject):
    sessionItemRestore = pyqtSignal(str)

    SESSION_FILE = ".session"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.session_data = None

    def init_session(self):
        if os.path.isfile(self.SESSION_FILE):
            self.session_data = self._restore_session()
        else:
            self.session_data = open(self.SESSION_FILE, "w+")

    def _restore_session(self):
        with open(self.SESSION_FILE, "r") as f:
            for line in f:
                self.sessionItemRestore.emit(line.strip())
        return open(self.SESSION_FILE, "a")

    @pyqtSlot()
    def clear(self):
        self.session_data.close()
        self.session_data = open(self.SESSION_FILE, "w+")

    @pyqtSlot(str)
    def new_item(self, code):
        self.session_data.write(f"{str(code)}\n")
