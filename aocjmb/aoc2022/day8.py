from aocd import data
import re
import numpy as np


def part_a(data):
    data = [ [int(y) for y in re.findall(r'\d', x)] for x in data.strip().split("\n") ]

    count = 2 * (len(data) + len(data[0])) - 4

    for y, row in enumerate(data):
        if y == 0 or y == len(data) - 1:
            continue
        for x, val in enumerate(row):
            if x == 0 or x == len(row) - 1:
                continue
            


    return 0

def part_b(data):
    #data = [ int(x) for x in data.strip().split("\n") ]

    return 


test_data = """\
30373
25512
65332
33549
35390
"""

if __name__ == "__main__":
    assert part_a(test_data) == None
    #assert part_b(test_data) == 
    print(part_a(data))
    #print(part_b(data))
