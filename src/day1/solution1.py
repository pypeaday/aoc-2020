from itertools import combinations


def get_data(file: str = './data/raw/day1_input.txt') -> list:
    inputs = []
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            inputs.append(int(line))
    return inputs


def find_sum(ls: list, k: int) -> list:
    return [tup for tup in combinations(ls, 2) if sum(tup) == k]


def main():
    _input_list = get_data()
    res = find_sum(_input_list, 2020)
    print(f'solution is {res}')
    print(f'product is {res[0][0]*res[0][1]}')


if __name__ == '__main__':
    main()
