from src.day14.main import (
    get_data,
    int236bitbin,
    apply_mask,
    bin2int,
    apply_floating_mask,
    decode_floating_address,
    apply_mask_v2,
    calculate_solution_1,
    calculate_solution_2,
)


def test_get_data():
    data = get_data()
    assert data[0][0] == "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
    assert data[0][1] == {8: "0", 7: "101"}


def test_transform_integer():
    assert int236bitbin("0") == "000000000000000000000000000000000000"
    assert int236bitbin("101") == "000000000000000000000000000001100101"
    assert int236bitbin("11") == "000000000000000000000000000000001011"


def test_apply_mask():
    data = get_data()
    mask = data[0][0]
    addr_map = data[0][1]
    assert bin2int(apply_mask(mask, addr_map[8])) == 64
    assert bin2int(apply_mask(mask, addr_map[7])) == 101


def test_apply_floating_mask():
    mask = "000000000000000000000000000000X1001X"
    address = 42
    assert (
        apply_floating_mask(mask, address)
        == "000000000000000000000000000000X1101X"
    )
    mask = "00000000000000000000000000000000X0XX"
    address = 26
    assert (
        apply_floating_mask(mask, address)
        == "00000000000000000000000000000001X0XX"
    )


def test_decode_floating_address():
    floating_addr = "000000000000000000000000000000X1101X"
    addrs = decode_floating_address(floating_addr)
    assert "000000000000000000000000000000011010" in addrs
    assert "000000000000000000000000000000011011" in addrs
    assert "000000000000000000000000000000111010" in addrs
    assert "000000000000000000000000000000111011" in addrs


def test_apply_mask_v2():
    mask = "000000000000000000000000000000X1001X"
    address = 42
    value = "100"
    res = apply_mask_v2(mask, address, value)
    assert res[26] == res[27] == res[58] == res[59] == 100


def test_calculate_solution_1():
    assert calculate_solution_1() == 165


def test_calculate_solution_2():
    assert calculate_solution_2() == 208
