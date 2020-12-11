class Seat:
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col
        self.occupied = False


class Lobby:
    def __init__(self, filepath: str = "./data/raw/day11_input.txt") -> None:
        self.grid = self.set_up_grid(filepath)
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
        return grid

    def iterate_round(self):
        """Calculate one round of the model's rules"""
        _new_seats = dict()
        for k, v in self.seats.items():
            n = self.count_adjacent_occupencies(k, v)
            if n == v == 0:  # empty seat surrounded by empty seats
                _new_seats[k] = 1
            elif v == 1 and n >= 4:  # seat is already occupied
                _new_seats[k] = 0  # seat empties
            else:
                _new_seats[k] = v
        self.seats = _new_seats

    def count_adjacent_occupencies(self, k, v):
        """Count number of adjacent seats that are occupied

        Args:
            k ([type]): row, col of the current seat
            v ([type]): 0 or 1 if the seat is empty or occupied
        """
        n = 0
        row, col = k[0], k[1]
        keys_to_check = [
            (row - 1, col - 1),
            (row - 1, col),
            (row - 1, col + 1),
            (row, col - 1),
            (row, col + 1),
            (row + 1, col - 1),
            (row + 1, col),
            (row + 1, col + 1),
        ]
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
        lobby.iterate_round()
        if old_seats == lobby.seats:
            occupied_seats = sum(v for v in old_seats.values())
            return occupied_seats


def main(filepath: str = "./data/raw/day11_sample.txt"):
    num_occupied_seats = calculate_solution_1(filepath)
    print(f"Solution 1: {num_occupied_seats}")


if __name__ == "__main__":
    main("./data/raw/day11_input.txt")
