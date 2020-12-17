from itertools import product
from typing import Union

Coor = Union[tuple[int, int, int], tuple[int, int, int, int]]
CubeMap = set[Coor]

def get_input() -> CubeMap:
    with open('input.txt', 'r') as f:
        return {(i, j, 0) for i, l in enumerate(f.readlines()) for j, ch in enumerate(l) if l and ch == '#'}

def neigh(c: Coor, space: int) -> set[Coor]:
    def coor_sum(a, b):
        return tuple(x + y for x, y in zip(a, b))
    return {coor_sum(c, nv) for nv in product([-1, 0, 1], repeat=space) if not all(x == 0 for x in nv)}

def evolve(active: CubeMap, space: int=3) -> CubeMap:
    next_active, visited = set(), set()
    for c in active:
        for x in neigh(c, space) - visited:
            if x in active and len(neigh(x, space) & active) in [2, 3]:
                next_active.add(x)
            elif not x in active and len(neigh(x, space) & active) == 3:
                next_active.add(x)
            visited.add(x)
    return next_active

def part_1(initial) -> int:
    active = initial
    for _ in range(6):
        active = evolve(active)
    return len(active)

def part_2(initial) -> int:
    active = {(*c, 0) for c in initial} # convert to 4d
    for _ in range(6):
        active = evolve(active, space=4)
    return len(active)

if __name__ == "__main__":
    initial = get_input()
    print(f'Part 1 answer: {part_1(initial)}')
    print(f'Part 2 answer: {part_2(initial)}')


