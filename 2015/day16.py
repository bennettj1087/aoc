import re

f = open('input.txt')
aunts = list()

answer = (3, 7, 2, 3, 0, 0, 5, 3, 2, 1)

ch_re = re.compile('children: (\d+)')
cats_re = re.compile('cats: (\d+)')
sam_re = re.compile('samoyeds: (\d+)')
pom_re = re.compile('pomeranians: (\d+)')
ak_re = re.compile('akitas: (\d+)')
viz_re = re.compile('vizslas: (\d+)')
gf_re = re.compile('goldfish: (\d+)')
tree_re = re.compile('trees: (\d+)')
cars_re = re.compile('cars: (\d+)')
perf_re = re.compile('perfumes: (\d+)')

regexes = (ch_re, cats_re, sam_re, pom_re, ak_re, viz_re,
           gf_re, tree_re, cars_re, perf_re)

things = ('children =', 'cats >', 'samoyeds =', 'pomeranians <', 'akitas =',
          'vizslas =', 'goldfish <', 'trees >', 'cars =', 'perfumes =')

for line in f:
    match_score = 0
    for x in range(10):
        m = re.findall(regexes[x], line)
        if len(m) > 0:
            #print(things[x], answer[x], int(m[0]))
            if x == 1 or x == 7:
                if int(m[0]) > answer[x]:
                    match_score += 1
            elif x == 3 or x == 6:
                if int(m[0]) < answer[x]:
                    match_score += 1
            elif int(m[0]) == answer[x]:
                match_score += 1
    #print(match_score)
    #print()
    aunts.append(match_score)

for x in range(len(aunts)):
    if aunts[x] == max(aunts):
        print(x, aunts[x])

    
