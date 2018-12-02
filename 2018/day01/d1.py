# day 01

f = open("input.txt")
lines = f.readlines()
freq = 0

# part 1
for line in lines:
    freq += int(line.strip())
print("Part 1: ", freq)

# part 2
freq = 0
seen = set()
while True:
    for line in lines:
        freq += int(line.strip())
        if freq not in seen:
            seen.add(freq)
        else:
            print("Part 2: ", freq)
            exit(0)
