import json

from PyQt5.QtCore import QObject, pyqtSignal


class AppConfig(QObject):
    dbFileChanged = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._db_file = None

    def read_config(self, filename):
        with open(filename, "r") as f:
            config = json.load(f)
        self.db_file = config.get("db_file")

    @property
    def db_file(self):
        return self._db_file

    @db_file.setter
    def db_file(self, value):
        self._db_file = value
        self.dbFileChanged.emit(self._db_file)
