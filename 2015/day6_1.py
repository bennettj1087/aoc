import re

def follow_chain(label, wires):
    # base case
    if len(wires[label]) == 1:
        print('in base case', label, wires[label])
        if re.match(r'\d+', wires[label][0]):
            # must be a number
            print('in NUMBER', wires[label][0], label)
            return int(wires[label][0])
        else:
            print('follow_chain', wires[label][0], label)
            return follow_chain(wires[label][0], wires)
    # unary NOT operator
    elif len(wires[label]) == 2:
        print('in NOT', wires[label], label)
        return ~follow_chain(wires[label][1], wires)
    # AND operator
    elif wires[label][1] == 'AND':
        print('in AND', wires[label], label)
        if re.match(r'\d+', wires[label][0]):
            return int(wires[label][0]) & follow_chain(wires[label][2], wires)
        elif re.match(r'\d+', wires[label][2]):
            return follow_chain(wires[label][0], wires) & int(wires[label][2])
        else:
            return follow_chain(wires[label][0], wires) & follow_chain(wires[label][2], wires)
    # OR operator
    elif wires[label][1] == 'OR':
        print('in OR', wires[label], label)
        if re.match(r'\d+', wires[label][0]):
            return int(wires[label][0]) | follow_chain(wires[label][2], wires)
        elif re.match(r'\d+', wires[label][2]):
            return follow_chain(wires[label][0], wires) | int(wires[label][2])
        else:
            return follow_chain(wires[label][0], wires) | follow_chain(wires[label][2], wires)
    # LSHIFT
    elif wires[label][1] == 'LSHIFT':
        print('in LSHIFT', wires[label], label)
        if re.match(r'\d+', wires[label][0]):
            return int(wires[label][0]) << follow_chain(wires[label][2], wires)
        elif re.match(r'\d+', wires[label][2]):
            return follow_chain(wires[label][0], wires) << int(wires[label][2])
        else:
            return follow_chain(wires[label][0], wires) << follow_chain(wires[label][2], wires)
    # RSHIFT
    elif wires[label][1] == 'RSHIFT':
        print('in RSHIFT', wires[label], label)
        if re.match(r'\d+', wires[label][0]):
            return int(wires[label][0]) >> follow_chain(wires[label][2], wires)
        elif re.match(r'\d+', wires[label][2]):
            return follow_chain(wires[label][0], wires) >> int(wires[label][2])
        else:
            return follow_chain(wires[label][0], wires) >> follow_chain(wires[label][2], wires)

f = open('input.txt')
wires = dict()

tokens = re.compile(r'[A-Z]+|[a-z]+|\d+')

# Get all of the wires
for line in f:
    els = re.findall(tokens, line)
    if els[-1] not in wires:
        wires.update({els[-1]: els[:-1]})
    else:
        print("this is a problem", line)
        break

print(follow_chain('a', wires))


