from src.day16.main import (
    get_data,
    get_any_possible_values,
    get_valid_tickets,
    get_possible_index,
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


def test_get_valid_tickets():
    fields, tickets = get_data()
    possible_values = get_any_possible_values(fields)
    assert get_valid_tickets(tickets, set(possible_values)) == [
        [7, 1, 14],
        [7, 3, 47],
    ]
    assert len(get_valid_tickets(tickets, set(possible_values))) == 2


def test_get_possible_index():
    fields, tickets = get_data("./data/raw/day16_sample2.txt")
    possible_values = set(get_any_possible_values(fields))
    tickets = get_valid_tickets(tickets, possible_values)
    field_index = get_possible_index(fields, tickets[0])
    assert field_index["class"] == [0, 1, 2]
    assert field_index["row"] == [0, 1, 2]
    assert field_index["seat"] == [0, 1, 2]
    field_index = get_possible_index(fields, tickets[1])
    assert field_index["class"] == [1, 2]
    assert field_index["row"] == [0, 1, 2]
    assert field_index["seat"] == [0, 1, 2]


def test_calculate_solution_1():
    fields, tickets = get_data()
    assert calculate_solution_1(fields, tickets) == 71


def test_calculate_solution_2():
    fields, tickets = get_data("./data/raw/day16_sample2.txt")
    # Not a great test but solution 2 only returns the product
    assert calculate_solution_2(fields, tickets) == 1
