from aocd import data
from itertools import combinations
import re


def part_a(data):
    bags = parse_data(data)
    current_run_bags = set()
    for bag_color, bag_contents in bags.items():
        print("part_a:", bag_color, bag_contents)
        current_run_bags = { bag_color }
        base_bags.add(find_gold(bags, bag_color, current_run_bags))

    print(base_bags)
    return len(base_bags)

def part_b(data):
    data = [ int(x) for x in data.strip().split("\n") ]

    #return 


test_data = """\
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

def find_gold(bags, bag_color, current_run_bags):
    if len(bags[bag_color]) == 0:
        print("find_gold return 0")
        return
    else:
        sub_total = 0
        print("find_gold:", bags[bag_color])
        if "shiny gold" in bags[bag_color].keys():
            base_bags.update(current_run_bags)
        for k,v in bags[bag_color].items():
            print("find_gold looping on:", k, v)
            if k in base_bags:
                return
            current_run_bags.add(k)
            find_gold(bags, k, current_run_bags)

def parse_data(data):
    data = [ x for x in test_data.strip().split("\n") ]
    bags = dict()
    for x in data:
        bag_color = x.split("bags")[0]
        bag_contents = re.findall("(\d+) (.*?) bags*[,.]", x)
        #print(bag_color, bag_contents)
        bags[bag_color.strip()] = { c[1]:c[0] for c in bag_contents }
    #print(bags)
    return bags

base_bags = set()

if __name__ == "__main__":
    assert part_a(test_data) == 4
    #assert part_b(test_data) == 
    print(part_a(data))
    #print(part_b(data))
