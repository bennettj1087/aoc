from aocd import data
from itertools import combinations
import re


def part_a(data):
    bags = parse_data(data)
    for bag_color in bags:
        if find_gold(bag_color, bags):
            base_bags.add(bag_color)

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

def find_gold(bag_color, bags):
    print("find_gold with:", bag_color, bags[bag_color])
    if len(bags[bag_color]) == 0:
        print("  base bag color, returning false")
        return False
    
    if "shiny gold" in bags[bag_color].keys():
        print("  shiny gold in bag, adding and returning true")
        base_bags.add(bag_color)
        return True

    gold = False
    print("  delving into sub bags...")
    for color in bags[bag_color].keys():
        gold = gold or find_gold(color, bags)

    if gold:
        print("  found shiny gold below, adding to base_bags")
        base_bags.add(bag_color)
    return gold

def parse_data(data):
    data = [ x for x in data.strip().split("\n") ]
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
