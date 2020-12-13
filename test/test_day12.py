import pytest
from src.day12.main import Ship, ShipWithWaypoint


def test_get_instructions():
    instructions = Ship.get_instructions("./data/raw/day12_sample.txt")
    assert instructions[0] == "F10"
    assert instructions[1] == "N3"
    assert instructions[2] == "F7"
    assert instructions[3] == "R90"
    assert instructions[4] == "F11"


def test_change_orientation():
    ship = Ship("./data/raw/day12_sample.txt", orientation="E")
    ship.change_orientation("R90")
    assert ship.orientation == "S"
    ship.change_orientation("L90")
    assert ship.orientation == "E"
    ship.change_orientation("R270")
    assert ship.orientation == "N"


def test_advance_position():
    ship = Ship("./data/raw/day12_sample.txt", orientation="E")
    ship.advance_position("F10")
    assert ship.position["E"] == 10
    ship.advance_position("E5")
    assert ship.position["E"] == 15
    with pytest.raises(ValueError):
        ship.advance_position("R90")


def test_carry_out_instructions():
    ship = Ship("./data/raw/day12_sample.txt", orientation="E")
    ship.carry_out_instructions()
    ew = abs(ship.position["E"] - ship.position["W"])
    ns = abs(ship.position["N"] - ship.position["S"])
    assert ns + ew == 25


def test_manhattan_distance():
    ship = Ship("./data/raw/day12_sample.txt", orientation="E")
    ship.carry_out_instructions()
    assert ship.manhattan_distance() == 25


def test_move_waypoint():
    ship = ShipWithWaypoint("./data/raw/day12_sample.txt", "E")
    ship.move_waypoint("R90")
    assert ship.relative_waypoint_position["E"] == 1
    assert ship.relative_waypoint_position["S"] == 10
    assert ship.relative_waypoint_position["W"] == 0
    assert ship.relative_waypoint_position["N"] == 0


def test_calculate_solution_2():
    ship = ShipWithWaypoint("./data/raw/day12_sample.txt", "E")
    ship.carry_out_instructions()
    assert ship.manhattan_distance() == 286
