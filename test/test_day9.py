import pytest
import os
from src.day9.main import get_data, is_valid, main, main2


def test_get_data():
    data = get_data("./data/raw/day9_sample.txt")
    assert data[0] == 35
    assert data[1] == 20
    assert data[2] == 15
    assert data[3] == 25
    assert data[4] == 47
    assert data[5] == 40
    assert data[6] == 62
    assert data[7] == 55
    assert data[8] == 65
    assert data[9] == 95
    assert data[10] == 102
    assert data[11] == 117
    assert data[12] == 150
    assert data[13] == 182
    assert data[14] == 127
    assert data[15] == 219
    assert data[16] == 299
    assert data[17] == 277
    assert data[18] == 309
    assert data[19] == 576


def test_is_valid():
    data = get_data("./data/raw/day9_sample.txt")
    assert is_valid(data[5], data[0:5]) is True
    assert is_valid(data[6], data[1:6]) is True
    assert is_valid(data[7], data[2:7]) is True
    assert is_valid(data[8], data[3:8]) is True
    assert is_valid(data[9], data[4:9]) is True
    assert is_valid(data[10], data[5:10]) is True
    assert is_valid(data[11], data[6:11]) is True
    assert is_valid(data[12], data[7:12]) is True
    assert is_valid(data[13], data[8:13]) is False
    assert is_valid(data[14], data[9:14]) is True
    assert is_valid(data[15], data[10:15]) is True
    assert is_valid(data[16], data[11:16]) is True
    assert is_valid(data[17], data[12:17]) is True
    assert is_valid(data[18], data[13:18]) is True
    assert is_valid(data[19], data[14:19]) is True


def test_main():
    res, idx = main("./data/raw/day9_sample.txt", 5)
    assert res == 127


def test_main2():
    _, idx = main("./data/raw/day9_sample.txt", 5)
    res2 = main2("./data/raw/day9_sample.txt", 5, idx)
    assert min(res2) == 15
    assert max(res2) == 47