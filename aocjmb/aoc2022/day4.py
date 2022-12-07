from aocd import data
from itertools import combinations


def part_a(data):
    data = [ x.split(',') for x in data.strip().split("\n") ]
    count = 0

    for d in data:
        a = [ int(x) for x in d[0].split('-') ]
        b = [ int(x) for x in d[1].split('-') ]
        if (a[0] <= b[0] and a[1] >= b[1]) or (b[0] <= a[0] and b[1] >= a[1]):
            count += 1

    return count

def part_b(data):
    data = [ x.split(',') for x in data.strip().split("\n") ]
    count = 0

    for d in data:
        a = [ int(x) for x in d[0].split('-') ]
        b = [ int(x) for x in d[1].split('-') ]
        if (a[1] >= b[0] and a[0] <= b[1]):
            # print("first overlap", a, b)
            count += 1
        elif (b[1] >= a[0] and a[1] >= b[0]):
            # print("second overlap", a, b)
            count += 1
        # else:
        #     print("not    ", a, b)

    return count


test_data = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

if __name__ == "__main__":
    assert part_a(test_data) == 2
    assert part_b(test_data) == 4
    print(part_a(data))
    print(part_b(data))
