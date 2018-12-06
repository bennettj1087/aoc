# Day 5

import string

f = open('input.txt')
inp = list(f.readlines()[0].strip())

test = list("dabAcCaCBAcCcaDA")

def react(p):
    i = 0
    while i < len(p)-1:
        if p[i].islower() and p[i+1].lower() == p[i] and p[i+1].isupper() or p[i].isupper() and p[i+1].upper() == p[i] and p[i+1].islower():
            p.pop(i)
            p.pop(i)
            i = i - 1
            if i < 0: i = 0
        else:
            i += 1
    return len(p)

# Part 1
print(react(inp.copy()))

# Part 2
results = dict()
for unit in string.ascii_lowercase:
    both = [unit, unit.upper()]
    reduced = [x for x in inp if x not in both]
    results[unit] = react(reduced)

print(results[min(results, key=results.get)])
