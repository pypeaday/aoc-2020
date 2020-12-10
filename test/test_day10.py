import pytest
import os
from src.day10.main import (
    calculate_solution_1,
    get_data,
    device_max_jolts,
    determine_any_invalid_adapters,
    format_data,
    determine_all_joltage_differences,
)


def test_get_data():
    data = get_data("./data/raw/day10_sample.txt")
    assert data[0] == 1
    assert data[1] == 4
    assert data[2] == 5
    assert data[3] == 6
    assert data[4] == 7
    assert data[5] == 10
    assert data[6] == 11
    assert data[7] == 12
    assert data[8] == 15
    assert data[9] == 16
    assert data[10] == 19


def test_append_device_joltage_adapter():
    data = get_data("./data/raw/day10_sample.txt")
    device_adapter_joltage = device_max_jolts(data)
    new_data = format_data(data, device_adapter_joltage)
    assert new_data[-1] == device_adapter_joltage
    assert new_data[0] == 0


def test_device_max_jolts():
    data = get_data()
    assert device_max_jolts(data) == 22


def test_determine_any_invalid_adapters():
    data = get_data("./data/raw/day10_sample.txt")
    assert determine_any_invalid_adapters(data) is False


def test_calculate_solution_1():
    data = get_data("./data/raw/day10_sample.txt")
    device_adapter_joltage = device_max_jolts(data)
    new_data = format_data(data, device_adapter_joltage)
    diffs = determine_all_joltage_differences(new_data)
    assert calculate_solution_1(diffs) == 22
