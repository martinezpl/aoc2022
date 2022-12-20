with open("d2.txt", "r") as f:
    inp = f.read()

PART = 2

point_worth = {
    "A": 1,
    "B": 2,
    "C": 3,
}

killed_by = {"A": "C", "B": "A", "C": "B"}
my_points = 0
ops_points = 0

if PART == 1:
    translate = {"X": "A", "Y": "B", "Z": "C"}
else:
    kills = {v: k for k, v in killed_by.items()}

    def translate(ops_hand, outcome):
        if outcome == "X":  # loose
            return killed_by[ops_hand]
        elif outcome == "Y":  # draw
            return ops_hand
        elif outcome == "Z":  # win
            return kills[ops_hand]


pairs = inp.split("\n")
for p in pairs[:-1]:
    ops_hand, my_hand = p.split(" ")
    my_hand = translate[my_hand] if PART == 1 else translate(ops_hand, my_hand)

    if killed_by[ops_hand] == my_hand:
        ops_points += 6
    elif ops_hand == my_hand:
        my_points += 3
        ops_points += 3
    else:
        my_points += 6

    ops_points += point_worth[ops_hand]
    my_points += point_worth[my_hand]

print(my_points, ops_points)
