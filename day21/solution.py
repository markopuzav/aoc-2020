import re
Food = tuple[str, ...]


def get_input() -> dict[Food, list[str]]:
    with open('input.txt', 'r') as f:
        return {
            tuple(d['ings'].split()): d['alers'].split(', ') for l in f if (d := re.match(r'(?P<ings>.+)\(contains (?P<alers>.+)\)', l).groupdict())
        }
    
def get_alergen_ingredients(foods: dict[Food, list[str]]) -> dict[str, str]:
    candidates = {}
    for food, alergens in foods.items():
        for a in alergens:
            candidates[a] = set(food) & candidates[a] if a in candidates else set(food)

    for _ in range(len(candidates)):
        resolved = set.union(*[v for v in candidates.values() if len(v) == 1])
        for a in candidates:
            if len(candidates[a]) > 1:
                candidates[a] -= resolved
    
    return {k: v.pop() for k, v in candidates.items()}

def part_1(foods) -> int:
    alergen_ingredients = get_alergen_ingredients(foods)
    return sum(i not in alergen_ingredients.values() for f in foods for i in f)

def part_2(alergens) -> int:
    alergen_ingredients = get_alergen_ingredients(foods)
    return ','.join(map(lambda x: str(x[1]), sorted(alergen_ingredients.items())))

if __name__ == "__main__":
    foods = get_input()
    print(f'Part 1 answer: {part_1(foods)}')
    print(f'Part 2 answer: {part_2(foods)}')

