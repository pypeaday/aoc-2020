import pytest
import os
from src.day7.main import (get_data, can_bag_be_carried, main, count_bag_capacity, count_all_bag_capacities_including_self)


def test_get_data():
    data = get_data('./data/raw/day7_sample.txt')

    assert data['light red'] == ['bright white', 'muted yellow', 'muted yellow']
    assert data['dark orange'] == ['bright white', 'bright white', 'bright white', 'muted yellow', 'muted yellow',
                                   'muted yellow', 'muted yellow']
    assert data['bright white'] == ['shiny gold']
    assert data['muted yellow'] == ['shiny gold', 'shiny gold', 'faded blue', 'faded blue', 'faded blue', 'faded blue',
                                    'faded blue', 'faded blue', 'faded blue', 'faded blue', 'faded blue']
    assert data['shiny gold'] == ['dark olive', 'vibrant plum', 'vibrant plum']
    assert data['dark olive'] == ['faded blue', 'faded blue', 'faded blue', 'dotted black', 'dotted black',
                                  'dotted black', 'dotted black']
    assert data['vibrant plum'] == ['faded blue', 'faded blue', 'faded blue', 'faded blue', 'faded blue',
                                    'dotted black', 'dotted black', 'dotted black', 'dotted black', 'dotted black',
                                    'dotted black']
    assert data['faded blue'] == data['dotted black']


def test_can_bag_be_carried():
    rules = get_data('./data/raw/day7_sample.txt')
    my_bag = 'shiny gold'
    assert can_bag_be_carried(rules, 'light red', my_bag) is True
    assert can_bag_be_carried(rules, 'dark orange', my_bag) is True
    assert can_bag_be_carried(rules, 'bright white', my_bag) is True
    assert can_bag_be_carried(rules, 'muted yellow', my_bag) is True
    assert can_bag_be_carried(rules, 'shiny gold', my_bag) is False
    assert can_bag_be_carried(rules, 'dark olive', my_bag) is False
    assert can_bag_be_carried(rules, 'vibrant plum', my_bag) is False
    assert can_bag_be_carried(rules, 'faded blue', my_bag) is False
    assert can_bag_be_carried(rules, 'dotted black', my_bag) is False


def test_main():
    res = main('./data/raw/day7_sample.txt', 'shiny gold')
    assert res == 4


def test_count_all_bag_capacities():
    rules2 = get_data('./data/raw/day7_sample2.txt')
    sums = count_all_bag_capacities_including_self(rules2, dict())
    assert sums['dark violet'] == 1
    assert sums['dark blue'] == 3
    assert sums['dark green'] == 7
    assert sums['dark yellow'] == 15
    assert sums['dark orange'] == 31
    assert sums['dark red'] == 63
    assert sums['shiny gold'] == 127


def test_count_bag_capacity():
    rules = get_data('./data/raw/day7_sample.txt')
    sums = count_all_bag_capacities_including_self(rules, dict())
    assert count_bag_capacity(sums, rules, 'shiny gold') == 32

    rules2 = get_data('./data/raw/day7_sample2.txt')
    sums2 = count_all_bag_capacities_including_self(rules2, dict())
    assert count_bag_capacity(sums2, rules2, 'shiny gold') == 126
