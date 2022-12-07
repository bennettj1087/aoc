from aocd import data
from itertools import combinations
import re


def part_a(data):
    c, i = data.split("\n\n")
    c = c.split("\n")
    i = i.split("\n")
    
    crates = list()
    rev = c[:-1].copy()
    rev.reverse()
    print([ int(x) for x in re.findall(r'\d+', c[-1])])
        # for line in rev:
        #     crates.append(line[crate*4-3])
        #     print(crates[crate])


    return 0 

def part_b(data):
    data = [ int(x) for x in data.strip().split("\n") ]

    #return 


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
    assert part_a(test_data) == None
    #assert part_b(test_data) == 
    print(part_a(data))
    #print(part_b(data))
