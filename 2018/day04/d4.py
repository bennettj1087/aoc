# Day 4

import time
import re
from operator import itemgetter

f = open('input.txt')
lines = f.readlines()
f.close()
lines.sort()

events = [e.strip().split("]") for e in lines]
patterns = {"guard": re.compile("Guard"),
            "falls": re.compile("falls"),
            "wakes": re.compile("wakes"),
            "id": re.compile("#(\d+)")}

start_sleep = 0
guard = 0
guards = dict()
max_mins = {"guard": 0, "num": 0, "minute": 0}
for e in events:
    minute = int(e[0][-2:])
    if re.findall(patterns["guard"], e[1]) != []:
        guard = re.findall(patterns["id"], e[1])[0]
    elif re.findall(patterns["falls"], e[1]) != []:
        start_sleep = minute
    elif re.findall(patterns["wakes"], e[1]) != []:
        if guard not in guards:
            guards[guard] = [0 for x in range(0, 60)]
        for x in range(start_sleep, minute):
            guards[guard][x] += 1
            # Solve part 2
            if guards[guard][x] > max_mins["num"]:
                max_mins = {"guard": int(guard), "num": int(guards[guard][x]), "minute": x}
    else:
        print("Error")
        exit(0)

# Solve part 1
sleepiest = 0
for i,sleep in guards.items():
    total = sum(sleep)
    if sleepiest == 0:
        sleepiest = i
    if total > sum(guards[sleepiest]):
        sleepiest = i

print(sleepiest, max(guards[sleepiest]), int(sleepiest)*guards[sleepiest].index(max(guards[sleepiest])))
print(max_mins["guard"]*max_mins["minute"])

