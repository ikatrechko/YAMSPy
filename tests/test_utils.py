import pytest
import struct

from yamspy.utils import (
    readbytes,
    bit_check,
    convert,
    _crc8_dvb_s2,
)


def test_readbytes_8_signed():
    data = bytearray([0xFE])  # -2
    assert readbytes(data, size=8) == -2
    assert data == bytearray()


def test_readbytes_8_unsigned():
    data = bytearray([0xFE])  # 254
    assert readbytes(data, size=8, unsigned=True) == 254
    assert data == bytearray()


def test_readbytes_16_signed():
    data = bytearray([0x34, 0x12])  # 0x1234 → 4660
    assert readbytes(data, size=16) == 0x1234
    assert data == bytearray()


def test_readbytes_16_unsigned():
    data = bytearray([0xFF, 0x7F])  # 0x7FFF → 32767
    assert readbytes(data, size=16, unsigned=True) == 32767


def test_readbytes_32_signed():
    val = -12345678
    packed = struct.pack("<i", val)
    data = bytearray(packed)
    assert readbytes(data, size=32) == val


def test_readbytes_32_float():
    val = 123.456
    packed = struct.pack("<f", val)
    data = bytearray(packed)
    out = readbytes(data, size=32, read_as_float=True)
    assert abs(out - val) < 1e-5


def test_readbytes_16_float():
    val = 12.5
    packed = struct.pack("<e", val)
    data = bytearray(packed)
    out = readbytes(data, size=16, read_as_float=True)
    assert abs(out - val) < 1e-3


def test_bit_check_true():
    assert bit_check(0b0100, 2) is True


def test_bit_check_false():
    assert bit_check(0b0100, 1) is False


def test_convert_default_16bit():
    result = convert([0x1234])
    assert result == [0x34, 0x12]


def test_convert_multiple_values():
    result = convert([0x1234, 0xABCD])
    assert result == [0x34, 0x12, 0xCD, 0xAB]


def test_convert_32bit():
    result = convert([0x11223344], n=32)
    assert result == [0x44, 0x33, 0x22, 0x11]


def test_crc8_dvb_s2_known_vector():
    crc = 0
    for b in [0x01, 0x02, 0x03, 0x04]:
        crc = _crc8_dvb_s2(crc, b)
    assert crc == 0x75

def test_crc8_dvb_s2_single_byte():
    assert _crc8_dvb_s2(0, 0xA5) == 0x60
