import re

Rule = tuple[str, int, int]
Password = str

def get_input() -> tuple[list[Rule], list[Password]]:
    rules, passwords = [], []
    with open('input.txt', 'r') as f:
        for line in f:
            d = re.match(r'(?P<min>\d+)-(?P<max>\d+) (?P<letter>\w): (?P<password>\w+)', line).groupdict()
            rules.append( ( d['letter'], int(d['min']), int(d['max']) ) )
            passwords.append(d['password'])
    return rules, passwords

def is_valid(rule: Rule, password: Password, oldschool=False) -> bool:
    letter, mn, mx = rule
    if oldschool:
        return mn <= password.count(letter) <= mx
    return (password[mn - 1] + password[mx - 1]).count(letter) == 1

def part_1(rules, passwords) -> int:
    return sum(is_valid(rule, password, True) for rule, password in zip(rules, passwords))

def part_2(rules, passwords) -> int:
    return sum(is_valid(rule, password) for rule, password in zip(rules, passwords))

if __name__ == "__main__":
    rules, passwords = get_input()
    print(f'Part 1 answer: {part_1(rules, passwords)}')
    print(f'Part 2 answer: {part_2(rules, passwords)}')