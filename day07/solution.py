from collections import defaultdict

Color = str
Rules = dict[Color, tuple[Color, int]]

def get_input() -> Rules:
    rules = defaultdict(list)
    with open('input.txt', 'r') as f:
        for line in f:
            color, rest = line.split(' bags contain ')
            for part in rest.split(', '):
                rule = part.split(' bag')
                cnt, val = rule[0].split()[0], ' '.join(rule[0].split()[1:])
                if cnt != 'no':
                    rules[color].append((val, int(cnt)))
    return rules
    
def part_1(rules) -> int:
    reverse_rules = defaultdict(set)
    for clr, vals in rules.items():
        for val, _ in vals:
            reverse_rules[val].add(clr) 

    # BFS for the set of bags that can contain the shiny gold
    goal = reverse_rules['shiny gold']
    while len(nxt := goal | set.union(*[reverse_rules[x] for x in goal])) != len(goal):
        goal = nxt
    return len(goal)
        
def part_2(rules) -> int:
    baggy_bag, result = [(1, 'shiny gold')], 0
    # expand while possible, merging the same colors not necessary
    while nxt := [(cnt * _cnt, _in) for cnt, clr in baggy_bag for _in, _cnt in rules[clr]]:
        result += sum(x[0] for x in nxt)
        baggy_bag = nxt
    return result


if __name__ == "__main__":
    rules = get_input()
    print(f'Part 1 answer: {part_1(rules)}')
    print(f'Part 2 answer: {part_2(rules)}')

