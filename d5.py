PART = 2

crates = None
instructions = None
with open("d5.txt", "r") as f:
    inp = f.read().split("\n")
    for i, l in enumerate(inp):
        if l == "":
            crates = inp[:i]
            instructions = inp[i + 1 : -1]
            break

stacks = {}

for i, ch in enumerate(crates[-1]):
    if ch != " ":
        stacks[ch] = [crate[i] for crate in crates[:-1] if crate[i] != " "]
        stacks[ch].reverse()

for ins in instructions:
    qty, _from, _to = [w for w in ins.split(" ") if w.isdecimal()]

    if PART == 1:
        for i in range(int(qty)):
            stacks[_to].append(stacks[_from].pop())
    elif PART == 2:
        stacks[_to] += stacks[_from][-int(qty) :]
        stacks[_from] = stacks[_from][: -int(qty)]

print(stacks)
print("".join([stacks[s][-1] for s in stacks]))
