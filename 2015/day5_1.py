import re

f = open('input.txt', 'r')
nice = 0

vregex = re.compile(r'(\w)(\w).*\1\2')
dregex = re.compile(r'(\w)\w\1')

for line in f.readlines():
    vowels = re.findall(vregex, line)
    if len(vowels) < 1:
        continue

    doubles = re.findall(dregex, line)
    if len(doubles) < 1:
        continue

    nice += 1
    
print(nice)
