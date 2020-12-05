def get_data(filepath: str = './data/raw/day5_sample.txt') -> list:
    """
    Returns sorted list of inputs
    :param filepath:
    :return:
    """
    with open(filepath, 'r') as f:
        lines = f.readlines()
    return sorted([x.replace('\n', '') for x in lines])


def get_number_indices(n: int = 7) -> int:
    """
    Parameterized function to return number of rows or columns in the
    plane. This isn't necessary for the solution but makes this code
    potentially more usable in the future

    :param n: number of characters used by BSP to determine a row/col
    :return: number of total row/cols in the place
    """
    return 2 ** n


def split_data(inputs: list, row_len: int = 7, col_len: int = 3) -> tuple:
    """
    Returns iterable of 2-item tuples which
    are the split inputs (row_identifier, col_identifier)
    :param inputs: output of get_data
    :param row_len: number of characters in the row_identifier
    :param col_len: number of characters in the col_identifier
    :return: ((row_identifier0, column_identifier0),
        (row_identifier1, col_identifier1), ...)
    """
    return tuple((x[:row_len], x[-col_len:]) for x in inputs)


def get_seat_id(row: int, col: int, p: int = 8) -> int:
    """
    Calculate the seat ID according to the AoC rule.
    :param row: row number on the boarding pass
    :param col: column number on the boarding pass
    :param p: multiplicative factor, given as 8
    :return: seat_id = row * p + col
    """
    return row * p + col


def split_list(ls: list) -> tuple:
    assert len(ls) % 2 == 0
    h = len(ls) // 2
    return ls[:h], ls[h:]


def return_binary_split_result(_range: list, _split: str) -> list:
    """

    :param _range: list of ids to split
    :param _split: one of ['B', 'F', 'R', 'L'] to determine which
        half of the _range to return
    :return: half of _range
    """
    # todo: move this map somewhere smarter
    # binary search will render list of 2 items, and
    # depending on looking for row or column the string
    # identifier for the lower or upper half is different.
    bin_map = {
        'B': 1,
        'F': 0,
        'L': 0,
        'R': 1
    }
    # put it in a map here to share the function
    return split_list(_range)[bin_map[_split]]


def decode_id(_input: str) -> int:
    """
    Naieve binary search to decode
    :param _input: row or column identifier to decode
        ex. BBFFBBF  or RLL
    :return: row/col id of the seat
    """
    num_ids = get_number_indices(len(_input))
    seats = [i for i in range(num_ids)]
    for i in range(len(_input)):
        seats = return_binary_split_result(seats, _input[i])

    return seats[0]


def main(filepath: str = './data/raw/day5_sample.txt') -> int:
    inputs = get_data(filepath)
    data = split_data(inputs, 7, 3)
    # get all row ids
    row_ids = map(decode_id, [x[0] for x in data])
    # get all col ids
    col_ids = map(decode_id, [x[1] for x in data])

    seat_ids_gen = map(get_seat_id, row_ids, col_ids)
    seat_ids = [x for x in seat_ids_gen]

    return max(seat_ids)


if __name__ == '__main__':
    # part 1
    seat_id = main('./data/raw/day5_input.txt')
    print(f'Max seat ID for part 1 is: {seat_id}')
