import datetime
import sys
from collections import namedtuple
from typing import Dict, List

import xlrd

ProductInfo = namedtuple(
    "ProductInfo",
    ("name", "storage_type", "packaging", "weight", "date"),
    defaults=(None, None, None, 0, datetime.datetime.now()),
)


class BarcodeDatabase:
    def __init__(self, filepaths: List[str] = list()):
        self._codemap = {}
        self._filepaths = filepaths
        self._fill_database(filepaths)

    def __getitem__(self, key):
        return self._codemap[key]

    def __contains__(self, key):
        return key in self._codemap

    def clear(self):
        self._codemap.clear()

    def reload(self):
        self.clear()
        self._fill_database(self.filepaths)

    def read_db_file(self, filepath: str):
        if filepath.endswith(".xls"):
            self._codemap.update(BarcodeDatabase._from_xls(filepath))
        else:
            raise NotImplementedError

    def _from_xls(filepath: str) -> Dict[int, ProductInfo]:
        result = {}
        rb = xlrd.open_workbook(filepath)
        for sheetidx in range(rb.nsheets):
            sheet = rb.sheet_by_index(sheetidx)
            for rownum in range(1, sheet.nrows):
                values = sheet.row_values(rownum)
                result[int(values[0])] = ProductInfo(*values[1:])
        return result

    def _fill_database(self, filepaths: List[str]):
        for filepath in filepaths:
            self.read_db_file(filepath)


db = BarcodeDatabase(filepaths=sys.argv[1:])
print(db._codemap)
