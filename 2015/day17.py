from itertools import combinations

containers = list()
total = list()

f = open('input.txt')
for line in f:
    containers.append(int(line[:-1]))

c = [combinations(containers, r) for r in range(len(containers))]

for x in range(len(c)):
    for option in c[x]:
        if sum(option) == 150:
            total.append(len(option))

print(total.count(4))

