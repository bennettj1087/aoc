# Day 2

import string

f = open("input.txt")
lines = f.readlines()
test = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]

# Part 1
letters = dict({x: 0 for x in string.ascii_lowercase[:26]})
twice = 0
thrice = 0
done2 = False
done3 = False
for line in lines:
    for l in line.strip():
        letters[l] += 1
    #print(letters)
    for k, v in letters.items():
        if v == 2 and not done2:
            twice += 1
            done2 = True
        if v == 3 and not done3:
            thrice += 1
            done3 = True
    #print(twice, thrice)
    letters = dict({x: 0 for x in string.ascii_lowercase[:26]})
    done2 = False
    done3 = False

print(twice*thrice)

# Part 2
test = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]

for t in lines:
    for u in lines[1:]:
        diff = 0
        for x in range(0, len(t)):
            if t[x] != u[x]:
                diff += 1
        if diff == 1:
            print(t, u)
            exit(0)
    lines = lines[1:]
        
    
