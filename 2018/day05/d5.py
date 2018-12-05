# Day 5

f = open('input.txt')
p = list(f.readlines()[0].strip())

test = list("dabAcCaCBAcCcaDA")
#p = test

# Part 1
i = 0
while i < len(p)-1:
    if p[i].islower() and p[i+1].lower() == p[i] and p[i+1].isupper() or p[i].isupper() and p[i+1].upper() == p[i] and p[i+1].islower():

        p.pop(i)
        p.pop(i)
        i = i - 1
        if i < 0: i = 0
    else:
        i += 1

print(len(p))
    
