
def get_input() -> list[list[str]]:
    with open('input.txt', 'r') as f:
        return [g.split('\n') for g in ''.join(f.readlines()).split('\n\n')]
    
def part_1(answers) -> int:
    return sum(len(set(''.join(g))) for g in answers)

def part_2(answers) -> int:
    return sum(len(set.intersection(*map(set, g))) for g in answers)

if __name__ == "__main__":
    answers = get_input()
    print(f'Part 1 answer: {part_1(answers)}')
    print(f'Part 2 answer: {part_2(answers)}')

