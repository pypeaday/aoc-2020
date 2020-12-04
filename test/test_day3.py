import pytest
import os
from src.day3.main import main, get_data, get_col_index, is_tree, check_row


os.chdir('..')  # we're in test/and need to be up one level


def test_get_data():
    inputs = get_data('./data/raw/day3_sample.txt')

    assert inputs[0] == '..##.......'
    assert inputs[1] == '#...#...#..'
    assert inputs[2] == '.#....#..#.'
    assert inputs[3] == '..#.#...#.#'
    assert inputs[4] == '.#...##..#.'
    assert inputs[5] == '..#.##.....'
    assert inputs[6] == '.#.#.#....#'
    assert inputs[7] == '.#........#'
    assert inputs[8] == '#.##...#...'
    assert inputs[9] == '#...##....#'
    assert inputs[10] == '.#..#...#.#'


def test_get_col_index():
    ans = get_col_index(0, 11)
    assert ans == 0
    ans = get_col_index(13, 11)
    assert ans == 2


def test_is_tree():
    ans = is_tree('.')
    assert ans is False
    ans = is_tree('#')
    assert ans is True
    with pytest.raises(ValueError):
        assert is_tree('x')


def test_check_row():
    inputs = get_data('./data/raw/day3_sample.txt')
    assert check_row(inputs[0], 0, 3, 1) is False
    assert check_row(inputs[1], 1, 3, 1) is False
    assert check_row(inputs[2], 2, 3, 1) is True
    assert check_row(inputs[3], 3, 3, 1) is False
    assert check_row(inputs[4], 4, 3, 1) is True
    assert check_row(inputs[5], 5, 3, 1) is True
    assert check_row(inputs[6], 6, 3, 1) is False
    assert check_row(inputs[7], 7, 3, 1) is True
    assert check_row(inputs[8], 8, 3, 1) is True
    assert check_row(inputs[9], 9, 3, 1) is True
    assert check_row(inputs[10], 10, 3, 1) is True

    assert check_row(inputs[0], 0, 1, 1) is False
    assert check_row(inputs[1], 1, 1, 1) is False
    assert check_row(inputs[2], 2, 1, 1) is False
    assert check_row(inputs[3], 3, 1, 1) is False
    assert check_row(inputs[4], 4, 1, 1) is False
    assert check_row(inputs[5], 5, 1, 1) is True
    assert check_row(inputs[6], 6, 1, 1) is False
    assert check_row(inputs[7], 7, 1, 1) is False
    assert check_row(inputs[8], 8, 1, 1) is False
    assert check_row(inputs[9], 9, 1, 1) is False
    assert check_row(inputs[10], 10, 1, 1) is True

    assert check_row(inputs[0], 0, 5, 1) is False
    assert check_row(inputs[1], 1, 5, 1) is False
    assert check_row(inputs[2], 2, 5, 1) is False
    assert check_row(inputs[3], 3, 5, 1) is True
    assert check_row(inputs[4], 4, 5, 1) is True
    assert check_row(inputs[5], 5, 5, 1) is False
    assert check_row(inputs[6], 6, 5, 1) is False
    assert check_row(inputs[7], 7, 5, 1) is False
    assert check_row(inputs[8], 8, 5, 1) is True
    assert check_row(inputs[9], 9, 5, 1) is False
    assert check_row(inputs[10], 10, 5, 1) is False

    assert check_row(inputs[0], 0, 7, 1) is False
    assert check_row(inputs[1], 1, 7, 1) is False
    assert check_row(inputs[2], 2, 7, 1) is False
    assert check_row(inputs[3], 3, 7, 1) is True
    assert check_row(inputs[4], 4, 7, 1) is True
    assert check_row(inputs[5], 5, 7, 1) is True
    assert check_row(inputs[6], 6, 7, 1) is False
    assert check_row(inputs[7], 7, 7, 1) is False
    assert check_row(inputs[8], 8, 7, 1) is False
    assert check_row(inputs[9], 9, 7, 1) is False
    assert check_row(inputs[10], 10, 7, 1) is True

    assert check_row(inputs[0], 0, 1, 2) is False
    assert check_row(inputs[2], 2, 1, 2) is True
    assert check_row(inputs[4], 4, 1, 2) is False
    assert check_row(inputs[6], 6, 1, 2) is True
    assert check_row(inputs[8], 7, 1, 2) is False
    assert check_row(inputs[10], 10, 1, 2) is False


