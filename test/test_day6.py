import pytest
import os
from src.day6.main import (get_data, get_group_count, sum_all_group_counts)


os.chdir('..')  # we're in test/and need to be up one level


def test_get_data():
    inputs, n_people_per_group = get_data('./data/raw/day6_sample.txt')

    assert inputs[0] == 'abc'
    assert inputs[1] == 'abc'
    assert inputs[2] == 'abac'
    assert inputs[3] == 'aaaa'
    assert inputs[4] == 'b'

    assert n_people_per_group[0] == 1
    assert n_people_per_group[1] == 3
    assert n_people_per_group[2] == 2
    assert n_people_per_group[3] == 4
    assert n_people_per_group[4] == 1


def test_get_group_count():
    inputs, n_people_per_group = get_data('./data/raw/day6_sample.txt')
    assert get_group_count(inputs[0]) == 3
    assert get_group_count(inputs[1]) == 3
    assert get_group_count(inputs[2]) == 3
    assert get_group_count(inputs[3]) == 1
    assert get_group_count(inputs[4]) == 1


def test_sum_all_group_counts():
    inputs, n_people_per_group = get_data('./data/raw/day6_sample.txt')
    all_group_counts = []
    for _data in inputs:
        all_group_counts.append(get_group_count(_data))

    assert sum_all_group_counts(all_group_counts) == 11
