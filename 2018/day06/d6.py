# Day 6

import numpy as np
from operator import itemgetter

f = open('input.txt')
lines = [l.strip() for l in f.readlines()]
coords = [tuple(map(int, c.split(","))) for c in lines]

grid = np.zeros((max(coords, key=itemgetter(0))[0],
                 max(coords, key=itemgetter(1))[1]), np.int32)

for (x, y) in coords:
    np[x, y] = (x ,
