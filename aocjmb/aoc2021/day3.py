from aocd import data
from itertools import combinations
from collections import Counter


def part_a(data):
    data = data.strip().split("\n")
    t = [list(x) for x in list(zip(*data))]
    gamma = int(''.join([Counter(x).most_common()[0][0] for x in t]), 2)
    eps = int(''.join([Counter(x).most_common()[-1][0] for x in t]), 2)
    return gamma*eps

def part_b(data):
    data = data.strip().split("\n")
    oxy = data.copy()
    co2 = data.copy()
    i = 0 
    t = [list(x) for x in list(zip(*data))]
    gamma_l = ''.join([Counter(x).most_common()[0][0] for x in t])
    eps_l = ''.join([Counter(x).most_common()[-1][0] for x in t])
    for c in range(len(gamma_l)):
        for d in oxy:
            if d[c] != gamma_l[c]:
                oxy.remove(d)
        for d in co2:
            if d[c] == gamma_l[c]:
                co2.remove(d)

    print(oxy, co2)

        
    #return 


test_data = """\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""

if __name__ == "__main__":
    assert part_a(test_data) == 198
    assert part_b(test_data) == 230
    print(part_a(data))
    print(part_b(data))
