import itertools

checksum = 0

with open('input.txt', 'r') as f:
    for line in f:
        l = [int(x) for x in line.split()]
        perm = itertools.permutations(l, 2)
        for (a,b) in perm:
            if a % b == 0:
                checksum += a // b

    print(checksum)
