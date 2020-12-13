def get_next_departure_time(earliest_ts: int = 939, bus_id: int = 7):
    return earliest_ts - earliest_ts % bus_id + bus_id


def get_data(filepath: str = "./data/raw/day13_sample.txt"):
    data = []
    with open(filepath, "r") as f:
        lines = f.readlines()
        data.append(int(lines[0]))
        for line in lines[1].split(","):
            if line == "x":
                data.append(line)
            else:
                data.append(int(line))

    return data


def get_part_2_inputs(data: list):
    """Returns 2 lists formatted for solving the
    Chinese Remainder Theorem solving for t such that:
    t = a[0] mod n[0]
    t = a[1] mod n[1]
    ...

    Args:
        data (list): raw data from get_data()

    Returns:
        n, a: principle inputs, remainders
    """
    a = []
    n = []
    for i, x in enumerate(data[1:]):
        if x == "x":
            continue
        a.append((x - i) % x)
        n.append(x)

    return n, a


def calculate_solution_1(filepath: str = "./data/raw/day13_sample.txt"):
    data = get_data(filepath)
    bus_ids = [x for x in data[1:] if x != "x"]
    next_timestamps = map(
        get_next_departure_time,
        [data[0] for _ in range(len(bus_ids))],
        bus_ids,
    )
    ts = [x for x in next_timestamps]
    next_ts = min(ts)
    bus_id_index = ts.index(next_ts)
    bus_id = bus_ids[bus_id_index]
    delta = next_ts - data[0]
    return delta * bus_id


def extended_euclidean(a: int, b: int):
    """extension to the Euclidean algorithm, and
     computes, in addition to the greatest common divisor
     (gcd) of integers a and b, also the coefficients of
     Bézout's identity
     # https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm

     ax + by = gcd(a, b)

    Args:
        a (int):
        b (int):

    Returns:
        [type]: greatest common divisor, bezout's id coefficients
    """
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_euclidean(b % a, a)
        return g, x - (b // a) * y, y


def inverse_modulo(a, m):
    """Return inverse modulo

    Args:
        a ([type]): remainder
        m ([type]): modulo

    Returns:
        [type]: modulo inverse
    """
    g, x, y = extended_euclidean(a, m)
    return x % m


def crt(m: list, a: list):
    """Chinese Remainder Algorithm over multiple inputs

    Args:
        m (list): list of modulii
        a (list): list of remainders

    Returns:
        [type]: t such that t = a[i] mod(m[i])
    """
    while True:
        temp1 = (
            inverse_modulo(m[1], m[0]) * a[0] * m[1]
            + inverse_modulo(m[0], m[1]) * a[1] * m[0]
        )
        temp2 = m[0] * m[1]
        if len(a) > 2:
            a = [temp1 % temp2] + a[2:]
        else:
            return [temp1 % temp2]
        m = [temp2] + m[2:]


def calculate_solution_2(filepath: str = "./data/raw/day13_sample.txt"):
    data = get_data(filepath)
    n, a = get_part_2_inputs(data)
    res = crt(n, a)
    return res


def main(filepath: str = "./data/raw/day13_sample.txt."):
    sol_1 = calculate_solution_1(filepath)
    print(f"Solution 1: {sol_1}")

    sol_2 = calculate_solution_2(filepath)
    print(f"Solution 2: {sol_2}")


if __name__ == "__main__":
    main("./data/raw/day13_input.txt")
