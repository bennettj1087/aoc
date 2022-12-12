from aocd import data
from anytree import Node, RenderTree

def traverse(cur_dir, dirs, data):
    while True and len(data) > 0:
        line = data.pop(0)
        if line.startswith("$ cd .."):
            return
        if line.startswith("$ cd "):
            traverse(cur_dir + "/" + line[5:], dirs, data)
            dirs[cur_dir] += dirs[cur_dir + "/" + line[5:]]
        elif line.startswith("dir"):
            dirs[cur_dir + "/" + line[4:]] = 0
        elif line.startswith("$ ls"):
            continue
        else:
            dirs[cur_dir] += int(line.split(' ')[0])


def part_a(data):
    data = data.strip().split("\n")
    data.pop(0)
    dirs = {"/": 0}
    traverse("/", dirs, data)

    return sum([x for x in dirs.values() if x <= 100000])

def part_b(data):
    data = data.strip().split("\n")
    data.pop(0)
    dirs = {"/": 0}
    traverse("/", dirs, data)

    needed_space = 30000000 - (70000000 - dirs["/"])

    return min([x for x in dirs.values() if x >= needed_space])


test_data = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

if __name__ == "__main__":
    assert part_a(test_data) == 95437
    assert part_b(test_data) == 24933642
    print(part_a(data))
    print(part_b(data))
