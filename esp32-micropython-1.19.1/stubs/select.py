"""
Module: 'select' on micropython-esp32-1.19.1
"""
# MCU: {'ver': '1.19.1', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module (spiram) with ESP32', 'release': '1.19.1', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.19.1'}
# Stubber: 1.4.3
from typing import Any

POLLERR = 8 # type: int
POLLHUP = 16 # type: int
POLLIN = 1 # type: int
POLLOUT = 4 # type: int
def poll(*args) -> Any:
    ...

def select(*args) -> Any:
    ...

