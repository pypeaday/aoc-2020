import pytest
import os
from src.day4.main import (
    get_data,
    format_data,
    is_passport_valid,
    main,
    check_height,
    VALIDATION_SCHEMA,
)


def test_get_data():
    inputs = get_data("./data/raw/day4_sample.txt")

    assert (
        inputs[0]
        == "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"
    )
    assert (
        inputs[1]
        == "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929"
    )
    assert (
        inputs[2]
        == "hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm"
    )
    assert inputs[3] == "hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in"


def test_format_data():
    inputs = get_data("./data/raw/day4_sample.txt")
    formatted_inputs = format_data(inputs)
    assert formatted_inputs[0]["ecl"] == "gry"
    assert formatted_inputs[0]["pid"] == "860033327"
    assert formatted_inputs[0]["eyr"] == "2020"
    assert formatted_inputs[0]["hcl"] == "#fffffd"
    assert formatted_inputs[0]["byr"] == "1937"
    assert formatted_inputs[0]["iyr"] == "2017"
    assert formatted_inputs[0]["cid"] == "147"
    assert formatted_inputs[0]["hgt"] == "183cm"

    assert formatted_inputs[1]["ecl"] == "amb"
    assert formatted_inputs[1]["pid"] == "028048884"
    assert formatted_inputs[1]["eyr"] == "2023"
    assert formatted_inputs[1]["hcl"] == "#cfa07d"
    assert formatted_inputs[1]["byr"] == "1929"
    assert formatted_inputs[1]["iyr"] == "2013"
    assert formatted_inputs[1]["cid"] == "350"

    assert formatted_inputs[2]["ecl"] == "brn"
    assert formatted_inputs[2]["pid"] == "760753108"
    assert formatted_inputs[2]["eyr"] == "2024"
    assert formatted_inputs[2]["hcl"] == "#ae17e1"
    assert formatted_inputs[2]["byr"] == "1931"
    assert formatted_inputs[2]["iyr"] == "2013"
    assert formatted_inputs[2]["hgt"] == "179cm"

    assert formatted_inputs[3]["ecl"] == "brn"
    assert formatted_inputs[3]["pid"] == "166559648"
    assert formatted_inputs[3]["eyr"] == "2025"
    assert formatted_inputs[3]["hcl"] == "#cfa07d"
    assert formatted_inputs[3]["iyr"] == "2011"
    assert formatted_inputs[3]["hgt"] == "59in"


def test_is_passport_valid():
    inputs = get_data("./data/raw/day4_sample.txt")
    formatted_inputs = format_data(inputs)

    assert is_passport_valid(formatted_inputs[0]) is True
    assert is_passport_valid(formatted_inputs[1]) is False
    assert is_passport_valid(formatted_inputs[2]) is True
    assert is_passport_valid(formatted_inputs[3]) is False


def test_is_passport_valid2():
    inputs = get_data("./data/raw/day4_sample2.txt")
    formatted_inputs = format_data(inputs)

    assert is_passport_valid(formatted_inputs[0], VALIDATION_SCHEMA) is False
    assert is_passport_valid(formatted_inputs[1], VALIDATION_SCHEMA) is False
    assert is_passport_valid(formatted_inputs[2], VALIDATION_SCHEMA) is False
    assert is_passport_valid(formatted_inputs[3], VALIDATION_SCHEMA) is False
    assert is_passport_valid(formatted_inputs[4], VALIDATION_SCHEMA) is True
    assert is_passport_valid(formatted_inputs[5], VALIDATION_SCHEMA) is True
    assert is_passport_valid(formatted_inputs[6], VALIDATION_SCHEMA) is True
    assert is_passport_valid(formatted_inputs[7], VALIDATION_SCHEMA) is True


def test_check_height():
    assert check_height("183cm") is True
    assert check_height("194cm") is False
    assert check_height("54in") is False
    assert check_height("64in") is True


def test_main():
    assert main("./data/raw/day4_sample.txt") == 2
    assert main("./data/raw/day4_sample2.txt", True) == 4
