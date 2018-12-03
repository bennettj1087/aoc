import re
from itertools import groupby

start = "1113222113"

##for x in range(50):
##    temp = ""
##    nums = re.findall("(?<=(.))(?!\\1)", start)
##    for num in nums:
##        count = 0
##        while start != "" and start[0] == num:
##            start = start[1:]
##            count += 1
##        temp += str(count) + num
##    start = temp

for x in range(50):
    start = ''.join([str(len(list(g))) + str(k) for k, g in groupby(start)])

print(len(start))
