import serial

ports = [f"COM{i + 1}" for i in range(256)]


def get_available_ports():
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result
