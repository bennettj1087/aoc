from aocd import data
from itertools import combinations

def calc_sums(data):
    elves = [x.split("\n") for x in data.strip().split("\n\n")]
    for x in range(len(elves)):
        elves[x] = [int(y) for y  in elves[x]]
    sums = [sum(x) for x in elves]
    return sums

def part_a(data):
    return max(calc_sums(data))


def part_b(data):
    return sum(sorted(calc_sums(data))[-3:])


test_data = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

if __name__ == "__main__":
    assert part_a(test_data) == 24000
    assert part_b(test_data) == 45000
    print(part_a(data))
    print(part_b(data))
