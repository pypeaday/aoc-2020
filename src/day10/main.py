from collections import defaultdict

import numpy as np


def get_data(filepath: str = "./data/raw/day10_sample.txt"):
    data = []
    with open(filepath, "r") as f:
        lines = f.readlines()
        for line in lines:
            data.append(int(line))
    return sorted(data)


def get_device_max_jolts(data: list) -> int:
    """Calculate my device's max joltage based on the input data

    Args:
        data (list): input data

    Returns:
        int: max joltage of my device
    """
    return max(data) + 3


def determine_good_sequence(
    data: list, max_diff: int = 3, last_val: int = 19
) -> bool:
    """Find if there are any invalid adapters in the list of data

    Args:
        data (list): input data
        max_diff (int): maximum joltage difference between adapters
        last_val (int): required last value of the sequence (necessary for
                        part 2)

    Returns:
        bool: True/False
    """
    diffs = np.diff(data)
    return not any(diffs > max_diff) and data[-1] == last_val


def determine_all_joltage_differences(data: list) -> list:
    """returns the joltage differences between all adapters used in the valid
    sequence

    Args:
        data (list): input data with the device's built-in joltage adapter
        appended

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
    """Return the product of the number of 1 joltage differences between
        adapter with the number of 3 joltage differences between adapters

    Args:
        diffs (list): list of joltage differences between adapters

    Returns:
        int: [description]
    """
    return diffs.count(1) * diffs.count(3)


def calculate_solution_2(data: list):
    data_plus = format_data(data, get_device_max_jolts(data))
    solution_map = defaultdict(int)
    # The sum of all the ways to get to any given adapter is the sum of all
    #  the ways to get to every adapter within 3 jolts of it so we can build
    # a solution map with a simple for loop
    solution_map[0] = 1
    for jolt in data_plus:
        if jolt - 1 in solution_map:
            solution_map[jolt] += solution_map[jolt - 1]
        if jolt - 2 in solution_map:
            solution_map[jolt] += solution_map[jolt - 2]
        if jolt - 3 in solution_map:
            solution_map[jolt] += solution_map[jolt - 3]
    return solution_map[data_plus[-1]]


def main(filepath: str = "./data/raw/day10_sample.txt"):

    data = get_data(filepath)
    if any(np.diff(data)) == 2:
        raise SystemError(
            "Only accounted for jolt differneces of 1 or 3! Need to rethink..."
        )
    device_adapter_joltage = get_device_max_jolts(data)
    data_plus = format_data(data, device_adapter_joltage)
    diffs = determine_all_joltage_differences(data_plus)
    solution_1 = calculate_solution_1(diffs)
    print(f"solution 1: {solution_1}")

    solution_2 = calculate_solution_2(data)
    print(f"solution 2: {solution_2}")


if __name__ == "__main__":
    main("./data/raw/day10_input.txt")
