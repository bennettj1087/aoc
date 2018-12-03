with open('input.txt') as f:
    data = f.read().splitlines()

regs = dict()
max_int = 0

for line in data:
    toks = line.split()

    reg = toks[0]

    if reg not in regs:
        regs[reg] = 0
    if toks[4] not in regs:
        regs[toks[4]] = 0
    if eval('regs["' + toks[4] + '"]' + toks[5] + toks[6]):
        if toks[1] == "inc":
            regs[reg] += int(toks[2])
        else:
            regs[reg] -= int(toks[2])

        max_int = max(max_int, regs[reg])

print(max(regs.values()), max_int)
