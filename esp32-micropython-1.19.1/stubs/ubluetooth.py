"""
Module: 'ubluetooth' on micropython-esp32-1.19.1
"""
# MCU: {'ver': '1.19.1', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module (spiram) with ESP32', 'release': '1.19.1', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.19.1'}
# Stubber: 1.4.3
from typing import Any


class BLE:
    ''
    def active(self, *args) -> Any:
        ...

    def config(self, *args) -> Any:
        ...

    def gap_advertise(self, *args) -> Any:
        ...

    def gap_connect(self, *args) -> Any:
        ...

    def gap_disconnect(self, *args) -> Any:
        ...

    def gap_scan(self, *args) -> Any:
        ...

    def gattc_discover_characteristics(self, *args) -> Any:
        ...

    def gattc_discover_descriptors(self, *args) -> Any:
        ...

    def gattc_discover_services(self, *args) -> Any:
        ...

    def gattc_exchange_mtu(self, *args) -> Any:
        ...

    def gattc_read(self, *args) -> Any:
        ...

    def gattc_write(self, *args) -> Any:
        ...

    def gatts_indicate(self, *args) -> Any:
        ...

    def gatts_notify(self, *args) -> Any:
        ...

    def gatts_read(self, *args) -> Any:
        ...

    def gatts_register_services(self, *args) -> Any:
        ...

    def gatts_set_buffer(self, *args) -> Any:
        ...

    def gatts_write(self, *args) -> Any:
        ...

    def irq(self, *args) -> Any:
        ...

FLAG_INDICATE = 32 # type: int
FLAG_NOTIFY = 16 # type: int
FLAG_READ = 2 # type: int
FLAG_WRITE = 8 # type: int
FLAG_WRITE_NO_RESPONSE = 4 # type: int

class UUID:
    ''
