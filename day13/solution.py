from math import prod

def get_input() -> tuple[int, list[str]]:
    with open('input.txt', 'r') as f:
        time = int(f.readline())
        buses = f.readline().strip().split(',')
        return time, buses
    
def part_1(time, buses) -> int:
    departure, bus = next((time + i, b) for i in range(1 + max(buses)) for b in buses if (time + i) % b == 0)
    return (departure - time) * bus

def part_2(buses) -> int:
    def chinese_remainder(M, A):
        ''' Solves a system of congruences using the C.R.T. '''
        res, product = 0, prod(M)
        for m_i, a_i in zip(M, A):
            p = product // m_i
            res += a_i * pow(p, m_i - 2, m_i) * p
        return res % product
        
    # Note that all of the buses are primes
    return chinese_remainder(*zip(*[(int(b), -i) for i, b in enumerate(buses) if b != 'x']))

if __name__ == "__main__":
    time, buses = get_input()
    print(f'Part 1 answer: {part_1(time, [int(b) for b in buses if b != "x"])}')
    print(f'Part 2 answer: {part_2(buses)}')

