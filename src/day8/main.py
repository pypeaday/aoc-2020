from typing import Union
import copy


class BootLoader:

    def __init__(self, filepath: str = './data/raw/day8_sample.txt', instructions: Union[None, list] = None):
        if instructions is not None:
            self.instructions = instructions
        else:
            self.filepath = filepath
            self.instructions = self.get_instructions(self.filepath)

        self.accumulator = 0
        self.instruction_id = 0
        self.next_instruction_id = 0
        self.completed_instructions = []

        self.instruction_map = {
            'nop': self.nop,
            'acc': self.acc,
            'jmp': self.jmp
        }

    @staticmethod
    def get_instructions(filepath) -> list:
        _instructions = []
        with open(filepath, 'r') as f:
            lines = f.readlines()
            for line in lines:
                op = line.split(' ')[0]
                val = int(line.split(' ')[1].replace('\n', ''))
                _instructions.append((op, val))
        return _instructions

    def acc(self, acc):
        self.accumulator += acc
        self.completed_instructions.append(self.instruction_id)
        self.next_instruction_id += 1

    def jmp(self, jmp):
        self.completed_instructions.append(self.instruction_id)
        self.next_instruction_id += jmp

    def nop(self, *args):
        self.completed_instructions.append(self.instruction_id)
        self.next_instruction_id += 1

    def load(self):
        booting = True
        while booting:
            _func_name, val = self.instructions[self.instruction_id]
            _func = self.instruction_map[_func_name]
            _func(val)
            if self.next_instruction_id in self.completed_instructions:
                raise SystemError(f'Infinite loop detected on instruction id {self.next_instruction_id}. \n'
                                  f'Current accumulator value is {self.accumulator}')
            if self.next_instruction_id == len(self.instructions):
                booting = False
            self.instruction_id = self.next_instruction_id
        print('Sucessfully booted')
        return self.accumulator


def get_raw_instructions(filepath: str = './data/raw/day8_sample.txt'):
    return BootLoader.get_instructions(filepath)


def catch(error, default, instructions):
    bootloader = BootLoader(instructions=instructions)
    try:
        return bootloader.load()
    except error:
        return default


def fix_instructions(filepath: str = './data/raw/day8_sample.txt'):
    raw_instructions = BootLoader.get_instructions(filepath)
    instruction_list = []
    for i, inst in enumerate(raw_instructions):
        # make attempted instructions for changing one jmp to nop
        if inst[0] == 'jmp':
            new_instructions = copy.deepcopy(raw_instructions)
            new_instructions[i] = ('nop', inst[1])
            instruction_list.append(new_instructions)

        # make attempted instructions for changing one nop to jmp
        elif inst[0] == 'nop':
            new_instructions = copy.deepcopy(raw_instructions)
            new_instructions[i] = ('jmp', inst[1])
            instruction_list.append(new_instructions)

    res = map(catch,
              [SystemError for _ in range(len(instruction_list))],
              [None for _ in range(len(instruction_list))],
              instruction_list)

    return [x for x in res if x is not None]


if __name__ == '__main__':
    # solution 1
    bootloader = BootLoader('./data/raw/day8_input.txt')
    try:
        bootloader.load()
    except SystemError:
        pass

    # solution 2
    # res =fix_instructions('./data/raw/day8_sample.txt')
    res = fix_instructions('./data/raw/day8_input.txt')
    print(f'Accumulator value with fixed instructions after successful boot is: {res[0]}')
