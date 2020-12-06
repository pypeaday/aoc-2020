import pytest
import os
from src.day6.main import (get_data, format_data_part_1, format_data_part_2, get_group_count, get_intersection,
                           main, main2)


os.chdir('..')  # we're in test/and need to be up one level


def test_get_data():
    raw_data = get_data('./data/raw/day6_sample.txt')

    assert raw_data[0] == 'abc'
    assert raw_data[1] == ''
    assert raw_data[2] == 'a'
    assert raw_data[3] == 'b'
    assert raw_data[4] == 'c'
    assert raw_data[5] == ''
    assert raw_data[6] == 'ab'
    assert raw_data[7] == 'ac'
    assert raw_data[8] == ''
    assert raw_data[9] == 'a'
    assert raw_data[10] == 'a'
    assert raw_data[11] == 'a'
    assert raw_data[12] == 'a'
    assert raw_data[13] == ''
    assert raw_data[14] == 'b'


def test_format_data_part_1():
    raw_data = get_data('./data/raw/day6_sample.txt')
    data = format_data_part_1(raw_data)
    assert data[0] == 'abc'
    assert data[1] == 'abc'
    assert data[2] == 'abac'
    assert data[3] == 'aaaa'
    assert data[4] == 'b'


def test_format_data_part_2():
    raw_data = get_data('./data/raw/day6_sample.txt')
    data = format_data_part_2(raw_data)

    assert data[0][0] == 'abc'

    assert data[1][0] == 'a'
    assert data[1][1] == 'b'
    assert data[1][2] == 'c'

    assert data[2][0] == 'ab'
    assert data[2][1] == 'ac'

    assert data[3][0] == 'a'
    assert data[3][1] == 'a'
    assert data[3][2] == 'a'
    assert data[3][3] == 'a'

    assert data[4][0] == 'b'


def test_get_group_count():
    raw_data = get_data('./data/raw/day6_sample.txt')
    data = format_data_part_1(raw_data)
    assert get_group_count(data[0]) == 3
    assert get_group_count(data[1]) == 3
    assert get_group_count(data[2]) == 3
    assert get_group_count(data[3]) == 1
    assert get_group_count(data[4]) == 1


def test_part_1():
    assert main('./data/raw/day6_sample.txt') == 11


def test_get_intersection():
    raw_data = get_data('./data/raw/day6_sample.txt')
    data = format_data_part_2(raw_data)
    assert get_intersection(data[0]) == 'abc'
    assert get_intersection(data[1]) == ''
    assert get_intersection(data[2]) == 'a'
    assert get_intersection(data[3]) == 'a'
    assert get_intersection(data[4]) == 'b'


def test_part_2():
    assert main2('./data/raw/day6_sample.txt') == 6
