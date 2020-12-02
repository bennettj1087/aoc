#from collections import Counter

def calc_fuel(mass):
    return mass // 3 - 2

p1_fuel = 0
p2_fuel = 0
with open('../rust/input/2019/day1.txt') as f:
    for line in f:
        tmp_fuel = calc_fuel(int(line))
        p1_fuel += tmp_fuel
        
        mod_fuel = 0
        while tmp_fuel > 0:
            p2_fuel += tmp_fuel
            mod_fuel += tmp_fuel
            #print(tmp_fuel, p2_fuel)
            tmp_fuel = calc_fuel(tmp_fuel)
        print("Total for " + line.strip() + ": " + str(mod_fuel))


print("Part1: " + str(p1_fuel))
print("Part2: " + str(p2_fuel))