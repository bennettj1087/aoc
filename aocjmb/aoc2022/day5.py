from aocd import data
from itertools import combinations
import re


def part_a(data):
    c, i = data.split("\n\n")
    c = c.split("\n")
    i = i.strip().split("\n")
    
    crates = list()
    rev = c[:-1].copy()
    rev.reverse()
    for x in [ int(x) for x in re.findall(r'\d+', c[-1])]:
        crates.append(list())
    
    for idx, crate in enumerate(crates):
        for line in rev:
            box = line[(idx+1)*4-3]
            if box != ' ': crate.append(box)

    for ins in i:
        ints = [int(x) for x in re.findall(r'\d+', ins)]
        for x in range(ints[0]):
            crates[ints[2]-1].append(crates[ints[1]-1].pop())

    return ''.join(x[-1] for x in crates) 

def part_b(data):
    c, i = data.split("\n\n")
    c = c.split("\n")
    i = i.strip().split("\n")
    
    crates = list()
    rev = c[:-1].copy()
    rev.reverse()
    for x in [ int(x) for x in re.findall(r'\d+', c[-1])]:
        crates.append(list())
    
    for idx, crate in enumerate(crates):
        for line in rev:
            box = line[(idx+1)*4-3]
            if box != ' ': crate.append(box)

    for ins in i:
        ints = [int(x) for x in re.findall(r'\d+', ins)]
        crates[ints[2]-1].extend(crates[ints[1]-1][-ints[0]:])
        del crates[ints[1]-1][-ints[0]:]

    return ''.join(x[-1] for x in crates) 


test_data = """\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

if __name__ == "__main__":
    assert part_a(test_data) == 'CMZ'
    assert part_b(test_data) == 'MCD'
    print(part_a(data))
    print(part_b(data))
