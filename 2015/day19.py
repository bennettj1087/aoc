import re

f = open('input.txt')
r = dict()
c = "CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl"
element_re = re.compile('[A-Z][a-z]{0,1}')
all_poss = list()

for line in f:
    words = line.split(' ')
    if words[0] not in r:
        r.update({words[0]: list()})

    r[words[0]].append(words[2][:-1])

els = re.findall(element_re, c)
for i in range(len(els)):
    if els[i] in r:
        temp = els[i]
        for rep in r[temp]:
            els[i] = rep
            all_poss.append(''.join(els))
        els[i] = temp

print(len(els), els.count('Ar'), els.count('Rn'), els.count('Y'))
