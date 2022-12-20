with open("d6.txt", "r") as f:
    inp = f.read().split("\n")[0]

PART = 2

buffer = []
for i, ch in enumerate(inp):
    buffer.append(ch)
    if len(buffer) == (4 if PART == 1 else 14):
        if len(set(buffer)) == len(buffer):
            print(i + 1)
            break

        buffer.pop(0)
