import itertools
import numpy as np
from typing import Tuple


def get_data(filepath: str = "./data/raw/day5_sample.txt") -> list:
    """
    Returns sorted list of inputs
    :param filepath:
    :return:
    """
    with open(filepath, "r") as f:
        lines = f.readlines()
    return sorted([x.replace("\n", "") for x in lines])


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
    bin_map = {"B": 1, "F": 0, "L": 0, "R": 1}
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
    for _split in _input:
        seats = return_binary_split_result(seats, _split)

    return seats[0]


def main(filepath: str = "./data/raw/day5_sample.txt") -> Tuple[list, tuple]:
    inputs = get_data(filepath)
    data = split_data(inputs, 7, 3)
    # get all row ids
    row_ids = map(decode_id, [x[0] for x in data])
    # get all col ids
    col_ids = map(decode_id, [x[1] for x in data])

    seat_ids_gen = map(get_seat_id, row_ids, col_ids)
    seat_ids = [x for x in seat_ids_gen]

    return seat_ids, data[0]


def get_all_seat_coords(num_rows: int, num_cols: int) -> list:
    # get cartesian product to represent all seats
    all_seat_coords = itertools.product(
        *[[x for x in range(num_rows)], [x for x in range(num_cols)]]
    )
    return list(all_seat_coords)


def get_all_seat_ids(row_len: int = 7, col_len: int = 3) -> list:
    """

    :param row_len: number of characters used to decode row id
        ex.  FBFBBFF is 7 characters
    :param col_len: number of character usedto decode col id
        ex. RLR is 3 characters
    :return: list of possible seat ids based on get_seat_id
    """

    # calculate all possible seat ids
    num_rows = get_number_indices(row_len)
    num_cols = get_number_indices(col_len)
    all_seat_coords = get_all_seat_coords(num_rows, num_cols)
    all_ids = map(
        get_seat_id,
        [x[0] for x in all_seat_coords],
        [x[1] for x in all_seat_coords],
    )
    return list(all_ids)


def post_main(seat_ids: list, one_input: str) -> int:
    """
    Takes the list of seat ids from main() from part 1
    and finds our missing seat id
    :param seat_ids: result of main
    :param one_input: one example input to main() to get the
        number of characters per row and col id decoding
    :return: my seat id
    """
    row_len = len(one_input[0])
    col_len = len(one_input[1])
    all_seat_ids = get_all_seat_ids(row_len, col_len)
    # find all missing seat ids
    missing_ids = list(set(all_seat_ids) - set(seat_ids))

    diff_ids = np.diff(missing_ids)
    # numpy np.argwhere returns a list of lists basically
    # so we have to index twice
    _id = 1 + np.argwhere(diff_ids != 1)[0][0]
    return missing_ids[_id]


if __name__ == "__main__":
    # part 1
    seat_ids, example_input = main("./data/raw/day5_input.txt")
    print(f"Max seat ID for part 1 is: {max(seat_ids)}")

    # part 2:
    my_seat_id = post_main(seat_ids, example_input)
    print(f"My seat ID is {my_seat_id}")
