import pytest
import os
from src.day5.main import (get_data, get_seat_id, get_number_indices, split_data, split_list,
                           return_binary_split_result, decode_id)


os.chdir('..')  # we're in test/and need to be up one level


def test_get_data():
    inputs = get_data('./data/raw/day5_sample.txt')

    assert inputs[0] == 'BBFFBBFRLL'
    assert inputs[1] == 'BFFFBBFRRR'
    assert inputs[2] == 'FBFBBFFRLR'
    assert inputs[3] == 'FFFBBBFRRR'


def test_get_seat_id():

    assert get_seat_id(70, 7) == 567
    assert get_seat_id(14, 7) == 119
    assert get_seat_id(102, 4) == 820
    assert get_seat_id(44, 5) == 357


def test_get_number_indices():
    assert get_number_indices(7) == 128
    assert get_number_indices(3) == 8


def test_split_data():
    inputs = get_data('./data/raw/day5_sample.txt')
    data = split_data(inputs, 7, 3)
    assert data[0] == ('BBFFBBF', 'RLL')
    assert data[1] == ('BFFFBBF', 'RRR')
    assert data[2] == ('FBFBBFF', 'RLR')
    assert data[3] == ('FFFBBBF', 'RRR')


def test_split_list():
    res = split_list(['a', 'b', 'c', 'd'])
    assert res[0] == ['a', 'b']
    assert res[1] == ['c', 'd']
    assert split_list([1, 2]) == ([1], [2])
    with pytest.raises(AssertionError):
        split_list([1, 2, 3])


def test_return_binary_split_result():
    assert return_binary_split_result([0, 1, 2, 3], 'B') == [2, 3]


def test_decode_id():
    inputs = get_data('./data/raw/day5_sample.txt')
    data = split_data(inputs,  7, 3)
    assert decode_id(data[0][0]) == 102
    assert decode_id(data[0][1]) == 4

    assert decode_id(data[1][0]) == 70
    assert decode_id(data[1][1]) == 7

    assert decode_id(data[2][0]) == 44
    assert decode_id(data[2][1]) == 5

    assert decode_id(data[3][0]) == 14
    assert decode_id(data[3][1]) == 7

