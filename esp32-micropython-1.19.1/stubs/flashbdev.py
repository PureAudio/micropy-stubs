"""
Module: 'flashbdev' on micropython-esp32-1.19.1
"""
# MCU: {'ver': '1.19.1', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module (spiram) with ESP32', 'release': '1.19.1', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.19.1'}
# Stubber: 1.4.3
from typing import Any


class Partition:
    ''
    def find(self, *args) -> Any:
        ...

    BOOT = 0 # type: int
    RUNNING = 1 # type: int
    TYPE_APP = 0 # type: int
    TYPE_DATA = 1 # type: int
    def get_next_update(self, *args) -> Any:
        ...

    def info(self, *args) -> Any:
        ...

    def ioctl(self, *args) -> Any:
        ...

    @classmethod
    def mark_app_valid_cancel_rollback(cls, *args) -> Any:
        ...

    def readblocks(self, *args) -> Any:
        ...

    def set_boot(self, *args) -> Any:
        ...

    def writeblocks(self, *args) -> Any:
        ...

bdev : Any ## <class 'Partition'> = <Partition type=1, subtype=129, address=2097152, size=2097152, label=vfs, encrypted=0>
