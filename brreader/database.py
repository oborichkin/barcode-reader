import datetime
import sys
from collections import namedtuple
from typing import Dict, List

from errors import NoSuchCode

import xlrd

ProductInfo = namedtuple(
    "ProductInfo",
    ("name", "storage_type", "packaging", "weight", "date"),
    defaults=(None, None, None, 0, datetime.datetime.now()),
)


class Item:

    def __init__(self, prod_info: ProductInfo):
        self.name = prod_info.name
        self.storage_type = prod_info.storage_type
        self.packaging = prod_info.packaging
        self.weight = prod_info.weight
        self.date = prod_info.date


class BarcodeDatabase:
    def __init__(self, filepaths: List[str] = list()):
        self._codemap = {}
        self._filepaths = filepaths
        self._fill_database(filepaths)

    def __getitem__(self, key):
        if key in self:
            return self._codemap[key]
        else:
            raise NoSuchCode(f"No such barcode in database {key}")

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
