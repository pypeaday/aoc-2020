from src.day14.main import (
    get_data,
    transform_integer,
    apply_mask,
    calculate_solution_1,
    calculate_solution_2,
)


def test_get_data():
    data = get_data()
    assert data[0][0] == "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
    assert data[0][1] == {8: "0", 7: "101"}


def test_transform_integer():
    assert transform_integer("0") == "000000000000000000000000000000000000"
    assert transform_integer("101") == "000000000000000000000000000001100101"
    assert transform_integer("11") == "000000000000000000000000000000001011"


def test_apply_mask():
    data = get_data()
    mask = data[0][0]
    addr_map = data[0][1]
    assert apply_mask(mask, addr_map[8]) == 64
    assert apply_mask(mask, addr_map[7]) == 101


def test_calculate_solution_1():
    assert calculate_solution_1() == 165