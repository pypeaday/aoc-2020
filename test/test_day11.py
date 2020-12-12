from src.day11.main import Lobby, calculate_solution_1, calculate_solution_2


def test_Lobby_init():
    lobby = Lobby("./data/raw/day11_sample.txt")
    floor_points = [
        (0, 1),
        (0, 4),
        (0, 7),
        (1, 7),
        (2, 1),
        (2, 3),
        (2, 5),
        (2, 6),
        (2, 8),
        (2, 9),
        (3, 4),
        (3, 7),
        (4, 1),
        (4, 4),
        (4, 7),
        (5, 1),
        (5, 7),
        (6, 0),
        (6, 1),
        (6, 3),
        (6, 5),
        (6, 6),
        (6, 7),
        (6, 8),
        (6, 9),
        (8, 1),
        (8, 8),
        (9, 1),
        (9, 7),
    ]
    for k, v in lobby.grid.items():
        if v == "floor":
            assert k in floor_points


def test_Lobby_algorithm():
    lobby = Lobby("./data/raw/day11_sample.txt")
    lobby.iterate_round()
    for k, v in lobby.seats.items():
        assert v == 1

    round_2_occupied = [
        (0, 0),
        (0, 6),
        (0, 8),
        (0, 9),
        (1, 0),
        (1, 9),
        (3, 0),
        (3, 9),
        (4, 0),
        (5, 0),
        (5, 6),
        (5, 8),
        (5, 9),
        (7, 0),
        (7, 9),
        (8, 0),
        (9, 0),
        (9, 8),
        (9, 9),
    ]
    lobby.iterate_round()
    for k in round_2_occupied:
        assert lobby.seats[k] == 1

    lobby.iterate_round()
    lobby.iterate_round()
    lobby.iterate_round()

    round_5_seats = {k: v for k, v in lobby.seats.items()}
    lobby.iterate_round()
    for k, v in lobby.seats.items():
        assert round_5_seats[k] == v


def test_calculate_solution_1():
    assert calculate_solution_1("./data/raw/day11_sample.txt") == 37


def test_calculate_solution_2():
    assert calculate_solution_2("./data/raw/day11_sample.txt.") == 26
