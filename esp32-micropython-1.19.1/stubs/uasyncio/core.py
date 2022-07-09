"""
Module: 'uasyncio.core' on micropython-esp32-1.19.1
"""
# MCU: {'ver': '1.19.1', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module (spiram) with ESP32', 'release': '1.19.1', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.19.1'}
# Stubber: 1.4.3
from typing import Any


class CancelledError:
    ''

class Task:
    ''

class TaskQueue:
    ''
    def pop(self, *args) -> Any:
        ...

    def remove(self, *args) -> Any:
        ...

    def peek(self, *args) -> Any:
        ...

    def push(self, *args) -> Any:
        ...

def run(*args) -> Any:
    ...

def sleep(*args) -> Any:
    ...

def sleep_ms(*args) -> Any:
    ...

def ticks_add(*args) -> Any:
    ...

def ticks_diff(*args) -> Any:
    ...


class TimeoutError:
    ''

class SingletonGenerator:
    ''
    def __init__(self, *args) -> None:
        ...


class IOQueue:
    ''
    def __init__(self, *args) -> None:
        ...

    def remove(self, *args) -> Any:
        ...

    def wait_io_event(self, *args) -> Any:
        ...

    def queue_read(self, *args) -> Any:
        ...

    def queue_write(self, *args) -> Any:
        ...


class Loop:
    ''
    def close(self, *args) -> Any:
        ...

    def stop(self, *args) -> Any:
        ...

    def create_task(self, *args) -> Any:
        ...

    def run_until_complete(self, *args) -> Any:
        ...

    def call_exception_handler(self, *args) -> Any:
        ...

    def run_forever(self, *args) -> Any:
        ...

    def set_exception_handler(self, *args) -> Any:
        ...

    def get_exception_handler(self, *args) -> Any:
        ...

    def default_exception_handler(self, *args) -> Any:
        ...

def create_task(*args) -> Any:
    ...

def run_until_complete(*args) -> Any:
    ...

def get_event_loop(*args) -> Any:
    ...

def current_task(*args) -> Any:
    ...

def new_event_loop(*args) -> Any:
    ...

def ticks(*args) -> Any:
    ...

