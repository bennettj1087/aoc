from functools import reduce
import math

def factors(n):
    small_divisors = [i for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0]
    large_divisors = [n / d for d in small_divisors if n != d * d]
    return small_divisors + large_divisors

house_num = 2097152
min_presents = 36000000

factor_list = list()
place = 1
binary = bin(min_presents//10)[2:]
print(binary)
print(binary[::-1])
for d in binary[::-1]:
    if d == '1':
        factor_list.append(place)
    place = place * 2

print(factor_list)

house = [0 for x in range(min_presents//10+1)]

part_one, part_two = None,None
i = 0
while not part_one or not part_two:
    i += 1
    f = factors(i)
    if not part_one:
        if sum(f)*10 >= min_presents:
            part_one = i
    if not part_two:
        if sum(d for d in f if i/d <= 50) * 11 >= min_presents:
            part_two = i

print(part_one, part_two)
