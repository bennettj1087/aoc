#

with open('input.txt') as f:
    ins = [line.rstrip() for line in f]

position = 0
registers = {'a': 1, 'b': 0}
while 0 <= position < len(ins):
    if ins[position][:3] == 'hlf':
        #print(position, "hlf", ins[position][:2], ins[position][4], registers[ins[position][4]])
        registers[ins[position][4]] = registers[ins[position][4]] // 2
        position += 1
        continue
    if ins[position][:3] == 'tpl':
        #print(position, "tpl", ins[position][:2], ins[position][4], registers[ins[position][4]])
        registers[ins[position][4]] = registers[ins[position][4]] * 3
        position += 1
        continue
    if ins[position][:3] == 'inc':
        #print(position, "inc", ins[position][:2], ins[position][4], registers[ins[position][4]])
        registers[ins[position][4]] += 1
        position += 1
        continue
    if ins[position][:3] == 'jmp':
        #print(position, "jmp", ins[position][:2], ins[position][4])
        if ins[position][4] == '+':
            position += int(ins[position][5:])
            continue
        else:
            position -= int(ins[position][5:])
            continue
    if ins[position][:3] == 'jie':
        #print(position, "jie", ins[position][:2], ins[position][4], registers[ins[position][4]])
        if registers[ins[position][4]] % 2 == 0:
            if ins[position][7] == '+':
                position += int(ins[position][8:])
            else:
                position -= int(ins[position][8:])
        else:
            position += 1
        continue
    if ins[position][:3] == 'jio':
        #print(position, "jio", ins[position][:2], ins[position][4],
        #      registers[ins[position][4]])
        if registers[ins[position][4]] == 1:
            if ins[position][7] == '+':
                position += int(ins[position][8:])
            else:
                position -= int(ins[position][8:])
        else:
            position += 1
        continue

print(registers)
