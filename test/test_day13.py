from src.day13.main import (
    get_next_departure_time,
    calculate_solution_1,
    get_data,
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
