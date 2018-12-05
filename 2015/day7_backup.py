import re

def add_value(label, number):
    global values

    if label not in values:
        values.update({label: number})
    else:
        print('problem', label, number, values)
        exit()

def follow_chain(label, wires):
    # first check to see if we know what this value is already
    if label in values:
        return values[label]
    
    # base case
    if re.match(r'\d+', label):
        print('in base case', label)
        return int(label)
    if len(wires[label]) == 1:
        print('in length of 1', label, wires[label])
        value = follow_chain(wires[label][0], wires)
    # unary NOT operator
    elif len(wires[label]) == 2:
        print('in NOT', wires[label], label)
        value = ~follow_chain(wires[label][1], wires)
    # AND operator
    elif wires[label][1] == 'AND':
        print('in AND', wires[label], label)
        value = follow_chain(wires[label][0], wires) & follow_chain(wires[label][2], wires)
    # OR operator
    elif wires[label][1] == 'OR':
        print('in OR', wires[label], label)
        value = follow_chain(wires[label][0], wires) | follow_chain(wires[label][2], wires)
    # LSHIFT
    elif wires[label][1] == 'LSHIFT':
        print('in LSHIFT', wires[label], label)
        value = follow_chain(wires[label][0], wires) << follow_chain(wires[label][2], wires)
    elif wires[label][1] == 'RSHIFT':
        print('in RSHIFT', wires[label], label)
        value = follow_chain(wires[label][0], wires) >> follow_chain(wires[label][2], wires)

    add_value(label, value)
    return value

f = open('input.txt')
wires = dict()
values = dict({'b': 956})

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
print(values['b'])



