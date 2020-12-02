from aocd import data
from itertools import combinations


def part_a(data):
    data = [ int(x) for x in data.strip().split("\n") ]
    c = list(combinations(data, 2))
    sums = [ a + b for (a, b) in c ]
    (x, y) = c[sums.index(2020)]
    return x * y


def part_b(data):
    data = [ int(x) for x in data.strip().split("\n") ]
    c = list(combinations(data, 3))
    sums = [ a + b + d for (a, b, d) in c ]
    (x, y, z) = c[sums.index(2020)]
    return x * y * z


test_data = """\
1721
979
366
299
675
1456
"""

if __name__ == "__main__":
    assert part_a(test_data) == 514579
    assert part_b(test_data) == 241861950
    print(part_a(data))
    print(part_b(data))
