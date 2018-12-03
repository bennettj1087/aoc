
with open('input.txt') as f:
    states = list()
    
    for line in f:
        banks = [int(n) for n in line.split()]
    n = len(banks)

    states.append(banks.copy())
    #print(banks)

    counter = 0
    while True:
        i_max = 0
        for i in range(0, n):
            if banks[i] > banks[i_max]:
                i_max = i

        blocks = banks[i_max]
        banks[i_max] = 0
        index = (i_max + 1) % n
        while blocks > 0:
            banks[index] += 1
            index = (index + 1) % n
            blocks -= 1

        if banks not in states:
            states.append(banks.copy())
            counter += 1
        else:
            counter += 1
            print(counter - states.index(banks.copy()))
            break
        #input()
print(counter)
