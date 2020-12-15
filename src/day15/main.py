from tqdm import tqdm
from collections import defaultdict


def get_data(filepath: str = "./data/raw/day15_sample.txt"):
    """Return raw data in a list

    Args:
        filepath (str, optional): Defaults to "./data/raw/day15_sample.txt".

    Returns:
        [list]: raw data in a list
    """
    with open(filepath, "r") as f:
        line = f.readline()
        data = [int(x) for x in line.split(",")]
    return data


def instantiate_maps(data: list):
    """Create initial maps based on raw data

    Args:
        data (list): raw data from get_data()

    Returns:
        dicts: turn_map and value_map
            turn_map is keyed by a turn id with the value said at that turn
            value_map is keyed by a value and contains a list of turn ids at
                which that value was said
    """
    turn_map = {k: v for k, v in zip(range(1, len(data) + 1), data)}
    value_map = defaultdict(list)
    for i, k in enumerate(data):
        value_map[k].append(i + 1)

    return turn_map, value_map


def take_turn(turn_map: dict, value_map: dict, turn_id: int):
    """Take a turn of the memory game

    Args:
        turn_map (dict): current turn_map up to date through turn_id-1
        value_map (dict): current value_map up to date through turn_id-1
        turn_id (int): the current turn number

    Returns:
        [type]: updated turn_map and value_map
    """
    if (
        turn_map[turn_id - 1] in value_map.keys()
        and len(value_map[turn_map[turn_id - 1]]) == 1
    ):
        turn_map[turn_id] = 0
        value_map[0].append(turn_id)
    else:
        turn_map[turn_id] = (
            value_map[turn_map[turn_id - 1]][-1]
            - value_map[turn_map[turn_id - 1]][-2]
        )
        value_map[turn_map[turn_id]].append(turn_id)
    return turn_map, value_map


def calculate_solution_1(data: list):
    turn_map, value_map = instantiate_maps(data)
    turn_id = len(data) + 1
    for i in range(turn_id, 2021):
        turn_map, value_map = take_turn(turn_map, value_map, i)

    return turn_map[2020]


def calculate_solution_2(data: list):
    turn_map, value_map = instantiate_maps(data)
    turn_id = len(data) + 1
    for i in tqdm(range(turn_id, 30000001)):
        turn_map, value_map = take_turn(turn_map, value_map, i)

    return turn_map[30000000]


def main(filepath: str = "./data/raw/day15_sample.txt."):
    data = get_data(filepath)
    sol_1 = calculate_solution_1(data)
    print(f"Solution 1: {sol_1}")

    sol_2 = calculate_solution_2(data)
    print(f"Solution 2: {sol_2}")


if __name__ == "__main__":
    main("./data/raw/day15_input.txt")
