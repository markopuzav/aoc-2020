class CupLinkedList():
    def __init__(self, l: list[int]) -> None:
        self.l, self.n = l, len(l)
        self.curr = 0

        self.index_map = [None] * (self.n + 1)
        for i, x in enumerate(l):
            self.index_map[x] = i
        self.next = [(i + 1) % self.n for i in range(self.n)]
        self.prev = [(i - 1) % self.n for i in range(self.n)]

    def move(self, moves: int=1) -> None:
        for _ in range(moves):
            left = self.next[self.curr]
            right = self.next[self.next[left]]

            # choose pick up and destination 
            pick_up = [self.l[left], self.l[self.next[left]], self.l[right]]
            dest = (self.l[self.curr] - 1) or self.n
            while dest in pick_up:
                dest = (dest - 1) or self.n
            dest_index = self.index_map[dest]

            # re-wire
            self.next[self.curr], self.prev[self.next[right]] = self.next[right], self.curr
            self.next[right], self.prev[self.next[dest_index]] = self.next[dest_index], right
            self.prev[left], self.next[dest_index] = dest_index, left

            # update curr
            self.curr = self.next[self.curr]

    def get_list(self) -> list[int]:
        result, i = [], 0
        for _ in range(self.n):
            result.append(self.l[i])
            i = self.next[i]
        return result
        
def get_input() -> int:
    return list(map(int, '789465123'))
    
def part_1(cups) -> str:
    cups = CupLinkedList(cups)
    cups.move(100)
    l = cups.get_list()
    i1 = l.index(1)
    return ''.join(map(str, l[i1 + 1:] + l[:i1]))

def part_2(cups) -> int:
    cups = CupLinkedList(cups + list(range(len(cups) + 1, 10**6 + 1)))
    cups.move(10**7)
    l = cups.get_list()
    i1 = l.index(1)
    return l[(i1 + 1) % len(l)] * l[(i1 + 2) % len(l)]

if __name__ == "__main__":
    cups = get_input()
    print(f'Part 1 answer: {part_1(cups)}')
    print(f'Part 2 answer: {part_2(cups)}')

