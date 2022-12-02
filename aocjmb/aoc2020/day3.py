from aocd import data
from itertools import combinations


def part_a(data):
    data = data.strip().split("\n")
    return check_slope(data, 3, 1)

def part_b(data):
    data = data.strip().split("\n")
    return check_slope(data, 1, 1) * check_slope(data, 3, 1) * check_slope(data, 5, 1) * check_slope(data, 7, 1) * check_slope(data, 1, 2)

def check_slope(data, dx, dy):
    trees = 0
    width = len(data[0])
    (x, y) = (0, 0)
    while y < len(data)-1:
        x = (x + dx) % width
        y = y + dy
        if data[y][x] == '#':
            trees = trees + 1        
    return trees


test_data = """\
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""

if __name__ == "__main__":
    assert part_a(test_data) == 7
    assert part_b(test_data) == 336
    print(part_a(data))
    print(part_b(data))
