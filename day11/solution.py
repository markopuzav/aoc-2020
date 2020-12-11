Map = list[list[str]]

NEIGHBOUR_VECTORS = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if not x == y == 0]

def get_input() -> Map:
    with open('input.txt', 'r') as f:
        return [line.strip() for line in f if line]
    
def neighbours(i: int, j: int, layout: Map, long_distance: bool) -> list[str]:
    def is_inside(x, y):
        return layout and 0 <= x < len(layout) and 0 <= y < len(layout[0])

    if not long_distance:
        return [layout[i + x][j + y] for x, y in NEIGHBOUR_VECTORS if is_inside(i + x, j + y)]

    in_view = []
    for x, y in NEIGHBOUR_VECTORS:
        k = 1
        while is_inside(i + k*x, j + k*y):
            if (seat := layout[i + k*x][j + k*y]) != '.': # not a floor
                in_view.append(seat)
                break
            k += 1
    return in_view

def evolve(layout: Map, long_distance:bool=False) -> Map:
    def rules(i: int, j: int) -> str:
        if layout[i][j] == 'L' and neighbours(i, j, layout, long_distance).count('#') == 0:
            return '#'
        if layout[i][j] == '#' and neighbours(i, j, layout, long_distance).count('#') > (4 if long_distance else 3):
            return 'L'
        return layout[i][j]

    return [''.join(rules(i, j) for j in range(len(layout[0]))) for i in range(len(layout))]

def part_1(layout) -> int:
    last = None
    while (joined_layout := ''.join(layout)) != last:
        layout = evolve(layout)
        last = joined_layout
    return joined_layout.count('#')


def part_2(layout) -> int:
    last = None
    while (joined_layout := ''.join(layout)) != last:
        layout = evolve(layout, long_distance=True)
        last = joined_layout
    return joined_layout.count('#')


if __name__ == "__main__":
    layout = get_input()
    print(f'Part 1 answer: {part_1(layout)}')
    print(f'Part 2 answer: {part_2(layout)}')

