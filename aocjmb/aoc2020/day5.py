from aocd import data
from itertools import combinations
import re


def part_a(data):
    data = data.strip().split("\n")
    ids = [ compute_seat_id(bp) for bp in data ]
    return max(ids)

def part_b(data):
    data = data.strip().split("\n")
    ids = [ compute_seat_id(bp) for bp in data ]
    ids.sort()
    for i in range(0, len(ids)-2):
        if ids[i+1] == ids[i] + 2:
            return ids[i] + 1
            break

def compute_seat_id(bp):
    bp = re.sub("B|R", "1", bp)
    bp = re.sub("F|L", "0", bp)
    row = int(bp[:-3], base=2)
    col = int(bp[-3:], base=2)
    return row * 8 + col

test_data = """\
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
"""

if __name__ == "__main__":
    assert part_a(test_data) == 820
    #assert part_b(test_data) == 
    print(part_a(data))
    print(part_b(data))
