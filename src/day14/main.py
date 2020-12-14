import copy
from typing import Union
import itertools


def get_data(filepath: str = "./data/raw/day14_sample.txt"):
    """Loads data for day 14 and returns list of formatted inputs

    Args:
        filepath (str, optional): [description]. Defaults to
         "./data/raw/day14_sample.txt".

    Returns:
        [type]: list of inputs

        example:
        data: mask = 01101X001X111X010X0000X1001X010XX0X0
              mem[4841] = 3942
              mem[9168] = 414370178
              mask = 0110010011X1X1X0000000XX0110000XX111
              mem[33062] = 288
              mem[20612] = 182
        return: [(01101X001X111X010X0000X1001X010XX0X0,
                    {4841: 3942, 9168: 414370178}),
                (0110010011X1X1X0000000XX0110000XX111,
                    {33062: 288, 20612: 182})]
    """
    data = []
    mask_ids = []
    _id = -1
    with open(filepath, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.split(" = ") == "mask":
                _id += 1
            else:
                mask_ids.append(_id)

    with open(filepath, "r") as f:
        lines = f.readlines()
        mask_id = -1
        mask_val = "X" * 36
        addr_values = dict()
        for _line in lines:
            _type, val = (
                _line.replace("\n", "").split(" = ")[0],
                _line.replace("\n", "").split(" = ")[1],
            )
            if _type == "mask":
                data.append([mask_val, addr_values])
                mask_val = val
                mask_id += 1
                addr_values = dict()
            else:
                addr = int(_type.replace("mem[", "").replace("]", ""))
                mem_val = val
                addr_values[addr] = mem_val
        data.append([mask_val, addr_values])
    return data[1:]  # start at 1 because id 0 is ['X'*36, {}]


def int236bitbin(value: Union[int, str]) -> str:
    return format(int(value), "036b")


def apply_mask(mask: str, value: str) -> str:
    """apply a given 36-bit mask to an integer


    Args:
        mask (str): 36 bit mask of X, 0, 1
        value (str): integer to be expanded into 36 bits
            note the integer is in str format

    Returns:
        str: 36 bit value representation
    """
    integer = int236bitbin(value)
    res = ""
    for m, i in zip(mask, integer):
        if m.lower() == "x":
            res += i
        else:
            res += m
    return res


def bin2int(value: str) -> int:
    return int(value, 2)


def apply_floating_mask(mask: str, address: int) -> str:
    """Aply 36 bit mask according to part 2 rules

    Args:
        mask (str): 36 bit mask
        address (int): integer address

    Returns:
        str: floating address
    """
    encoded_address = int236bitbin(address)
    res = ""
    for m, i in zip(mask, encoded_address):
        if m == "0":
            res += i
        elif m == "1":
            res += "1"
        elif m.upper() == "X":
            res += "X"
    return res


def decode_floating_address(floating_address: str) -> list:
    """return all possible addresses based on floating
        address input

    Args:
        floating_address (str): 36 bit floating address
            note: result of apply_floating_mask()

    Returns:
        list: list of possible addresses
    """
    num_floats = floating_address.count("X")
    combos = itertools.product("01", repeat=num_floats)
    decoded_addresses = []
    for combo in combos:
        new_addr = copy.copy(floating_address)
        for v in combo:
            new_addr = new_addr.replace("X", v, 1)
        decoded_addresses.append(new_addr)
    return decoded_addresses


def apply_mask_v2(mask: str, address: int, value: str) -> dict:
    """apply a given 36-bit mask to a memory address and
    write the value to the resulting decoded addressed

    Args:
        mask (str): 36-bit mask
        address (int): memory address to decode
        value (str): value to write to addresses

    Returns:
        dict: dict of decoded memory addresses valued by value,
        keyed by the integer representation of the binary address
    """
    floating_address = apply_floating_mask(mask, address)
    keys = decode_floating_address(floating_address)
    res = {bin2int(k): int(value) for k in keys}
    return res


def calculate_solution_1(filepath: str = "./data/raw/day14_sample.txt"):
    data = get_data(filepath)
    solution_map = dict()
    for ls in data:
        mask, addr_map = ls[0], ls[1]
        for k, v in addr_map.items():
            solution_map[k] = bin2int(apply_mask(mask, v))

    return sum(v for v in solution_map.values())


def calculate_solution_2(filepath: str = "./data/raw/day14_sample2.txt"):
    data = get_data(filepath)
    solution_map = dict()
    for ls in data:
        mask, addr_map = ls[0], ls[1]
        for k, v in addr_map.items():
            res = apply_mask_v2(mask, k, v)
            solution_map.update(res)
    return sum(v for v in solution_map.values())


def main(filepath: str = "./data/raw/day14_sample.txt."):
    sol_1 = calculate_solution_1(filepath)
    print(f"Solution 1: {sol_1}")

    sol_2 = calculate_solution_2(filepath.replace("sample", "sample2"))
    print(f"Solution 2: {sol_2}")


if __name__ == "__main__":
    main("./data/raw/day14_input.txt")
