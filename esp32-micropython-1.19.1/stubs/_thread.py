"""
Module: '_thread' on micropython-esp32-1.19.1
"""
# MCU: {'ver': '1.19.1', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module (spiram) with ESP32', 'release': '1.19.1', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.19.1'}
# Stubber: 1.4.3
from typing import Any


class LockType:
    ''
    def acquire(self, *args) -> Any:
        ...

    def locked(self, *args) -> Any:
        ...

    def release(self, *args) -> Any:
        ...

def allocate_lock(*args) -> Any:
    ...

def exit(*args) -> Any:
    ...

def get_ident(*args) -> Any:
    ...

def stack_size(*args) -> Any:
    ...

def start_new_thread(*args) -> Any:
    ...

