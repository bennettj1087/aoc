import re

f = open('input.txt')

lights = [[0 for x in range(1000)] for x in range(1000)]
int_regex = re.compile('\d+')
num_lines = 6
lines = 0

for line in f:
    #lines += 1
    #if lines > num_lines:
    #    print('ending')
    #    break

    #print('processing line')
    start_x, start_y, end_x, end_y = re.findall(int_regex, line)

    for i in range(int(start_x), int(end_x)+1):
        for j in range(int(start_y), int(end_y)+1):
            if line.startswith('toggle'):
                lights[i][j] += 2
            elif line.startswith('turn on'):
                lights[i][j] += 1
            elif line.startswith('turn off'):
                lights[i][j] = max(lights[i][j] - 1, 0)

print(sum([sum(x) for x in lights]))
