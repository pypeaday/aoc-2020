from src.day15.main import (
    get_data,
    instantiate_maps,
    take_turn,
    calculate_solution_1,
    calculate_solution_2,
)


def test_get_data():
    data = get_data()
    assert data == [0, 3, 6]


def test_instantiate_maps():
    data = get_data()
    turn_map, value_map = instantiate_maps(data)
    assert turn_map == {1: 0, 2: 3, 3: 6}
    assert value_map == {0: [1], 3: [2], 6: [3]}


def test_take_turn():
    data = get_data()
    turn_map, value_map = instantiate_maps(data)
    turn_map, value_map = take_turn(turn_map, value_map, len(data) + 1)
    assert turn_map[4] == 0
    assert value_map[0] == [1, 4]
    turn_map, value_map = take_turn(turn_map, value_map, len(data) + 2)
    assert turn_map[5] == 3
    assert value_map[3] == [2, 5]
    turn_map, value_map = take_turn(turn_map, value_map, len(data) + 3)
    assert turn_map[6] == 3
    assert value_map[3] == [2, 5, 6]
    turn_map, value_map = take_turn(turn_map, value_map, len(data) + 4)
    assert turn_map[7] == 1
    assert value_map[1] == [7]
    turn_map, value_map = take_turn(turn_map, value_map, len(data) + 5)
    assert turn_map[8] == 0
    assert value_map[0] == [1, 4, 8]
    turn_map, value_map = take_turn(turn_map, value_map, len(data) + 6)
    assert turn_map[9] == 4
    assert value_map[4] == [9]
    turn_map, value_map = take_turn(turn_map, value_map, len(data) + 7)
    assert turn_map[10] == 0
    assert value_map[0] == [1, 4, 8, 10]


def test_calculate_solution_1():
    data = get_data()
    assert calculate_solution_1(data) == 436
    assert calculate_solution_1([1, 3, 2]) == 1
    assert calculate_solution_1([2, 1, 3]) == 10
    assert calculate_solution_1([1, 2, 3]) == 27
    assert calculate_solution_1([2, 3, 1]) == 78
    assert calculate_solution_1([3, 2, 1]) == 438
    assert calculate_solution_1([3, 1, 2]) == 1836


def test_calculate_solution_2():
    assert calculate_solution_2() == 208
