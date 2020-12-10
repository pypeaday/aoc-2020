import numpy as np
from typing import Union
import copy
import itertools
from more_itertools import windowed


def get_data(filepath: str = './data/raw/day10_sample.txt'):
    data = []
    with open(filepath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data.append(int(line))
    return sorted(data)


def device_max_jolts(data: list) -> int:
    """Calculate my device's max joltage based on the input data

    Args:
        data (list): input data

    Returns:
        int: max joltage of my device  
    """
    return max(data) + 3


def determine_any_invalid_adapters(data: list, max_diff: int = 3) -> bool:
    """Find if there are any invalid adapters in the list of data

    Args:
        data (list): input data
        max_diff (int): maximum joltage difference between adapters

    Returns:
        bool: True/False
    """
    diffs = np.diff(data)
    return any(diffs > max_diff)


def determine_all_joltage_differences(data: list) -> list:
    """returns the joltage differences between all adapters used in the valid sequence

    Args:
        data (list): input data with the device's built-in joltage adapter appended

    Returns:
        list: list of joltage differences
    """
    return list(np.diff(data))


def format_data(data: list, device_adapter_joltage: int):
    """Append to the input data the device's built in adapter's joltage

    Args:
        data (list): [description]
        device_adapter_joltage (int): [description]
    """
    new_data = [0]
    new_data.extend([x for x in data])
    new_data.append(device_adapter_joltage)
    return new_data


def calculate_solution_1(diffs: list) -> int:
    """Return the product of the number of 1 joltage differences between adapter with the number of 3 joltage differences between adapters

    Args:
        diffs (list): list of joltage differences between adapters

    Returns:
        int: [description]
    """
    return diffs.count(1) * diffs.count(3)


def main(filepath: str = './data/raw/day10_sample.txt'):

    data = get_data(filepath)
    device_adapter_joltage = device_max_jolts(data)
    new_data = format_data(data, device_adapter_joltage)
    if determine_any_invalid_adapters(new_data):
        raise SystemError('Invalid adapter sequence')
    diffs = determine_all_joltage_differences(new_data)
    solution_1 = calculate_solution_1(diffs)
    print(f'solution 1: {solution_1}')

if __name__ == '__main__':
    main('./data/raw/day10_input.txt')