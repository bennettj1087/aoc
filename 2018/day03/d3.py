# Day 3

f = open("input.txt")
lines = [x.split() for x in f.readlines()]
f.close()
test = [x.split() for x in "#1 @ 1,3: 4x4\n#2 @ 1,3: 4x4\n#3 @ 1,3: 2x2".split("\n")]

points = dict()
for x in lines:
    points[x[0][1:]] = [tuple(x[2][:-1].split(',')), tuple(x[3].split('x'))]

# Part 1
grid = dict()
for id, claim in points.items():
    p = claim[0]
    dim = claim[1]
    for x in range(int(dim[0])):
        for y in range(int(dim[1])):
            new_x = int(p[0]) + x
            new_y = int(p[1]) + y
            if (new_x, new_y) not in grid:
                grid[new_x, new_y] = 1
            else:
                grid[new_x, new_y] += 1
print(len([k for k,v in grid.items() if v > 1]))

# Part 2
overlapped = False
for id, (p,dim) in points.items():
    for x in range(int(dim[0])):
        for y in range(int(dim[1])):
            new_x = int(p[0]) + x
            new_y = int(p[1]) + y
            if grid[new_x, new_y] != 1:
                overlapped = True
    if not overlapped:
        print(id)
        exit(0)
    overlapped = False
    
