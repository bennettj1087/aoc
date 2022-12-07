from aocd import data
from itertools import combinations

def priority(c):
    if c.isupper():
        return ord(c) - 38
    else:
        return ord(c) - 96

def part_a(data):
    data = data.strip().split("\n")
    sum = 0
    for d in data:
        front = [priority(x) for x in d[len(d)//2:]]
        back = [priority(x) for x in d[:len(d)//2]]
        common = set.intersection(set(front), set(back))
        sum += common.pop()
    return sum

def part_b(data):
    data = data.strip().split("\n")
    i = 0
    sum = 0
    while i < len(data):
        sum += priority(set.intersection(set(data[i]), set(data[i+1]), set(data[i+2])).pop())
        i += 3
    return sum


test_data = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

if __name__ == "__main__":
    assert part_a(test_data) == 157
    assert part_b(test_data) == 70
    print(part_a(data))
    print(part_b(data))
