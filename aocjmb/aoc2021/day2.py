from aocd import data
from itertools import combinations


def part_a(data):
    data = [ x.split(" ") for x in data.strip().split("\n") ]
    h = 0
    d = 0
    for i in data:
        if i[0] == "forward":
            h += int(i[1])
        elif i[0] == "up":
            d -= int(i[1])
        else:
            d += int(i[1])
    return h*d

def part_b(data):
    data = [ x.split(" ") for x in data.strip().split("\n") ]
    h = 0
    d = 0
    aim = 0
    for i in data:
        if i[0] == "forward":
            h += int(i[1])
            d += int(i[1]) * aim
        elif i[0] == "up":
            aim -= int(i[1])
        else:
            aim += int(i[1])
    return h*d


test_data = """\
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""

if __name__ == "__main__":
    assert part_a(test_data) == 150
    assert part_b(test_data) == 900
    print(part_a(data))
    print(part_b(data))
