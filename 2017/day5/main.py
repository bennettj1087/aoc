
with open('input.txt') as f:
    current = 0
    counter = 1
    jumps = [int(line.strip()) for line in f]
    #jumps = [0, 3, 0, 1, -3]
    while True:
        new = current + jumps[current]
        #print(jumps, current, new)
        if new >= 0 and new < len(jumps):
            if jumps[current] >= 3:
                jumps[current] -= 1
            else:
                jumps[current] += 1
            current = new
            counter += 1
        else:
            break

        #input()

print(counter)
