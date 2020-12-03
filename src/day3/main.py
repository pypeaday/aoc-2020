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

    return _input == '#'


def check_row_part_1(row: str, row_id: int, delta_x: int = 3, delta_y: int = 1) -> bool:
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
    raw_col_id = row_id * delta_x
    col_id = get_col_index(raw_col_id, len(row))
    return is_tree(row[col_id])


def main(filepath: str = './data/raw/day3_sample.txt'):
    inputs = get_data(filepath)
    ids = range(len(inputs))
    res = map(check_row_part_1, inputs, ids)
    print(f'Number of trees encountered for part 1 is: {sum(res)}')


if __name__ == '__main__':
    # solution 1
    # filepath = './data/raw/day3_sample.txt'
    filepath = './data/raw/day3_input.txt'

    # part 1
    main(filepath)
