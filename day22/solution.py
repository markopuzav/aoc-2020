Hand = list[int]

def get_input() -> tuple[Hand, Hand]:
    with open('input.txt', 'r') as f:
        h1, h2 = ''.join(f.readlines()).strip().split('\n\n')
        return list(map(int, h1.split('\n')[1:])), list(map(int, h2.split('\n')[1:]))

def play(hand1: Hand, hand2: Hand) -> Hand:
    while hand1 and hand2:
        t1, t2 = hand1[0], hand2[0]
        del hand1[0]; del hand2[0]
        (hand1 if t1 > t2 else hand2).extend([max(t1, t2), min(t1, t2)])
    return hand1 or hand2

def recursive_combat(hand1: Hand, hand2: Hand) -> Hand:
    def play_game(h1: Hand, h2: Hand, seen: set[tuple[tuple[int], tuple[int]]]) -> tuple[int, Hand]:
        while h1 and h2:
            tuple_key = (tuple(h1), tuple(h2))
            if tuple_key in seen:
                return 1, []
            seen.add(tuple_key)

            t1, t2 = h1[0], h2[0]
            del h1[0]; del h2[0]
            if len(h1) >= t1 and len(h2) >= t2:
                winner, _ = play_game(h1[:t1], h2[:t2], set())
            else:
                winner = 1 if t1 > t2 else 2
        
            if winner == 1:
                h1.extend([t1, t2])
            else:
                h2.extend([t2, t1])
        
        return (1, h1) if h1 else (2, h2)

    return play_game(hand1, hand2, set())[1]

def score(hand: Hand) -> int:
    return sum(i * x for i, x in enumerate(hand[::-1], 1))

def part_1(hand1, hand2) -> int:
    return score(play(hand1, hand2))

def part_2(hand1, hand2) -> int:
    return score(recursive_combat(hand1,hand2))

if __name__ == "__main__":
    hand1, hand2 = get_input()
    print(f'Part 1 answer: {part_1(list(hand1), list(hand2))}')
    print(f'Part 2 answer: {part_2(list(hand1), list(hand2))}')

