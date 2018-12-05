from itertools import combinations

def run_sim(d, a):
    my_health = 100
    monster_health = 103
    monster_damage = 9
    monster_armor = 2

    my_damage_per_turn = max(1, d - monster_armor)
    monster_damage_per_turn = max(1, monster_damage - a)

    while True:
        monster_health -= my_damage_per_turn
        if monster_health <= 0:
            return True
        
        my_health -= monster_damage_per_turn
        if my_health <= 0:
            return False
        
w = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
a = [(13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
r = [(25, 1, 0), (50, 2, 0), (100,3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]

wins = list()
count = 0
for i in w:
    for j in a:
        damage = i[1]
        armor = j[2]
        cost = i[0] + j[0]
        if not run_sim(damage, armor):
            #print(cost, 'won')
            wins.append((damage, armor, cost))
            
        for k in list(combinations(r, 2)) + list(combinations(r, 1)):
            new_cost = cost
            new_damage = damage
            new_armor = armor
            for x in k:
                new_damage += x[1]
                new_armor += x[2]
                new_cost += x[0]
            if not run_sim(new_damage, new_armor):
                wins.append((new_damage, new_armor, new_cost))

print(max(i[2] for i in wins))
                

