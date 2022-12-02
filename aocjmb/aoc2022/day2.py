from aocd import data
from itertools import combinations

wins = { "A": "Y",
         "B": "Z",
         "C": "X"
       }
draws = { "A": "X", "B": "Y", "C": "Z"}
losses = {"A": "Z", "B": "X", "C": "Y"}
points = {"X": 1, "Y": 2, "Z": 3}

def part_a(data):
    score = 0
    data = data.strip().split("\n")
    for round in data:
        y, m = round.split(" ")
        if (wins[y] == m):
            score += 6
        elif (draws[y] == m):
            score += 3
        score += points[m]
        #print(y, m, wins[y], score)
    return score

def part_b(data):
    score = 0
    data = data.strip().split("\n")

    for round in data:
        move, strat = round.split(" ")
        if (strat == "X"): #lose
            score += points[losses[move]]
        elif (strat == "Y"): #draw
            score += 3 + points[draws[move]]
        else: #win
            score += 6 + points[wins[move]]
        #print(move, strat, score)
    return score


test_data = """\
A Y
B X
C Z
"""

if __name__ == "__main__":
    assert part_a(test_data) == 15
    assert part_b(test_data) == 12
    print(part_a(data))
    print(part_b(data))
