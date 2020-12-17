from src.day16.main import (
    get_data,
    get_any_possible_values,
    calculate_solution_1,
    calculate_solution_2,
)


def test_get_data():
    fields, tickets = get_data()
    assert fields["class"] == [1, 2, 3, 5, 6, 7]
    rows = [x for x in range(6, 12)]
    rows.extend([x for x in range(33, 45)])
    assert fields["row"] == rows
    seats = [x for x in range(13, 41)]
    seats.extend([x for x in range(45, 51)])
    assert fields["seat"] == seats

    assert tickets[0] == [7, 1, 14]


def test_get_any_possible_values():
    fields, _ = get_data()
    res = get_any_possible_values(fields)
    vals = [1, 2, 3, 5, 6, 7]
    vals.extend([x for x in range(6, 12)])
    vals.extend([x for x in range(33, 45)])
    vals.extend([x for x in range(13, 41)])
    vals.extend([x for x in range(45, 51)])
    assert res == vals


def test_calculate_solution_1():
    fields, tickets = get_data()
    assert calculate_solution_1(fields, tickets) == 71


def test_calculate_solution_2():
    data = get_data()
    assert calculate_solution_2(data) == 0
