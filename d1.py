with open("d1.txt", "r") as f:
    inp = f.read()

calories = inp.split("\n")

totals = []

cal_total = 0
for cal in calories:
    if cal == "":
        totals.append(cal_total)
        cal_total = 0
        continue

    cal_total += int(cal)

# p1
print(max(totals))

# p2
print(sum(sorted(totals, reverse=True)[:3]))
