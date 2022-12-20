with open("d20.txt", "r") as f:
    inp = f.read().split("\n")


from itertools import cycle
from copy import copy

PART = 2


nums = []
for ix, i in enumerate(inp):
    inp[ix] = int(inp[ix]) * (811589153 if PART == 2 else 1)
    nums.append((inp[ix], ix))

for i in range(10 if PART == 2 else 1):
    for i, n in enumerate(inp):
        n = int(n)
        if n == 0:
            continue
        i = nums.index((n, i))
        to = (i + n) % (len(inp) - 1)
        nums.insert(to, nums.pop(i))
        # print(f"{n} moves to {to} - between {nums[to-1]} and {nums[(to+1) % len(inp)]}")
        # print(nums)

sum = 0
c = cycle(nums)
while True:
    n = next(c)
    if n[0] == 0:
        i = 0
        while True:
            i += 1
            n = next(c)
            if i in [1000, 2000, 3000]:
                sum += n[0]
            if i > 3000:
                break
        break

print(sum)
