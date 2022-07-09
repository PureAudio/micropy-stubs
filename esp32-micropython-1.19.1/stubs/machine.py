"""
Module: 'machine' on micropython-esp32-1.19.1
"""
# MCU: {'ver': '1.19.1', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module (spiram) with ESP32', 'release': '1.19.1', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.19.1'}
# Stubber: 1.4.3
from typing import Any


class ADC:
    ''
    def read(self, *args) -> Any:
        ...

    ATTN_0DB = 0 # type: int
    ATTN_11DB = 3 # type: int
    ATTN_2_5DB = 1 # type: int
    ATTN_6DB = 2 # type: int
    WIDTH_10BIT = 10 # type: int
    WIDTH_11BIT = 11 # type: int
    WIDTH_12BIT = 12 # type: int
    WIDTH_9BIT = 9 # type: int
    def atten(self, *args) -> Any:
        ...

    def block(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...

    def read_u16(self, *args) -> Any:
        ...

    def read_uv(self, *args) -> Any:
        ...

    def width(self, *args) -> Any:
        ...


class ADCBlock:
    ''
    def connect(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...


class DAC:
    ''
    def write(self, *args) -> Any:
        ...

DEEPSLEEP = 4 # type: int
DEEPSLEEP_RESET = 4 # type: int
EXT0_WAKE = 2 # type: int
EXT1_WAKE = 3 # type: int
HARD_RESET = 2 # type: int

class I2C:
    ''
    def readinto(self, *args) -> Any:
        ...

    def start(self, *args) -> Any:
        ...

    def stop(self, *args) -> Any:
        ...

    def write(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...

    def readfrom(self, *args) -> Any:
        ...

    def readfrom_into(self, *args) -> Any:
        ...

    def readfrom_mem(self, *args) -> Any:
        ...

    def readfrom_mem_into(self, *args) -> Any:
        ...

    def scan(self, *args) -> Any:
        ...

    def writeto(self, *args) -> Any:
        ...

    def writeto_mem(self, *args) -> Any:
        ...

    def writevto(self, *args) -> Any:
        ...


class I2S:
    ''
    def readinto(self, *args) -> Any:
        ...

    def write(self, *args) -> Any:
        ...

    MONO = 0 # type: int
    RX = 9 # type: int
    STEREO = 1 # type: int
    TX = 5 # type: int
    def deinit(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...

    def irq(self, *args) -> Any:
        ...

    def shift(self, *args) -> Any:
        ...

PIN_WAKE = 2 # type: int

class PWM:
    ''
    def deinit(self, *args) -> Any:
        ...

    def duty(self, *args) -> Any:
        ...

    def duty_ns(self, *args) -> Any:
        ...

    def duty_u16(self, *args) -> Any:
        ...

    def freq(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...

PWRON_RESET = 1 # type: int

class Pin:
    ''
    def value(self, *args) -> Any:
        ...

    DRIVE_0 = 0 # type: int
    DRIVE_1 = 1 # type: int
    DRIVE_2 = 2 # type: int
    DRIVE_3 = 3 # type: int
    IN = 1 # type: int
    IRQ_FALLING = 2 # type: int
    IRQ_RISING = 1 # type: int
    OPEN_DRAIN = 7 # type: int
    OUT = 3 # type: int
    PULL_DOWN = 1 # type: int
    PULL_UP = 2 # type: int
    WAKE_HIGH = 5 # type: int
    WAKE_LOW = 4 # type: int
    def init(self, *args) -> Any:
        ...

    def irq(self, *args) -> Any:
        ...

    def off(self, *args) -> Any:
        ...

    def on(self, *args) -> Any:
        ...


class RTC:
    ''
    def datetime(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...

    def memory(self, *args) -> Any:
        ...


class SDCard:
    ''
    def deinit(self, *args) -> Any:
        ...

    def info(self, *args) -> Any:
        ...

    def ioctl(self, *args) -> Any:
        ...

    def readblocks(self, *args) -> Any:
        ...

    def writeblocks(self, *args) -> Any:
        ...

SLEEP = 2 # type: int
SOFT_RESET = 5 # type: int

class SPI:
    ''
    def read(self, *args) -> Any:
        ...

    def readinto(self, *args) -> Any:
        ...

    def write(self, *args) -> Any:
        ...

    LSB = 1 # type: int
    MSB = 0 # type: int
    def deinit(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...

    def write_readinto(self, *args) -> Any:
        ...


class Signal:
    ''
    def value(self, *args) -> Any:
        ...

    def off(self, *args) -> Any:
        ...

    def on(self, *args) -> Any:
        ...


class SoftI2C:
    ''
    def readinto(self, *args) -> Any:
        ...

    def start(self, *args) -> Any:
        ...

    def stop(self, *args) -> Any:
        ...

    def write(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...

    def readfrom(self, *args) -> Any:
        ...

    def readfrom_into(self, *args) -> Any:
        ...

    def readfrom_mem(self, *args) -> Any:
        ...

    def readfrom_mem_into(self, *args) -> Any:
        ...

    def scan(self, *args) -> Any:
        ...

    def writeto(self, *args) -> Any:
        ...

    def writeto_mem(self, *args) -> Any:
        ...

    def writevto(self, *args) -> Any:
        ...


class SoftSPI:
    ''
    def read(self, *args) -> Any:
        ...

    def readinto(self, *args) -> Any:
        ...

    def write(self, *args) -> Any:
        ...

    LSB = 1 # type: int
    MSB = 0 # type: int
    def deinit(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...

    def write_readinto(self, *args) -> Any:
        ...

TIMER_WAKE = 4 # type: int
TOUCHPAD_WAKE = 5 # type: int

class Timer:
    ''
    def value(self, *args) -> Any:
        ...

    ONE_SHOT = 0 # type: int
    PERIODIC = 1 # type: int
    def deinit(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...


class TouchPad:
    ''
    def read(self, *args) -> Any:
        ...

    def config(self, *args) -> Any:
        ...


class UART:
    ''
    def any(self, *args) -> Any:
        ...

    def read(self, *args) -> Any:
        ...

    def readinto(self, *args) -> Any:
        ...

    def readline(self, *args) -> Any:
        ...

    def write(self, *args) -> Any:
        ...

    CTS = 2 # type: int
    INV_CTS = 8 # type: int
    INV_RTS = 64 # type: int
    INV_RX = 4 # type: int
    INV_TX = 32 # type: int
    RTS = 1 # type: int
    def deinit(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...

    def sendbreak(self, *args) -> Any:
        ...

ULP_WAKE = 6 # type: int

class WDT:
    ''
    def feed(self, *args) -> Any:
        ...

WDT_RESET = 3 # type: int
def bitstream(*args) -> Any:
    ...

def deepsleep(*args) -> Any:
    ...

def disable_irq(*args) -> Any:
    ...

def enable_irq(*args) -> Any:
    ...

def freq(*args) -> Any:
    ...

def idle(*args) -> Any:
    ...

def lightsleep(*args) -> Any:
    ...

mem16 : Any ## <class 'mem'> = <16-bit memory>
mem32 : Any ## <class 'mem'> = <32-bit memory>
mem8 : Any ## <class 'mem'> = <8-bit memory>
def reset(*args) -> Any:
    ...

def reset_cause(*args) -> Any:
    ...

def sleep(*args) -> Any:
    ...

def soft_reset(*args) -> Any:
    ...

def time_pulse_us(*args) -> Any:
    ...

def unique_id(*args) -> Any:
    ...

def wake_reason(*args) -> Any:
    ...

