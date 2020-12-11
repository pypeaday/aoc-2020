import pytest
from src.day10.main import (
    calculate_solution_1,
    get_data,
    get_device_max_jolts,
    determine_good_sequence,
    format_data,
    determine_all_joltage_differences,
    calculate_solution_2,
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
    device_adapter_joltage = get_device_max_jolts(data)
    new_data = format_data(data, device_adapter_joltage)
    assert new_data[-1] == device_adapter_joltage
    assert new_data[0] == 0


def test_device_max_jolts():
    data = get_data()
    assert get_device_max_jolts(data) == 22


def test_determine_good_sequence():
    data = get_data("./data/raw/day10_sample.txt")
    assert determine_good_sequence(data) is True

    data = get_data("./data/raw/day10_sample2.txt")
    assert determine_good_sequence(data, last_val=max(data)) is True


def test_calculate_solution_1():
    data = get_data("./data/raw/day10_sample.txt")
    device_adapter_joltage = get_device_max_jolts(data)
    new_data = format_data(data, device_adapter_joltage)
    diffs = determine_all_joltage_differences(new_data)
    assert calculate_solution_1(diffs) == 35


def test_calculate_solution_2():
    data = get_data("./data/raw/day10_sample.txt")
    sol2 = calculate_solution_2(data)
    assert sol2 == 8
    data = get_data("./data/raw/day10_sample2.txt")
    sol2 = calculate_solution_2(data)
    assert sol2 == 19208
