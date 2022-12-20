with open("d3.txt", "r") as f:
    inp = f.read()

rucksacks = inp.split("\n")[:-1]
print(len(rucksacks))


def translate(ch):
    v = ord(ch) - 96
    if v < 0:
        v = ord(ch) - 38
    return v


values = []
for i in range(3, len(rucksacks) + 1, 3):
    group = rucksacks[i - 3 : i]
    for t in set(group[0]):
        if t in set(group[1]) and t in set(group[2]):
            values.append(translate(t))


print(sum(values))
