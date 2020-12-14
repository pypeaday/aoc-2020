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


def transform_integer(value: str) -> str:
    return format(int(value), "036b")


def apply_mask(mask: str, value: str) -> int:
    """apply a given 32-bit mask to an integer


    Args:
        mask (str): 32 bit mask of X, 0, 1
        value (str): integer to be expanded into 32 bits
            note the integer is in str format

    Returns:
        int: [description]
    """
    integer = transform_integer(value)
    res = ""
    for m, i in zip(mask, integer):
        if m.lower() == "x":
            res += i
        else:
            res += m
    return int(res, 2)


def calculate_solution_1(filepath: str = "./data/raw/day14_sample.txt"):
    data = get_data(filepath)
    solution_map = dict()
    for ls in data:
        mask, addr_map = ls[0], ls[1]
        for k, v in addr_map.items():
            solution_map[k] = apply_mask(mask, v)

    return sum(v for v in solution_map.values())


def calculate_solution_2(filepath: str = "./data/raw/day14_sample.txt"):
    pass


def main(filepath: str = "./data/raw/day13_sample.txt."):
    sol_1 = calculate_solution_1(filepath)
    print(f"Solution 1: {sol_1}")

    sol_2 = calculate_solution_2(filepath)
    print(f"Solution 2: {sol_2}")


if __name__ == "__main__":
    main("./data/raw/day14_input.txt")
