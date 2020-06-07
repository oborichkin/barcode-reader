from brreader.comport import ComPortManager


def test_comport_manager_init():
    cpm = ComPortManager()
    assert cpm
