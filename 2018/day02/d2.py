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
