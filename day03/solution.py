from math import prod

Map = list[str]

def get_input() -> Map:
    with open('input.txt', 'r') as f:
        return [line.strip() for line in f if line]

def check_slope(area: Map, delta_x: int = 1, delta_y: int = 1) -> int:
    m, n, i, j = len(area), len(area[0]), 0, 0
    trees = 0
    while i < m: 
        trees += area[i][j] == '#'
        i, j = i + delta_x, (j + delta_y) % n
    return trees

def part_1(area) -> int:
    return check_slope(area, delta_y=3)    

def part_2(area) -> int:
    TRAVERSES = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    return prod(check_slope(area, *t) for t in TRAVERSES)

if __name__ == "__main__":
    area = get_input()
    print(f'Part 1 answer: {part_1(area)}')
    print(f'Part 2 answer: {part_2(area)}')