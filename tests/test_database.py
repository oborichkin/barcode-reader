from brreader.database import BarcodeDatabase


def test_barcode_database_init():
    db = BarcodeDatabase()
    assert db
