from itertools import accumulate

def get_input() -> list[int]:
    with open('input.txt', 'r') as f:
        return [int(line) for line in f if line]


def part_1(xmas, preamble=25) -> int:
    def check(pos, ns):
        return any(ns[pos-1-i] + ns[pos-1-j] == ns[pos] for i in range(preamble) for j in range(i + 1, preamble))
    return next(xmas[i] for i in range(preamble, len(xmas)) if not check(i, xmas))

def part_2(xmas, weakness) -> int:
    def find_break(pos, ns):
        cumsum = list(accumulate(xmas[pos:]))
        return cumsum.index(weakness) if weakness in cumsum else None
    
    for i in range(len(xmas)):
        b = find_break(i, xmas)
        if b is not None:
            return min(xmas[i:i+b]) + max(xmas[i:i+b])

if __name__ == "__main__":
    xmas = get_input()
    weakness = part_1(xmas)
    print(f'Part 1 answer: {weakness}')
    print(f'Part 2 answer: {part_2(xmas, weakness)}')

