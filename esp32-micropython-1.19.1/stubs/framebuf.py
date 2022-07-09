"""
Module: 'framebuf' on micropython-esp32-1.19.1
"""
# MCU: {'ver': '1.19.1', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module (spiram) with ESP32', 'release': '1.19.1', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.19.1'}
# Stubber: 1.4.3
from typing import Any


class FrameBuffer:
    ''
    def blit(self, *args) -> Any:
        ...

    def fill(self, *args) -> Any:
        ...

    def fill_rect(self, *args) -> Any:
        ...

    def hline(self, *args) -> Any:
        ...

    def line(self, *args) -> Any:
        ...

    def pixel(self, *args) -> Any:
        ...

    def rect(self, *args) -> Any:
        ...

    def scroll(self, *args) -> Any:
        ...

    def text(self, *args) -> Any:
        ...

    def vline(self, *args) -> Any:
        ...

def FrameBuffer1(*args) -> Any:
    ...

GS2_HMSB = 5 # type: int
GS4_HMSB = 2 # type: int
GS8 = 6 # type: int
MONO_HLSB = 3 # type: int
MONO_HMSB = 4 # type: int
MONO_VLSB = 0 # type: int
MVLSB = 0 # type: int
RGB565 = 1 # type: int
