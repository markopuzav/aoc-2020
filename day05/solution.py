Seat = str

def get_input() -> list[Seat]:
    with open('input.txt', 'r') as f:
        return [line.strip() for line in f if line]

def seat_id(seat: Seat) -> int:
    return sum(1 << i for i, x in enumerate(seat[::-1]) if x in 'BR')

def part_1(seats) -> int:
    return max(map(seat_id, seats))

def part_2(passports) -> int:
    taken = set(map(seat_id, seats))
    for id in taken:
        if (your_seat := id + 1) not in taken and (id + 2) in taken:
            return your_seat

if __name__ == "__main__":
    seats = get_input()
    print(f'Part 1 answer: {part_1(seats)}')
    print(f'Part 2 answer: {part_2(seats)}')

