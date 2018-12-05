
sum = 0

with open('input.txt', 'r') as f:
    s = f.read().strip()
    half = len(s) // 2
    #print(half)
    for i in range(0, len(s)):
        #print(i, s[i], i+half, s[(i+half)%len(s)])
        if s[i] == s[(i+half)%len(s)]:
            sum += int(s[i])

print(sum)
