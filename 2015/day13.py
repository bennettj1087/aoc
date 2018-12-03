from itertools import permutations

f = open("input.txt")
relationships = dict()
names = list()
h = list()

for line in f.readlines():
    words = line.split(' ')
    if words[2] == 'gain':
        num = words[3]
    else:
        num = '-' + words[3]
    relationships.update({(words[0], words[-1][:-2]): int(num)})
    if words[0] not in names:
        names.append(words[0])
    if words[-1][:-2] not in names:
        names.append(words[-1][:-2])

names.append("Justin")

p = permutations(range(9))

for option in p:
    total = 0
    for x in range(9):
        if names[option[x]] == "Justin" or names[option[x-1]] == "Justin":
            continue
        else:
            temp1 = relationships[(names[option[x-1]], names[option[x]])]
            temp2 = relationships[(names[option[x]], names[option[x-1]])]
            total += temp1 + temp2
        #print(names[option[x-1]], names[option[x]], temp1)
        #print(names[option[x]], names[option[x-1]], temp2)

    h.append(total)

print(max(h))
