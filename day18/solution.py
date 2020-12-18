from enum import Enum
from typing import Union
# pylint: disable=unsubscriptable-object
Instructions = list[Union[int, str]]
Expression = str

class Precedence(Enum):
    EQUAL = 'EQUAL'
    ADDITION_FIRST = 'ADDITION_FIRST'

# global precedence
PRECEDENCE = Precedence.EQUAL

class N():
    def __init__(self, n: int=None, instructions: Instructions=None) -> None:
        self.instructions = instructions or [n]
    
    def __add__(self, other: 'N') -> 'N':
        return N(instructions=self.instructions + ['+'] + other.instructions)

    def __mul__(self, other: 'N') -> 'N':
        result = N(instructions=self.instructions + ['*'] + other.instructions)
        if PRECEDENCE == Precedence.EQUAL:
            return result
        elif PRECEDENCE == Precedence.ADDITION_FIRST:
             # in this mode addition is denoted as *, so Python will call this function first.
             # Evaluate greedily.
            return _(result)

    def __str__(self) -> str:
        return str(self.instructions)

def _(n: N) -> N:
    ''' N-evaluation operator '''
    res = n.instructions[0]
    for op, nxt in list(zip(n.instructions[1:], n.instructions[2:]))[::2]:
        addition_op = {Precedence.EQUAL: '+', Precedence.ADDITION_FIRST: '*'}[PRECEDENCE]
        res = res + nxt if op == addition_op else res * nxt
    return N(res)

def get_input() -> list[Expression]:
    with open('input.txt', 'r') as f:
        return [l.strip() for l in f if l]

def evaluate(expression: Expression) -> int:
    s = '_(' + expression.replace('(', '_(') + ')'
    for d in range(10):
        s = s.replace(f'{d}', f'N({d})')
    if PRECEDENCE == Precedence.ADDITION_FIRST: # switcheroo
        s = ''.join({'+': '*', '*': '+'}[ch] if ch in '+*' else ch for ch in s)
    return eval(s).instructions[0]


def part_1(expressions) -> int:
    return sum(evaluate(e) for e in expressions)

def part_2(expressions) -> int:
    global PRECEDENCE
    PRECEDENCE = Precedence.ADDITION_FIRST
    return sum(evaluate(e) for e in expressions)

if __name__ == "__main__":
    expressions = get_input()
    print(f'Part 1 answer: {part_1(expressions)}')
    print(f'Part 2 answer: {part_2(expressions)}')
