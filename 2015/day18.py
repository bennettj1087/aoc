#

f = open('input.txt')
lights = list()

for line in f:
    strand = list()
    for c in range(len(line)):
        if line[c] == '#':
            strand.append(1)
        elif line[c] == '.':
            strand.append(0)
    lights.append(strand)

#lights = ((0,1,0,1,0,1),(0,0,0,1,1,0),(1,0,0,0,0,1),
#          (0,0,1,0,0,0),(1,0,1,0,0,1),(1,1,1,1,0,0))

for count in range(100):
    temp_lights = [[0 for x in range(100)] for x in range(100)]
    
    for i in range(100):
        for j in range(100):
            neighbors_on = 0
            if (i == 0 and j == 0) or (i == 0 and j == 99) or (i == 99 and j == 0) or (i == 99 and j == 99):
                temp_lights[i][j] = 1
                continue
            
            for x,y in ((i-1, j-1), (i-1, j), (i-1, j+1),
                        (i, j-1), (i, j+1),
                        (i+1, j-1), (i+1, j), (i+1, j+1)):
                if x < 0 or x > 99 or y < 0 or y > 99:
                    continue
                else:
                    if lights[x][y] == 1:
                        neighbors_on += 1

            if lights[i][j] == 1:
                if neighbors_on == 2 or neighbors_on == 3:
                    temp_lights[i][j] = 1
                    continue
                else:
                    temp_lights[i][j] = 0
                    continue

            if lights[i][j] == 0 and neighbors_on == 3:
                temp_lights[i][j] = 1
                continue
            else:
                temp_lights[i][j] = 0
                continue
            
    lights = temp_lights
    #print(lights)
    #print()
    
print(sum([sum(x) for x in lights]))
