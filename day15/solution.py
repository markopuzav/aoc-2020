
def get_input() -> list[int]:
    return [9,19,1,6,0,5,4]
    
def speak(numbers: int, turns: int) -> int:
    spoken = {n: i for i, n in enumerate(numbers[:-1], 1)}
    last = numbers[-1]
    for t in range(len(numbers) + 1, turns + 1):
        this =  t - 1 - spoken[last] if last in spoken else 0
        spoken[last] = t - 1
        last = this
    return this

def part_1(numbers) -> int:
    return speak(numbers, 2020)

def part_2(numbers) -> int:
    return speak(numbers, 30000000)

if __name__ == "__main__":
    numbers = get_input()
    print(f'Part 1 answer: {part_1(numbers)}')
    print(f'Part 2 answer: {part_2(numbers)}')

