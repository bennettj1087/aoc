import sys

def find_weight(root):
    weight = graph[root][0]
    if len(graph[root][1]) > 0:
        for c in graph[root][1]:
            print(c)
            weight += find_weight(c)
        print("had children")
        input()
        return weight
    else:
        print("didn't have children")
        return weight

sys.setrecursionlimit(2000)

graph = dict()
lines = list()
children = list()
all_children = list()

with open('input.txt') as f:
    for line in f:
        info = line.split()
        name = info[0]
        weight = int(info[1].strip('()'))
        if len(info) > 2:
            children = [x.strip(',') for x in info[3:]]
            all_children += children

        graph[name] = (weight, children)

all_children = set(all_children)

for node in graph.keys():
    if node not in all_children:
        print(node)
        root = node
        break

print(find_weight(root))
