from aocd import data
from itertools import combinations


def part_a(data):
    data = [ set(x.replace("\n", "")) for x in data.strip().split("\n\n") ]
    return sum([len(x) for x in data])

def part_b(data):
    data = [ x.split("\n") for x in data.strip().split("\n\n") ]
    answers = list()
    for group in data:
        s = set.intersection(*map(set, group))
        answers.append(len(s))

    return sum(answers)


test_data = """\
abc

a
b
c

ab
ac

a
a
a
a

b
"""

if __name__ == "__main__":
    assert part_a(test_data) == 11
    assert part_b(test_data) == 6
    print(part_a(data))
    print(part_b(data))
