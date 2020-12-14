from itertools import product
import re

BitProgram = list[str]
N = 36 # bitlength

class BitComputer():
    def __init__(self, program: BitProgram, decoder_chip_version: int=1) -> None:
        self.program = program
        self.mask = 'X'*N
        self.counter = 0
        self.memory = {}
        self.decoder_chip_version = decoder_chip_version

    def _update(self, location: int, value: int) -> None:
        if self.decoder_chip_version == 1:
            self.memory[location] = 0
            for i in range(N):
                self.memory[location] += (1 << i) & value if self.mask[i] == 'X' else int(self.mask[i]) * (1 << i)
        
        elif self.decoder_chip_version == 2:
            location_mask = [str(int(bool((1 << i) & location))) if self.mask[i] == '0' else self.mask[i] for i in range(N)]
            xs = location_mask.count('X')
            if xs == 0:
                self.memory[sum(1 << i for i in range(N) if location_mask[i] == '1')] = value
            else:
                for inj in product(['0', '1'], repeat=xs):
                    inj_loc = list(location_mask)
                    j = 0
                    for i, val in enumerate(inj_loc):
                        if val == 'X':
                            inj_loc[i] = inj[j]
                            j += 1
                    self.memory[sum(1 << i for i in range(N) if inj_loc[i] == '1')] = value


    def _execute_next_instruction(self) -> None:
        if self.program[self.counter].startswith('mask'):
            d = re.match(r'mask = (?P<mask>.+)', self.program[self.counter]).groupdict()
            self.mask = d['mask'][::-1]
        else:
            d = re.match(r'mem\[(?P<location>\d+)\] = (?P<value>\d+)', self.program[self.counter]).groupdict()
            location, value = map(int, (d['location'], d['value']))
            self._update(location, value)
        self.counter += 1

    def run(self) -> None:
        while 0 <= self.counter < len(self.program):
            self._execute_next_instruction()



def get_input() -> list[list[str]]:
    with open('input.txt', 'r') as f:
        return [line.strip() for line in f if line]
    
def part_1(program) -> int:
    c = BitComputer(program)
    c.run()
    return sum(c.memory.values()) 

def part_2(answers) -> int:
    c = BitComputer(program, decoder_chip_version=2)
    c.run()
    return sum(c.memory.values()) 

if __name__ == "__main__":
    program = get_input()
    print(f'Part 1 answer: {part_1(program)}')
    print(f'Part 2 answer: {part_2(program)}')

