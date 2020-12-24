class HexagonalPos():
    def __init__(self, pos: tuple[int, int]=(0, 0)) -> None:
        self.pos = pos

    def move(self, dir: str) -> None:
        self.pos = {
            'e': (lambda x, y: (x + 1, y)),
            'w': (lambda x, y: (x - 1, y)),
            'se': (lambda x, y: (x + (y % 2 == 0), y + 1)),
            'sw': (lambda x, y: (x - (y % 2 == 1), y + 1)),
            'ne': (lambda x, y: (x + (y % 2 == 0), y - 1)),
            'nw': (lambda x, y: (x - (y % 2 == 1), y - 1)),
        }[dir](*self.pos)

    def neighbours(self) -> 'set[HexagonalPos]':
        neighs = set()
        for dir in ('e', 'w', 'se', 'sw', 'ne', 'nw'):
            ne = HexagonalPos(self.pos)
            ne.move(dir)
            neighs.add(ne)
        return neighs

    def __hash__(self):
        return self.pos.__hash__()

    def __eq__(self, other):
        return self.pos == other.pos


def get_input() -> list[str]:
    with open('input.txt', 'r') as f:
        return [line.strip() for line in f if line]

def find_black_tiles(instructions) -> set[HexagonalPos]:
    black_tiles = set()
    for inst in instructions:
        pos = HexagonalPos()
        i = 0
        while i < len(inst):
            if i + 1 < len(inst) and inst[i:i+2] in ('se', 'sw', 'ne', 'nw'):
                pos.move(inst[i:i+2])
                i += 2
            else:
                pos.move(inst[i])
                i += 1
        if pos in black_tiles:
            black_tiles.remove(pos)
        else:
            black_tiles.add(pos)
    return black_tiles

def part_1(instructions) -> int:
    return len(find_black_tiles(instructions))
        

def part_2(instructions, days=100) -> int:
    black_tiles = find_black_tiles(instructions)
    for _ in range(days):
        next_black_tiles, visited = set(), set()
        for t in black_tiles:
            if len(t.neighbours() & black_tiles) in [1, 2]:
                next_black_tiles.add(t)
            for ne in (t.neighbours() - visited):
                visited.add(ne)
                if len(ne.neighbours() & black_tiles) == 2:
                    next_black_tiles.add(ne)
        black_tiles = next_black_tiles
    return len(black_tiles)

if __name__ == "__main__":
    instructions = get_input()
    print(f'Part 1 answer: {part_1(instructions)}')
    print(f'Part 2 answer: {part_2(instructions)}')


