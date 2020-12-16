from itertools import chain
from math import prod
import re

Range = tuple[int, int]
Rules = dict[str, list[Range]]
Ticket = list[int]

def get_input() -> (Rules, Ticket, list[Ticket]):
    with open('input.txt', 'r') as f:
        d = re.match(r'(?P<rules>.+)\n\nyour ticket:\n(?P<your>.+)\n\nnearby tickets:\n(?P<nearby>.+)\n', f.read(), re.DOTALL).groupdict()
        rules = {sr[0]: [int(x) for x in re.findall(r'(\d+)', sr[1])] for r in d['rules'].split('\n') if (sr := r.split(': '))}
        for k, v in rules.items():
            rules[k] = [(x, y) for i, (x, y) in enumerate(zip(v, v[1:])) if not i&1]
        your = [int(x) for x in d['your'].split(',')]
        nearby = [[int(x) for x in l.split(',')] for l in d['nearby'].split('\n') if l]
        return rules, your, nearby

def is_valid_number(n: int, rules: Rules) -> bool:
    return any(l <= n <= r for l, r in chain(*rules.values()))

def is_valid(ticket: Ticket, rules: Rules) -> bool:
    return all(is_valid_number(x, rules) for x in ticket)

def ticket_scanning_error_rate(ticket: Ticket, rules: Rules) -> int:
    return sum(x for x in ticket if not is_valid_number(x, rules))

def part_1(nearby, rules) -> int:
    return sum(ticket_scanning_error_rate(t, rules) for t in nearby)

def part_2(rules, your, nearby) -> int:
    def find_possible_categories(pos: int, valids: list[Ticket]) -> set[str]:
        return {k for k, v in rules.items() if all(is_valid_number(t[pos], {k: v}) for t in valids)}

    valid_tickets = [t for t in nearby if is_valid(t, rules)]
    possible_categories = [find_possible_categories(i, valid_tickets) for i in range(len(your))]

    # reduce to a unique solution
    determined = set.union(*[c for c in possible_categories if len(c) == 1])
    for _ in range(len(your)):
        possible_categories = [c - determined if len(c) > 1 else c for c in possible_categories]
        determined = set.union(*[c for c in possible_categories if len(c) == 1])
    
    category_pos = {c.pop(): i for i, c in enumerate(possible_categories)}
    return prod(your[category_pos[name]] for name in category_pos if name.startswith('departure'))


if __name__ == "__main__":
    rules, your, nearby = get_input()
    print(f'Part 1 answer: {part_1(nearby, rules)}')
    print(f'Part 2 answer: {part_2(rules, your, nearby)}')


