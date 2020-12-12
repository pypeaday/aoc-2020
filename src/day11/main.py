from collections import defaultdict


class Seat:
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col
        self.occupied = False


class Lobby:
    def __init__(self, filepath: str = "./data/raw/day11_input.txt") -> None:
        self.grid, self.M, self.N = self.set_up_grid(filepath)
        self.seats = {k: 0 for k, v in self.grid.items() if v == "seat"}

    @staticmethod
    def set_up_grid(filepath: str) -> dict:
        grid = dict()
        with open(filepath, "r") as f:
            lines = f.readlines()
            for row, _line in enumerate(lines):
                line = _line.replace("\n", "").strip()
                for col, dat in enumerate(line):
                    grid[(row, col)] = "seat" if dat == "L" else "floor"
        return grid, row, col

    def iterate_round(self, part: int = 1, occupied_threshold: int = 4):
        """Calculate one round of the model's rules"""
        _new_seats = dict()
        for k, v in self.seats.items():
            n = self.count_relevant_occupancies(k, v, part)
            if n == v == 0:  # empty seat surrounded by empty seats
                _new_seats[k] = 1
            elif v == 1 and n >= occupied_threshold:  # seat occupied
                _new_seats[k] = 0  # seat empties
            else:
                _new_seats[k] = v
        self.seats = _new_seats

    def map_first_seats_in_sight(self):

        _map = defaultdict(set)
        for seat_coord in self.seats.keys():
            r, c = seat_coord[0], seat_coord[1]
            up_right = False
            down_right = False
            right = False
            down = False
            for i, j in zip(range(1, self.M), range(1, self.N)):
                # check up and right
                if not up_right:
                    _coord = (r - i, c + j)
                    if self.grid.get(_coord, "foo") == "seat":
                        _map[seat_coord].add(_coord)
                        _map[_coord].add(seat_coord)
                        up_right = True
                # check down and right
                if not down_right:
                    _coord = (r + i, c + j)
                    if self.grid.get(_coord, "foo") == "seat":
                        _map[seat_coord].add(_coord)
                        _map[_coord].add(seat_coord)
                        down_right = True
                # check straight right
                if not right:
                    _coord = (r, c + j)
                    if self.grid.get(_coord, "foo") == "seat":
                        _map[seat_coord].add(_coord)
                        _map[_coord].add(seat_coord)
                        right = True
                # check straight down
                if not down:
                    _coord = (r + i, c)
                    if self.grid.get(_coord, "foo") == "seat":
                        _map[seat_coord].add(_coord)
                        _map[_coord].add(seat_coord)
                        down = True
        self.part2_map = _map

    def get_keys_to_check(self, seat_coord: tuple, part: int = 1):
        row, col = seat_coord[0], seat_coord[1]
        if part == 1:
            return [
                (row - 1, col - 1),
                (row - 1, col),
                (row - 1, col + 1),
                (row, col - 1),
                (row, col + 1),
                (row + 1, col - 1),
                (row + 1, col),
                (row + 1, col + 1),
            ]
        elif part == 2:
            # todo
            return self.part2_map[seat_coord]
        else:
            raise NotImplementedError()

    def count_relevant_occupancies(self, k, v, part: int = 1):
        """Count number of adjacent seats that are occupied

        Args:
            k ([type]): row, col of the current seat
            v ([type]): 0 or 1 if the seat is empty or occupied
        """
        n = 0
        keys_to_check = self.get_keys_to_check(k, part)
        for key in keys_to_check:
            if key not in self.grid.keys():
                continue
            elif self.grid[key] == "floor":
                continue
            if self.seats[key]:
                n += 1
        return n


def calculate_solution_1(filepath: str = "./data/raw/day11_sample.txt"):
    lobby = Lobby(filepath)
    stable = False
    while not stable:
        old_seats = {k: v for k, v in lobby.seats.items()}
        lobby.iterate_round(part=1, occupied_threshold=4)
        if old_seats == lobby.seats:
            occupied_seats = sum(v for v in old_seats.values())
            return occupied_seats


def calculate_solution_2(filepath: str = "./data/raw/day11_sample.txt"):
    lobby = Lobby(filepath)
    lobby.map_first_seats_in_sight()
    stable = False
    while not stable:
        old_seats = {k: v for k, v in lobby.seats.items()}
        lobby.iterate_round(part=2, occupied_threshold=5)
        if old_seats == lobby.seats:
            occupied_seats = sum(v for v in old_seats.values())
            return occupied_seats


def main(filepath: str = "./data/raw/day11_sample.txt"):
    num_occupied_seats = calculate_solution_1(filepath)
    print(f"Solution 1: {num_occupied_seats}")

    num_occupied_seats = calculate_solution_2(filepath)
    print(f"Solution 2: {num_occupied_seats}")


if __name__ == "__main__":
    main("./data/raw/day11_input.txt")
