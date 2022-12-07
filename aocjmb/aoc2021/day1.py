from aocd import data
from itertools import combinations

def part_a(data):
    data = [ int(x) for x in data.strip().split("\n") ]
    count = 0
    for index,value in enumerate(data):
        if index == 0: continue
        if value > data[index-1]:
            count += 1

    return count


def part_b(data):
    data = [ int(x) for x in data.strip().split("\n") ]
    count = 0
    i = 1
    while i < len(data)-2:
        if sum(data[i:i+3]) > sum(data[i-1:i+2]):
            count += 1
        i += 1

    return count


test_data = """\
199
200
208
210
200
207
240
269
260
263
"""

if __name__ == "__main__":
    assert part_a(test_data) == 7
    assert part_b(test_data) == 5
    print(part_a(data))
    print(part_b(data))
