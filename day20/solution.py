from collections import defaultdict
from copy import deepcopy
import re
Coor = tuple[int, int]
Tile = list[str]
Picture = list[list[tuple[Tile, int]]]

SEA_MONSTER = [
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   '
    ]

def get_input() -> dict[int, Tile]:
    with open('input.txt', 'r') as f:
        tiles = {}
        for chunk in ''.join(f.readlines()).strip().split('\n\n'):
            d = re.match(r'Tile (?P<id>\d+):\n(?P<rows>.+)', chunk, re.DOTALL).groupdict()
            tiles[int(d['id'])] = d['rows'].split('\n')
        return tiles

def get_transform(tile: Tile, transform: int) -> Tile:
    N = len(tile)
    coor_map = {
        0: (lambda x, y: (x, y)),
        1: (lambda x, y: (N - 1 - x, y)),
        2: (lambda x, y: (x, N - 1 - y)),
        3: (lambda x, y: (N - 1 - x, N - 1 - y)),
        4: (lambda x, y: (y, x)),
        5: (lambda x, y: (N - 1 - y, x)),
        6: (lambda x, y: (y, N - 1 - x)),
        7: (lambda x, y: (N - 1 - y, N - 1 - x)),
    }
    return [''.join(tile[coor_map[transform](x, y)[0]][coor_map[transform](x, y)[1]] for y in range(N)) for x in range(N)]


SIDE_CACHE = {}
def get_side(tiles: dict[int, Tile], side: str, tile_ind: Tile, transform: int) -> str:
    cache_key = (side, tile_ind, transform)
    if cache_key in SIDE_CACHE:
        return SIDE_CACHE[cache_key]

    transformed = get_transform(tiles[tile_ind], transform)
    result = {
        'left': (lambda t: ''.join(r[0] for r in t)),
        'right': (lambda t: ''.join(r[-1] for r in t)),
        'top': (lambda t: ''.join(t[0])), 
        'bottom': (lambda t: ''.join(t[-1]))
    }[side](transformed)
    SIDE_CACHE[cache_key] = result
    return result


def rec_fill_in(
        tiles: dict[int, Tile], 
        available: set[int], 
        pic_so_far: Picture, 
        N: int, 
        pos: Coor=(0,0)) -> Picture:

    x, y = pos
    if x == N:
        return pic_so_far

    for c in available:
        for transform in range(8): # symmetry group of square
            if y > 0 and get_side(tiles, 'right', *pic_so_far[x][y - 1]) != get_side(tiles, 'left', c, transform):
                continue
            if x > 0 and get_side(tiles, 'bottom', *pic_so_far[x - 1][y]) != get_side(tiles, 'top', c, transform):
                continue

            new_pic_so_far = deepcopy(pic_so_far)
            new_pic_so_far[x][y] = (c, transform)
            c_res = rec_fill_in(tiles, available - {c}, new_pic_so_far, N, (x, y + 1) if y < N - 1 else (x + 1, 0))
            if c_res is not None:
                return c_res
    return None

def sea_monster_squares(tile: Tile) -> set[Coor]:
    SX, SY = len(SEA_MONSTER), len(SEA_MONSTER[0])
    result = set()
    for x in range(len(tile) - SX):
        for y in range(len(tile[0]) - SY):
            if all(SEA_MONSTER[i][j] == ' ' or tile[x + i][y + j] == '#' for i in range(SX) for j in range(SY)):
                result |= {(x + i, y + j) for i in range(SX) for j in range(SY) if SEA_MONSTER[i][j] == '#'}
    return result

###############################################################################################


def part_1(tiles) -> int:
    N = int(len(tiles) ** 0.5) # picture size
    picture = rec_fill_in(tiles, set(tiles.keys()), [[None]*N for _ in range(N)], N)
    return picture[0][0][0] * picture[0][-1][0] * picture[-1][0][0] * picture[-1][-1][0]


def part_2(tiles) -> int:
    N = int(len(tiles) ** 0.5) # picture size
    picture = rec_fill_in(tiles, set(tiles.keys()), [[None]*N for _ in range(N)], N)
    
    # 🤮🤮🤮
    actual_image = [
        ''.join(get_transform(tiles[x[0]], x[1])[i][1:-1] for x in row) 
        for row in picture for i in range(1, len(tiles[row[0][0]]) -1)
    ]
    for transform in range(8):
        if sms := sea_monster_squares(get_transform(actual_image, transform)):
            return sum(r.count('#') for r in actual_image) - len(sms)
    
if __name__ == "__main__":
    tiles = get_input()
    print(f'Part 1 answer: {part_1(tiles)}')
    print(f'Part 2 answer: {part_2(tiles)}')

