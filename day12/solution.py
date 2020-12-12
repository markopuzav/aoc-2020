from functools import partial

Pos = (int, int)
Orientation = int

class Ship():
    def __init__(self, pos:Pos=(0, 0), o: Orientation=0):
        self.pos = pos
        self.o = o
        self.waypoint = (10, 1)
    
    def _update_ship(self, x: int=0, y: int=0, rot: int=0, neg=False) -> None:
        if neg:
            x, y, rot = -x, -y, -rot
        self.pos = (self.pos[0] + x, self.pos[1] + y)
        self.o = (self.o + rot) % 360

    def _update_waypoint(self, x: int=0, y: int=0, rot: int=0, neg=False) -> None:
        if neg:
            x, y, rot = -x, -y, (-rot) % 360
        self.waypoint = (self.waypoint[0] + x, self.waypoint[1] + y)
        if rot == 90:
            self.waypoint = (-self.waypoint[1], self.waypoint[0])
        elif rot == 180:
            self.waypoint = (-self.waypoint[0], -self.waypoint[1])
        elif rot == 270:
            self.waypoint = (self.waypoint[1], -self.waypoint[0])

    def _forward(self, by: int, use_waypoint: bool=False) -> None:
        if use_waypoint:
            self.pos = (self.pos[0] + by * self.waypoint[0], self.pos[1] + by * self.waypoint[1])
        else:
            self.apply_action({0: 'E', 90: 'N', 180: 'W', 270: 'S'}[self.o], by)

    def apply_action(self, action: str, by: int, use_waypoint: bool=False) -> None:
        update_function = self._update_waypoint if use_waypoint else self._update_ship
        {
            'N': partial(update_function, 0),
            'S': partial(update_function, 0, neg=True),
            'E': partial(update_function),
            'W': partial(update_function, neg=True),
            'L': partial(update_function, 0, 0),
            'R': partial(update_function, 0, 0, neg=True),
            'F': partial(self._forward, use_waypoint=use_waypoint)
        }[action](by)

    def __str__(self):
        return f'🚢{self.pos},{self.o}'



def get_input() -> list[list[str]]:
    with open('input.txt', 'r') as f:
        return [line.strip() for line in f if line]
    
def part_1(instructions) -> int:
    ship = Ship()
    for i in instructions:
        ship.apply_action(i[0], int(i[1:]))
    return abs(ship.pos[0]) + abs(ship.pos[1])
    
def part_2(answers) -> int:
    ship = Ship()
    for i in instructions:
        ship.apply_action(i[0], int(i[1:]), use_waypoint=True)
    return abs(ship.pos[0]) + abs(ship.pos[1])

if __name__ == "__main__":
    instructions = get_input()
    print(f'Part 1 answer: {part_1(instructions)}')
    print(f'Part 2 answer: {part_2(instructions)}')
