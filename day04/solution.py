import re

Passport = dict[str, str]

FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
VALIDATORS = {
    'byr': (lambda s: re.match(r'^(\d){4}$', s) and 1920 <= int(s) <= 2002),
    'iyr': (lambda s: re.match(r'^(\d){4}$', s) and 2010 <= int(s) <= 2020),
    'eyr': (lambda s: re.match(r'^(\d){4}$', s) and 2020 <= int(s) <= 2030),
    'hgt': (lambda s: (re.match(r'^\d+cm$', s) and 150 <= int(s[:-2]) <= 193) or \
                        (re.match(r'^\d+in$', s) and 59 <= int(s[:-2]) <= 76)),
    'hcl': (lambda s: bool(re.match(r'^#[\d|a-f]{6}$', s))),
    'ecl': (lambda s: s in 'amb blu brn gry grn hzl oth'.split()),
    'pid': (lambda s: bool(re.match(r'^(\d){9}$', s)))
}

def get_input() -> list[Passport]:
    def passportify(few_lines: str) -> Passport:
        return dict(entry.split(':') for entry in re.split(r'\s', few_lines))

    with open('input.txt', 'r') as f:
        return [
            passportify(hunk) 
            for hunk in re.split('\n\n', ''.join(f.readlines()).strip())
        ]

def is_valid(passport: Passport, validate_fields=True) -> bool:
    if not validate_fields:
        return all(k in passport for k in FIELDS - {'cid'})

    return all(k in passport and VALIDATORS[k](passport[k]) for k in FIELDS - {'cid'})

def part_1(passports) -> int:
    return sum(is_valid(p, validate_fields=False) for p in passports)

def part_2(passports) -> int:
    return sum(is_valid(p) for p in passports)

if __name__ == "__main__":
    passports = get_input()
    print(f'Part 1 answer: {part_1(passports)}')
    print(f'Part 2 answer: {part_2(passports)}')