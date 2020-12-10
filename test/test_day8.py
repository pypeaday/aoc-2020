import pytest
import os
from src.day8.main import BootLoader, get_raw_instructions, fix_instructions


def test_get_instructions():
    bootloader = BootLoader("./data/raw/day8_sample.txt")
    assert bootloader.instructions[0] == ("nop", 0)
    assert bootloader.instructions[1] == ("acc", 1)
    assert bootloader.instructions[2] == ("jmp", 4)
    assert bootloader.instructions[3] == ("acc", 3)
    assert bootloader.instructions[4] == ("jmp", -3)
    assert bootloader.instructions[5] == ("acc", -99)
    assert bootloader.instructions[6] == ("acc", 1)
    assert bootloader.instructions[7] == ("jmp", -4)
    assert bootloader.instructions[8] == ("acc", 6)


def test_get_raw_instructions():
    raw_instructions = get_raw_instructions("./data/raw/day8_sample.txt")
    assert raw_instructions[0] == ("nop", 0)
    assert raw_instructions[1] == ("acc", 1)
    assert raw_instructions[2] == ("jmp", 4)
    assert raw_instructions[3] == ("acc", 3)
    assert raw_instructions[4] == ("jmp", -3)
    assert raw_instructions[5] == ("acc", -99)
    assert raw_instructions[6] == ("acc", 1)
    assert raw_instructions[7] == ("jmp", -4)
    assert raw_instructions[8] == ("acc", 6)


def test_acc():
    bootloader = BootLoader("./data/raw/day8_sample.txt")
    bootloader.acc(1)
    assert bootloader.accumulator == 1
    assert bootloader.next_instruction_id == 1
    assert 0 in bootloader.completed_instructions


def test_jmp():
    bootloader = BootLoader("./data/raw/day8_sample.txt")
    bootloader.jmp(1)
    assert bootloader.next_instruction_id == 1
    assert 0 in bootloader.completed_instructions

    bootloader.jmp(-1)
    assert bootloader.next_instruction_id == 0


def test_catch_infinite_loop():
    bootloader = BootLoader("./data/raw/day8_sample.txt")

    with pytest.raises(SystemError):
        bootloader.load()
        assert bootloader.accumulator == 5


def test_successful_boot():
    bootloader = BootLoader("./data/raw/day8_sample2.txt")
    assert bootloader.load() == 8


def test_fix_instructions():
    res = fix_instructions("./data/raw/day8_sample.txt")
    assert res[0] == 8
