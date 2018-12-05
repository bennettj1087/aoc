#

f = open('input.txt')
ing = list()

for line in f:
    words = line.split(' ')
    ing.append((int(words[2][:-1]),
        int(words[4][:-1]),
        int(words[6][:-1]),
        int(words[8][:-1]),
        int(words[10][:-1])))
print(ing)
max = 0
score = 0

for i in range(100):
    for j in range(100-i):
        for k in range(100-i-j):
            l = 100-i-j-k
            cap = i*ing[0][0] + j*ing[1][0] + k*ing[2][0] + l*ing[3][0]
            dur = i*ing[0][1] + j*ing[1][1] + k*ing[2][1] + l*ing[3][1]
            fla = i*ing[0][2] + j*ing[1][2] + k*ing[2][2] + l*ing[3][2]
            tex = i*ing[0][3] + j*ing[1][3] + k*ing[2][3] + l*ing[3][3]
            cal = i*ing[0][4] + j*ing[1][4] + k*ing[2][4] + l*ing[3][4]

            if cal != 500:
                continue
            if cap<=0 or dur<=0 or fla<=0 or tex<=0:
                score = 0
                continue
            score = cap*dur*fla*tex
            if (score > max):
                max = score

print(max)
