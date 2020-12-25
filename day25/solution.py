
def get_input() -> list[int]:
    with open('input.txt', 'r') as f:
        return [int(l) for l in f if l]
    
def get_loop_size(key: int, init_val: int=1, subject_num: int=7, M: int=20201227) -> int:
    loop_size, val = 0, init_val
    while val != key:
        loop_size += 1
        val = val * subject_num % M
    return loop_size

def get_key(loop_size: int, init_val: int=1, subject_num: int=7, M: int=20201227) -> int:
    key = init_val
    for _ in range(loop_size):
        key = key * subject_num % M
    return key

def part_1(door_pk, card_pk) -> int:
    return get_key(loop_size=get_loop_size(card_pk), subject_num=door_pk)

def part_2() -> int:
    return '🎄🎄🎄'

if __name__ == "__main__":
    door_pk, card_pk = get_input()
    print(f'Part 1 answer: {part_1(door_pk, card_pk)}')
    print(f'Part 2 answer: {part_2()}')
