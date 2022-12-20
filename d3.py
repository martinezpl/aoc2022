with open("d3.txt", "r") as f:
    inp = f.read()

rucksacks = inp.split("\n")[:-1]
print(rucksacks)
rucksacks = [(c[: (len(c) // 2)], c[(len(c) // 2) :]) for c in rucksacks]
print(rucksacks)


def translate(ch):
    v = ord(ch) - 96
    if v < 0:
        v = ord(ch) - 38
    return v


common_types = []
for rucksack in rucksacks:
    c1, c2 = rucksack
    for t in set(c1):
        if t in c2:
            print(t)
            common_types.append(translate(t))

print(sum(common_types))
