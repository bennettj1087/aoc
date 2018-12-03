import re
    
def increment_list(l, position=-1):
    if position < -len(l):
        l.insert(0, int("97"))
        return l
    l[position] += 1
    if l[position] == 123:
        l[position] = 97
        return increment_list(l, position=position - 1)
    return l

start = "cqjxjnds"
nums = [ord(x) for x in start]

iol = re.compile('i|o|l')
pairs = re.compile('([a-z])\\1')

count = 1

while True:
    nums = increment_list(nums)
    temp = ''.join([chr(x) for x in nums])
    if len(re.findall(iol, temp)) > 0:
        continue
    if len(re.findall(pairs, temp)) < 2:
        continue

    seq = False
    for i in range(0, len(nums)-2):
        if nums[i+1] == nums[i]+1 and nums[i+2] == nums[i]+2:
            seq = True
            break
        
    if not seq:
        continue

    print(temp)
    if count == 2:
        break
    else:
        count += 2


