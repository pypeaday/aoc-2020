import numpy as np


def get_data(filepath: str = './data/raw/day3_input.txt'):
    with open(filepath, 'r') as f:
        inputs = f.readlines()
    # strip away the \n character
    return [x.replace('\n', '') for x in inputs]


def get_col_index(raw_col_id: int, num_cols: int = 11) -> int:
    """
    Return the column index of the map based on the modulo operator

    The pattern we traverse repeats itself to the right many times.
    Say we have 11 columns in our original map and as we move right
    via the given algorithm we will eventually come to column 12.
    This would be equivalent to the first column of the map so the
    desired index is 0

    :param raw_col_id: given column index
    :param num_cols: number of columns in the original map 1-indexed
    :return: column index in [0, num_columns-1]
    """
    return raw_col_id % num_cols


def is_tree(_input: str) -> bool:
    """
    check if the current coordinate is a tree or not
    :param _input: one of '.' or '#'
    :return: False/True
    """
    if _input not in ['#', '.']:
        raise ValueError('Unexpected argument passed.')
    return _input == '#'


def check_row(row: str, row_id: int, delta_x: int = 3, delta_y: int = 1) -> bool:
    """
    For part 1 this takes one  row of the map and returns
    whether or not the coordinate in that row is a tree
    :param row: row of the map
        ex. '#...#...#..'
    :param row_id: 0 based index of which row in the map
         we are checking for a tree - used to determine
         the column id based on the algorithm.
         Will be normalized inside the function.
    :param delta_x: how many coordinates to move right per iteration
        for a given algorithm
    :param delta_y: how many rows to move down at any iteration in a
        given algorithm
    :return: is_tree()
    """
    # check that this is actually a row to check
    if row_id % delta_y != 0:
        return False
    raw_col_id = row_id // delta_y * delta_x
    col_id = get_col_index(raw_col_id, len(row))
    return is_tree(row[col_id])


def main(filepath: str = './data/raw/day3_sample.txt',
         delta_x: int = 3,
         delta_y: int = 1):
    inputs = get_data(filepath)
    ids = range(len(inputs))
    delta_xs = [delta_x for _ in range(len(inputs))]
    delta_ys = [delta_y for _ in range(len(inputs))]
    res = map(check_row, inputs, ids, delta_xs, delta_ys)
    answer = sum(res)
    print(f'Number of trees encountered when moving '
          f'right {delta_x} and down {delta_y} is: {answer}')
    return answer


if __name__ == '__main__':
    # filepath = './data/raw/day3_sample.txt'
    filepath = './data/raw/day3_input.txt'

    # part 1
    print('Solution for part 1')
    main(filepath)
    print('*'*24)

    # part 2
    print('Starting solution for part 2')
    algorithm_config = get_data('./src/day3/algorithm_config.txt')
    solution2_results = []
    for algo in algorithm_config:
        delta_x = int(algo.split(',')[0])
        delta_y = int(algo.split(',')[1])
        solution2_results.append(main(filepath, delta_x, delta_y))

    # due to potential issues with numpy I opt for a simple approach
    # sol2 = np.prod(solution2_results)
    sol2 = 1
    for n in solution2_results:
        sol2 = sol2 * n

    print(f'Solution for part 2 is {sol2}')
