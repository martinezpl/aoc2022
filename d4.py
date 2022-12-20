with open("d4.txt", "r") as f:
    inp = f.read()

PART = 2
pairs = inp.split("\n")[:-1]

fully_contain = 0
contain = 0

for p in pairs:
    p1, p2 = p.split(",")
    p1s = p1.split("-")
    p2s = p2.split("-")
    if PART == 1:
        counter = 0
        for i in range(int(p1s[0]), int(p1s[1]) + 1):
            if i in range(int(p2s[0]), int(p2s[1]) + 1):
                counter += 1
        if counter == len(range(int(p1s[0]), int(p1s[1]) + 1)):
            fully_contain += 1
            continue

        counter = 0
        for i in range(int(p2s[0]), int(p2s[1]) + 1):
            if i in range(int(p1s[0]), int(p1s[1]) + 1):
                counter += 1
        if counter == len(range(int(p2s[0]), int(p2s[1]) + 1)):
            fully_contain += 1
    else:
        for i in range(int(p1s[0]), int(p1s[1]) + 1):
            if i in range(int(p2s[0]), int(p2s[1]) + 1):
                contain += 1
                break

print(fully_contain)
print(contain)
