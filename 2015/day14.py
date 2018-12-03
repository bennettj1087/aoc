#

reindeer = dict()
distances = dict()
rest_flags = dict()
f = open("input.txt")

for line in f:
    words = line.split(' ')
    reindeer.update({words[0]: {
        "speed": int(words[3]),
        "max_go": int(words[6]),
        "rest": int(words[-2]),
        "resting": False,
        "distance": 0,
        "go_counter": 0,
        "rest_counter": 0,
        "points": 0 }})
        
for t in range(1, 2504):
    for deer in reindeer.values():
        if deer['resting'] == True:
            deer['rest_counter'] += 1
            if deer['rest_counter'] == deer['rest']:
                deer['resting'] = False
                deer['rest_counter'] = 0
            continue
        deer['distance'] += deer['speed']
        deer['go_counter'] += 1
        if deer['go_counter'] == deer['max_go']:
            deer['resting'] = True
            deer['go_counter'] = 0

    longest = max([x['distance'] for x in reindeer.values()])
    for deer in reindeer:
        if reindeer[deer]['distance'] == longest:
            reindeer[deer]['points'] += 1

print(max([x['points'] for x in reindeer.values()]))
