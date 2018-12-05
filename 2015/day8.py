import re

uni = re.compile('\\\\x([0-9a-f]{2})')
backslash = re.compile('\\\\')
quote = re.compile('"')
quote2 = re.compile('^"')
quote3 = re.compile('"$')

f = open('input.txt')
#f = ['""', '"abc"', r'"aaa\"aaa"', r'"\x27"']
total = 0

for line in f:
    line = line.strip()
    print(line, len(line))
    total -= len(line)
    #line = re.sub(uni, '\\\\\\\\x\\1', line)
    line = re.sub(backslash, '\\\\\\\\', line)
    line = re.sub(quote, '\\\\"', line)
    print(line, len(line))
    print()
    total += len(line) + 2

print(total)

##tests = [r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"']
##print([len(x) for x in tests])
##
##stripped = [re.sub(pattern, '*', x) for x in tests]
##stripped = [re.sub(quote, '', x) for x in stripped]
##
##print([len(x) for x in stripped])
