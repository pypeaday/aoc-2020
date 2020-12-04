from itertools import combinations
import numpy as np


def get_data(file: str = './data/raw/day1_input.txt') -> list:
    inputs = []
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            inputs.append(int(line))
    return inputs


def find_sum(ls: list, p: int, k: int) -> list:
    return [tup for tup in combinations(ls, p) if sum(tup) == k]


def main(filepath: str = './data/raw/day1_input.txt',
         p: int = 2,
         k: int = 2020):
    _input_list = get_data(filepath)
    results = find_sum(_input_list, p, k)
    res = results[0]
    print(f'solution is {res}')
    prod = np.prod(res)
    print(f'product is {prod}')
    return prod


if __name__ == '__main__':
    # solution 1
    main('./data/raw/day1_input.txt', 2, 2020)
    # solution 2
    main('./data/raw/day1_input.txt', 3, 2020)
