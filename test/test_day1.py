import pytest
import os
from src.day1.main import get_data, find_sum, main


def test_get_data():
    inputs = get_data("./data/raw/day1_sample.txt")
    assert inputs[0] == 1721
    assert inputs[-1] == 1456


def test_find_sum():
    inputs = get_data("./data/raw/day1_sample.txt")
    ts1 = find_sum(inputs, 2, 2020)
    assert set(ts1[0]) == {1721, 299}

    ts2 = find_sum(inputs, 3, 2020)
    assert set(ts2[0]) == {979, 366, 675}


def test_main():
    prod1 = main("./data/raw/day1_sample.txt", 2, 2020)
    assert prod1 == 514579
    prod2 = main("./data/raw/day1_sample.txt", 3, 2020)
    assert prod2 == 241861950
