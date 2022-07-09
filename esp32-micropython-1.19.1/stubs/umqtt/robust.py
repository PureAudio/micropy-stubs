"""
Module: 'umqtt.robust' on micropython-esp32-1.19.1
"""
# MCU: {'ver': '1.19.1', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module (spiram) with ESP32', 'release': '1.19.1', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.19.1'}
# Stubber: 1.4.3
from typing import Any


class MQTTClient:
    ''
    def __init__(self, *args) -> None:
        ...

    def connect(self, *args) -> Any:
        ...

    def disconnect(self, *args) -> Any:
        ...

    def log(self, *args) -> Any:
        ...

    DEBUG = False # type: bool
    def set_callback(self, *args) -> Any:
        ...

    def set_last_will(self, *args) -> Any:
        ...

    def ping(self, *args) -> Any:
        ...

    publish : Any ## <class 'closure'> = <closure>
    wait_msg : Any ## <class 'closure'> = <closure>
    def subscribe(self, *args) -> Any:
        ...

    def check_msg(self, *args) -> Any:
        ...

    def delay(self, *args) -> Any:
        ...

    DELAY = 2 # type: int
    reconnect : Any ## <class 'closure'> = <closure>
