from aocd import data
from itertools import combinations


def part_a(data):
    data = data.strip().split("\n")
    valid = 0
    for line in data:
        tokens = line.split(" ")
        limits = [ int(x) for x in tokens[0].split("-") ]
        char = tokens[1][0]
        password = list(tokens[2])
        if password.count(char) >= limits[0] and password.count(char) <= limits[1]:
            valid = valid + 1
    return valid

def part_b(data):
    data = data.strip().split("\n")
    valid = 0
    for line in data:
        tokens = line.split(" ")
        positions = [ int(x) for x in tokens[0].split("-") ]
        char = tokens[1][0]
        password = list(tokens[2])
        if (password[positions[0]-1] == char) ^ (password[positions[1]-1] == char):
            valid = valid + 1
    return valid


test_data = """\
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""

if __name__ == "__main__":
    assert part_a(test_data) == 2
    assert part_b(test_data) == 1
    print(part_a(data))
    print(part_b(data))
