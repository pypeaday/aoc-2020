from typing import Union
import copy
import itertools
from more_itertools import windowed


def get_data(filepath: str = './data/raw/day9_sample.txt'):
    data = []
    with open(filepath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data.append(int(line))
    return data


def is_valid(num_to_check: int, values: list) -> bool:
    """function to check is num_to_check is the sum of any 2 numbers, without replacement, in values

    Args:
        num_to_check (int): input number to check
        values (list): list of integer values to pair off and check for sum()

    Returns:
        bool: True/False
    """
    pairs = itertools.combinations(values, 2)
    res = map(sum, pairs)
    return num_to_check in res



def main(filepath: str = './data/raw/day9_sample.txt', preamble_length: int = 5):
    data = get_data(filepath)
    nums = data[preamble_length:]
    res = map(is_valid, nums, windowed(data, preamble_length))
    res = list(res)
    idx = res.index(False)
    return nums[idx]


if __name__ == '__main__':
    res = main('./data/raw/day9_input.txt', 25)
    print(f'Solution to part 1 is: {res}')
