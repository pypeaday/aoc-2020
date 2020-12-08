

class BootLoader:

    def __init__(self, filepath: str = './data/raw/day8_sample.txt'):
        self.filepath = filepath
        self.instructions = self.get_instructions()

        self.accumulator = 0
        self.instruction_id = 0
        self.next_instruction_id = 0
        self.completed_instructions = []

        self.instruction_map = {
            'nop': self.nop,
            'acc': self.acc,
            'jmp': self.jmp
        }

    def get_instructions(self) -> list:
        _instructions = []
        with open(self.filepath, 'r') as f:
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
            self.instruction_id = self.next_instruction_id


if __name__ == '__main__':
    # solution 1
    bootloader = BootLoader('./data/raw/day8_input.txt')
    bootloader.load()
