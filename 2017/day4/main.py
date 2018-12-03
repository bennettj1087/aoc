from collections import Counter

def soln(pwd, hashfn):
    words = set()
    for word in pwd.split():
        hashed = hashfn(word)
        if hashed in words:
            return False
        words.add(hashed)
    return True

totalp1 = 0
totalp2 = 0

identity = lambda x : x
anagram = lambda x : frozenset(Counter(x).items())

with open('input.txt') as f:
    for line in f:
        totalp1 += soln(line, identity)
        totalp2 += soln(line, anagram)

print(totalp1, totalp2)
