import json
import configparser

from errors import ConfigError, UnsupportedConfig

from PyQt5.QtCore import QObject, pyqtSignal


class AppConfig(QObject):
    dbFileChanged = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._db_file = None

    def read_config(self, filename: str):
        config = configparser.ConfigParser()
        config.read(filename)
        self.db_file = config["DB"]["Path"]
        self.report_file = config["Output"]["TextReport"]
        self.full_report_file = config["Output"]["FullTextReport"]
        self.xls_report_file = config["Output"]["XlsReport"]
        self.full_xls_report_file = config["Output"]["FullXlsReport"]
        self.port = config["Input"]["Port"]

    @property
    def db_file(self):
        return self._db_file

    @db_file.setter
    def db_file(self, value):
        self._db_file = value
        self.dbFileChanged.emit(self._db_file)
