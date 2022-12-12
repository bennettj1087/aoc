from aocd import data
from itertools import combinations


def part_a(data):
    for i in range(4, len(data)):
        #print(data[i-4:i], set(data[i-4:i]))
        if len(set(data[i-4:i])) == 4:
            #print(i, data[i-4:i])
            return i
    return None

def part_b(data):
    for i in range(14, len(data)):
        #print(data[i-4:i], set(data[i-4:i]))
        if len(set(data[i-14:i])) == 14:
            #print(i, data[i-4:i])
            return i
    return None


test_data = """\
mjqjpqmgbljsphdztnvjfqwrcgsmlb
"""

if __name__ == "__main__":
    assert part_a(test_data) == 7
    assert part_b(test_data) == 19
    print(part_a(data))
    print(part_b(data))
