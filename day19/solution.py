import re

Message = str
Expansion = list[tuple[str, ...]]

class Rule():
    def __init__(self, expansion: Expansion=None, pattern: str=None) -> None:
        self.expansion = expansion
        self.pattern = pattern

    def _get_pattern(self, rules: 'dict[Rule]', depth: int=0) -> str:
        if depth > 10:
            return ''
        if self.pattern is None:
            self.pattern = '(' + '|'.join("".join(rules[x]._get_pattern(rules, depth+1) for x in part) for part in self.expansion)+ ')'
        return self.pattern

    def matches(self, s: str, rules: 'dict[Rule]') -> bool:
        return bool(re.match(f'^{self._get_pattern(rules)}$', s))

def get_input() -> (dict[str, Rule], list[Message]):
    with open('input.txt', 'r') as f:
        r, m = ''.join(f.readlines()).strip().split('\n\n')
        rules = {}
        for line in r.split('\n'):
            index, exp = line.split(': ')
            expansion = None if '"' in exp else [x.split() for x in exp.split(' | ')]
            pattern = eval(exp) if '"' in exp else None
            rules[index] = Rule(expansion, pattern)
        return rules, m.split('\n')
    
def part_1(rules, messages) -> int:
    return sum(rules['0'].matches(m, rules) for m in messages)

def part_2(rules, messages) -> int:
    rules['8'].expansion = [('42', ), ('42', '8')]
    rules['11'].expansion = [('42', '31'), ('42', '11', '31')]
    for r in rules.values():
        if not r.expansion is None:
            r.pattern = None # reset
    return sum(rules['0'].matches(m, rules) for m in messages)

if __name__ == "__main__":
    rules, messages = get_input()
    print(f'Part 1 answer: {part_1(rules, messages)}')
    print(f'Part 2 answer: {part_2(rules, messages)}')

