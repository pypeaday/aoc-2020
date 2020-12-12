class Ship:
    def __init__(
        self,
        filepath: str = "./dara/raw/day12_sample.txt",
        orientation: str = "E",
    ):
        self.instructions = self.get_instructions(filepath)
        self.orient_map = ["N", "E", "S", "W"]
        self.orientation = orientation

        self.position = {"N": 0, "S": 0, "E": 0, "W": 0}

    @staticmethod
    def get_instructions(filepath: str):
        _input = []
        with open(filepath, "r") as f:
            lines = f.readlines()
            for line in lines:
                _input.append(line.strip())
        return _input

    def change_orientation(self, instruction: str):
        cur_id = self.orient_map.index(self.orientation)
        direction, value = instruction[0], int(instruction[1:])
        id_delta = value // 90
        if direction == "R":
            new_id = (cur_id + id_delta) % 4
        elif direction == "L":
            new_id = (cur_id - id_delta) % 4
        else:
            raise ValueError("Undefined direction: expected L or R")
        self.orientation = self.orient_map[new_id]

    def advance_position(self, instruction: str):
        cmd, value = instruction[0], int(instruction[1:])
        if cmd == "F":
            self.position[self.orientation] += value
        elif cmd in self.orient_map:
            self.position[cmd] += value
        else:
            raise ValueError(
                f"Received unknown cmd: {cmd} to advance_position()"
            )

    def carry_out_instructions(self):
        for instruction in self.instructions:
            if instruction[0] in ["L", "R"]:
                self.change_orientation(instruction)
            elif instruction[0] in self.orient_map or instruction[0] == "F":
                self.advance_position(instruction)
            else:
                raise ValueError(f"Unknown instruction: {instruction}")

    def manhattan_distance(self):
        return sum(
            [
                abs(self.position["E"] - self.position["W"]),
                abs(self.position["N"] - self.position["S"]),
            ]
        )


def calculate_solution_1(filepath: str = "./data/raw/day12_sample.txt"):
    ship = Ship(filepath, "E")
    ship.carry_out_instructions()
    return ship.manhattan_distance()


def main(filepath: str = "./data/raw/day12_sample.txt."):
    sol_1 = calculate_solution_1(filepath)
    print(f"Solution 1: {sol_1}")


if __name__ == "__main__":
    main("./data/raw/day12_input.txt")
