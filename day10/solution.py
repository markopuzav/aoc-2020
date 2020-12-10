from collections import Counter

def get_input() -> list[int]:
    with open('input.txt', 'r') as f:
        return [int(line) for line in f if line]
    
def part_1(jolts) -> int:
    diffs = Counter(y - x for x, y in zip(jolts, jolts[1:]))
    return diffs.get(1, 0) * diffs.get(3, 0)

def part_2(jolts) -> int:
    dp = [1] + [0] * max(jolts)
    for i in jolts[1:]:
        dp[i] = sum(dp[i - m] for m in [1, 2, 3] if i >= m)
    return dp[-1]

if __name__ == "__main__":
    jolts = sorted(get_input())
    jolts = [0] + jolts + [max(jolts) + 3]
    print(f'Part 1 answer: {part_1(jolts)}')
    print(f'Part 2 answer: {part_2(jolts)}')

