#

# cost, damage, heal, mr, armor, duration
all_spells = { 'mm': [53, 4, 0, 0, 0, 1],
               'd':  [73, 2, 2, 0, 0, 1],
               's':  [113, 0, 0, 0, 7, 6],
               'p':  [173, 3, 0, 0, 0, 6],
               'r':  [229, 0, 0, 101, 0, 5] }
active_spells = dict()

wins = list()

bd = 10

def run_turn(mine, spent, mana, hp, boss_hp):
    global active_spells
    
    # apply effects
    damage = sum(i[1] for i in active_spells.values())
    armor = sum(i[4] for i in active_spells.values())
    mana += sum(i[3] for i in active_spells.values())

    # check boss hp
    boss_hp -= damage
    if boss_hp <= 0:
        wins.append(spent)
        return

    # decrement durations and remove old effects
    for x in list(active_spells.keys()):
        active_spells[x][5] -= 1
        if active_spells[x][5] == 0:
            active_spells.pop(x)

    #my turn
    if mine:
        # what can I cast?
        poss_spells = [x for x in all_spells if all_spells[x][0] <= mana and x not in [y[0] for y in active_spells]]
        # try them all!
        for x in poss_spells:
            spent += all_spells[x][0]
            mana -= all_spells[x][0]
            active_spells.update({x: all_spells[x]})
            #print('run_turn(False, ', spent, mana, hp, boss_hp)
            run_turn(False, spent, mana, hp, boss_hp)            
        
    #boss' turn
    else:
        hp = hp - max(bd - armor, 1)
        if hp <= 0:
            return
        #print('run_turn(True, ', spent, mana, hp, boss_hp)
        run_turn(True, spent, mana, hp, boss_hp)

run_turn(True, 0, 500, 50, 71)
print(wins)

##active_spells = {'r':[0,0,0,0,0]}
##poss_spells = [x for x in all_spells if all_spells[x][0] <= 500 and x not in [y[0] for y in active_spells]]
##print(poss_spells)

