import pytest
import os
from src.day2.main import main, main2, get_data, extract_vars, extract_vars_pt2, check_validity, check_validity2


def test_get_data():
    inputs = get_data('./data/raw/day2_sample.txt')
    assert inputs[0] == '1-3 a: abcde'
    assert inputs[-1] == '2-9 c: ccccccccc'


def test_extract_vars():
    _input = '1-3 a: abcde'
    res = extract_vars(_input)
    assert res[0] == 1
    assert res[1] == 3
    assert res[2] == 'a'
    assert res[3] == 'abcde'


def test_extract_vars2():
    _input = '1-3 a: abcde'
    res = extract_vars_pt2(_input)
    assert res[0] == 0
    assert res[1] == 2
    assert res[2] == 'a'
    assert res[3] == 'abcde'


def test_check_validity():
    _input = '1-3 a: abcde'
    res = check_validity(_input)
    assert res is True

    _input = '1-3 b: cdefg'
    res = check_validity(_input)
    assert res is False

    _input = '2-9 c: ccccccccc'
    res = check_validity(_input)
    assert res is True


def test_check_validity2():
    _input = '1-3 a: abcde'
    res = check_validity2(_input)
    assert res is True

    _input = '1-3 b: cdefg'
    res = check_validity2(_input)
    assert res is False

    _input = '2-9 c: ccccccccc'
    res = check_validity2(_input)
    assert res is False


def test_main():
    ans1 = main('./data/raw/day2_sample.txt', False, True)
    assert ans1 == 2
    ans2 = main2('./data/raw/day2_sample.txt')
    assert ans2 == 1

