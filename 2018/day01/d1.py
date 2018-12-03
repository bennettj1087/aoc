# day 01

from itertools import cycle, accumulate

f = open("input.txt")
lines = f.readlines()

# part 1
as_ints = [int(i) for i in lines]
print(sum(as_ints))

# part 2
seen = {0}
print(next(x for x in accumulate(cycle(as_ints)) if x in seen or seen.add(x)))
