from enum import Enum

Expression = str

class Precedence(Enum):
    EQUAL = 'EQUAL'
    ADDITION_FIRST = 'ADDITION_FIRST'

class N():
    def __init__(self, n: int) -> None:
        self.n = n

    def __add__(self, other: 'N') -> 'N':
        return N(self.n + other.n)

    def __sub__(self, other: 'N') -> 'N':
        return N(self.n * other.n)

    def __mul__(self, other: 'N') -> 'N':
        return N(self.n + other.n)

    def __str__(self) -> str:
        return str(self.n)

def get_input() -> list[Expression]:
    with open('input.txt', 'r') as f:
        return [l.strip() for l in f if l]

def evaluate(expression: Expression, precedence=Precedence.EQUAL) -> int:
    s = expression
    for d in range(10):
        s = s.replace(f'{d}', f'N({d})')
    s = s.replace('*', '-')
    if precedence == Precedence.ADDITION_FIRST:
        s = s.replace('+', '*')
    return eval(s).n

def part_1(expressions) -> int:
    return sum(evaluate(e) for e in expressions)

def part_2(expressions) -> int:
    return sum(evaluate(e, Precedence.ADDITION_FIRST) for e in expressions)

if __name__ == "__main__":
    expressions = get_input()
    print(f'Part 1 answer: {part_1(expressions)}')
    print(f'Part 2 answer: {part_2(expressions)}')
