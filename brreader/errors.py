class DatabaseException(Exception):
    pass


class NoSuchCode(DatabaseException):
    pass


class ReaderError(Exception):
    pass


class UnsupportedBarcode(ReaderError):
    pass


class InvalidBarcode(ReaderError):
    pass


class ConfigError(Exception):
    pass


class UnsupportedConfig(ConfigError):
    pass
