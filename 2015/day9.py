from itertools import permutations

routes = dict()
places = list()
distances = list()

with open('input.txt') as f:
    for line in f:
        words = line.split(' ')
        routes.update({(words[0], words[2]): words[4][:-1]})
        routes.update({(words[2], words[0]): words[4][:-1]})
        if words[0] not in places:
            places.append(words[0])
        if words[2] not in places:
            places.append(words[2])

p = permutations(range(8))

for option in p:
    d = 0
    #print(option)
    for x in range(1,8):
        temp = int(routes[(places[option[x-1]], places[option[x]])])
        #print(temp)
        d += temp

    distances.append(d)

print(places)
#print(distances)

print(max(distances))
