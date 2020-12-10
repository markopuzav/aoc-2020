from itertools import product

def get_input() -> list[int]:
    with open('input.txt', 'r') as f:
        return [int(line) for line in f]

def part_1(numbers: list[int]) -> int:
    return next(x * y for x in numbers for y in numbers if x + y == 2020)

def part_2(numbers: list[int]) -> int:
    return next(x * y * z for x, y, z in product(numbers, repeat=3) if x + y + z == 2020)

if __name__ == "__main__":
    numbers = get_input()
    print(f'Part 1 answer: {part_1(numbers)}')
    print(f'Part 2 answer: {part_2(numbers)}')