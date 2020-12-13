def get_next_departure_time(earliest_ts: int = 939, bus_id: int = 7):
    return earliest_ts - earliest_ts % bus_id + bus_id


def get_data(filepath: str = "./data/raw/day13_sample.txt"):
    data = []
    with open(filepath, "r") as f:
        lines = f.readlines()
        data.append(int(lines[0]))
        for line in lines[1].split(","):
            if line == "x":
                continue
            data.append(int(line))

    return data


def calculate_solution_1(filepath: str = "./data/raw/day13_sample.txt"):
    data = get_data(filepath)
    next_timestamps = map(
        get_next_departure_time,
        [data[0] for _ in range(len(data[1:]))],
        data[1:],
    )
    ts = [x for x in next_timestamps]
    next_ts = min(ts)
    bus_id_index = ts.index(next_ts)
    bus_id = data[1:][bus_id_index]
    delta = next_ts - data[0]
    return delta * bus_id


def calculate_solution_2(filepath: str = "./dataraw/day13_sample.txt"):
    pass


def main(filepath: str = "./data/raw/day13_sample.txt."):
    sol_1 = calculate_solution_1(filepath)
    print(f"Solution 1: {sol_1}")

    sol_2 = calculate_solution_2(filepath)
    print(f"Solution 2: {sol_2}")


if __name__ == "__main__":
    main("./data/raw/day13_input.txt")
