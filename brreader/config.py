import json

from PyQt5.QtCore import QObject, pyqtSignal


class AppConfig(QObject):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dbFilesChanged = pyqtSignal()
        self._db_files = None

    def read_config(self, filename):
        with open(filename, "r") as f:
            config = json.load(f)
        self.db_files = config.get("db_files")

    @property
    def db_files(self):
        return self._db_files

    @db_files.setter
    def db_files(self, value):
        self._db_files = value
        self.dbFilesChanged.emit()
