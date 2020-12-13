from src.day13.main import (
    get_next_departure_time,
    calculate_solution_1,
    calculate_solution_2,
    get_data,
    get_part_2_inputs,
    crt,
)


def test_get_data():
    data = get_data()
    assert data[0] == 939
    assert data[1:] == [7, 13, -99, -99, 59, -99, 31, 19]


def test_get_next_departure_time():
    assert get_next_departure_time(bus_id=7) == 945
    assert get_next_departure_time(bus_id=13) == 949
    assert get_next_departure_time(bus_id=59) == 944


def test_calculate_solution_1():
    res = calculate_solution_1("./data/raw/day13_sample.txt")
    assert res == 295


def test_get_part_2_inputs():
    data = get_data()
    n, a = get_part_2_inputs(data)
    assert n == [7, 13, 59, 31, 19]
    assert a == [0, 12, 55, 25, 12]


def test_crt():
    data = get_data()
    n, a = get_part_2_inputs(data)
    res = crt(n, a)
    assert res == 1068781

    data = [939, 17, "x", 13, 19]
    n, a = get_part_2_inputs(data)
    assert crt(n, a) == 3417

    data = [939, 67, 7, 59, 61]
    n, a = get_part_2_inputs(data)
    assert crt(n, a) == 754018

    data = [939, 67, "x", 7, 59, 61]
    n, a = get_part_2_inputs(data)
    assert crt(n, a) == 779210

    data = [939, 67, 7, "x", 59, 61]
    n, a = get_part_2_inputs(data)
    assert crt(n, a) == 1261476

    data = [939, 1789, 37, 47, 1889]
    n, a = get_part_2_inputs(data)
    assert crt(n, a) == 1202161486


def test_calculate_solution_2():
    assert calculate_solution_2("./data/raw/day13_sample.txt") == 1068781
