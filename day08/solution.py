Program = list[tuple[str, int]]

class HandheldGameConsole():
    def __init__(self, program: Program) -> None:
        self.counter = 0 # program counter
        self.accumulator = 0
        self.program = program

    def _execute_instruction(self) -> None: 
        op, val = self.program[self.counter]
        if op == 'acc':
            self.accumulator += val
            self.counter += 1
        elif op == 'jmp':
            self.counter += val
        elif op == 'nop':
            self.counter += 1

    def execute(self) -> None:
        instructions_run = set()
        while self.counter < len(self.program) and not self.counter in instructions_run:
            instructions_run.add(self.counter)
            self._execute_instruction()

    def reset(self) -> None:
        self.counter = 0
        self.accumulator = 0

    def part1(self) -> int:
        self.execute()
        return self.accumulator

    def part2(self) -> int:
        for i, (op, val) in enumerate(self.program):
            if op == 'jmp' or op == 'nop':
                self.program[i] = ({'jmp': 'nop', 'nop': 'jmp'}[op], val)
                self.reset()
                self.execute()
                if self.counter == len(self.program):
                    return self.accumulator
                self.program[i] = (op, val)

    def __str__(self) -> str:
        return f'A HGC with program of len {len(self.program)}'


def get_input() -> HandheldGameConsole:
    with open('input.txt', 'r') as f:
        return HandheldGameConsole([(line.split()[0], int(line.split()[1])) for line in f])

if __name__ == "__main__":
    hgc = get_input()
    print(f'Part 1 answer: {hgc.part1()}')
    print(f'Part 2 answer: {hgc.part2()}')

