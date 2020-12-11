from typing import Union
import copy
import itertools
from more_itertools import windowed


def get_data(filepath: str = "./data/raw/day9_sample.txt"):
    data = []
    with open(filepath, "r") as f:
        lines = f.readlines()
        for line in lines:
            data.append(int(line))
    return data


def is_valid(num_to_check: int, values: list, seq_len: int = 2) -> bool:
    """function to check is num_to_check is the sum of any 2 numbers, without replacement, in values

    Args:
        num_to_check (int): input number to check
        values (list): list of integer values to pair off and check for sum()
        seq_len (int): length of combination sequences (default to 2 for pairs)
    Returns:
        bool: True/False
    """
    groups = itertools.combinations(values, seq_len)
    res = map(sum, groups)
    return num_to_check in res


def main(
    filepath: str = "./data/raw/day9_sample.txt", preamble_length: int = 5
):
    data = get_data(filepath)
    nums = data[preamble_length:]
    res = map(is_valid, nums, windowed(data, preamble_length))
    res = list(res)
    idx = res.index(False)
    return nums[idx], idx


def check_sum(seq: list, value: int) -> bool:
    """Check is the numbers in seq sum to value

    Args:
        seq (list): input sequence of integers
        value (int): desired sum output

    Returns:
        bool: True/False
    """
    return sum(seq) == value


def main2(
    filepath: str = "./data/raw/day9_sample.txt",
    preamble_length: int = 5,
    idx: int = 0,
):
    """Solution 2 for day 9

    Args:
        filepath (str, optional):  Defaults to './data/raw/day9_sample.txt'.
        preamble_length (int, optional):  Defaults to 5.
        idx (int, optional): The id of the invalid number from main(). Defaults to 0.
    """

    data = get_data(filepath)
    invalid_number = data[preamble_length:][idx]
    values = data[: idx + preamble_length]
    # find any set of contiguous values in values that sum to invalid_number
    for seq_len in range(2, len(values) + 1):
        res = map(
            check_sum,
            windowed(values, seq_len),
            [invalid_number for _ in range(len(values) + 1 - seq_len)],
        )
        res = list(res)
        if any(res):
            idx = res.index(True)
            vec = values[idx : seq_len + idx]
            return vec
    return []


if __name__ == "__main__":
    res, idx = main("./data/raw/day9_input.txt", 25)
    print(f"Solution to part 1 is: {res}")

    res2 = main2("./data/raw/day9_input.txt", 25, idx)
    encryption_weakness = min(res2) + max(res2)
    print(f"Encryption weakness for part 2 is: {encryption_weakness}")
