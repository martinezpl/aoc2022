import sys, os

with open("d17.txt", "r") as f:
    inp = f.read()

from collections import deque
from itertools import cycle
from copy import deepcopy
from time import sleep

chamber = deque([["#", "#", "#", "#", "#", "#", "#"]])
jets = cycle(inp)
shapes = cycle("-+/|o")

shape = next(shapes)
rocks_fallen = 0
tall = 0


def visualize(s):
    print(
        "\n" + "\n".join([f"".join(s) + str(i) for i, s in enumerate(chamber)]),
        flush=True,
    )
    sleep(s)
    # os.system("clear")


def extend_chamber():
    while len(chamber) - 1 - tall > 3:
        chamber.popleft()
    while len(chamber) - 1 - tall < 3:
        chamber.appendleft([".", ".", ".", ".", ".", ".", "."])
    rng = None
    if shape == "-":
        chamber.appendleft([".", ".", "@", "@", "@", "@", "."])
        rng = [[0, [2, 6]]]
    elif shape == "+":
        chamber.appendleft([".", ".", ".", "@", ".", ".", "."])
        chamber.appendleft([".", ".", "@", "@", "@", ".", "."])
        chamber.appendleft([".", ".", ".", "@", ".", ".", "."])
        rng = [[0, [3, 4]], [1, [2, 5]], [2, [3, 4]]]
    elif shape == "/":
        chamber.appendleft([".", ".", "@", "@", "@", ".", "."])
        chamber.appendleft([".", ".", ".", ".", "@", ".", "."])
        chamber.appendleft([".", ".", ".", ".", "@", ".", "."])
        rng = [[0, [4, 5]], [1, [4, 5]], [2, [2, 5]]]
    elif shape == "|":
        chamber.appendleft([".", ".", "@", ".", ".", ".", "."])
        chamber.appendleft([".", ".", "@", ".", ".", ".", "."])
        chamber.appendleft([".", ".", "@", ".", ".", ".", "."])
        chamber.appendleft([".", ".", "@", ".", ".", ".", "."])

        rng = [[0, [2, 3]], [1, [2, 3]], [2, [2, 3]], [3, [2, 3]]]
    elif shape == "o":
        chamber.appendleft([".", ".", "@", "@", ".", ".", "."])
        chamber.appendleft([".", ".", "@", "@", ".", ".", "."])

        rng = [[0, [2, 4]], [1, [2, 4]]]

    return rng


def set_rest(rng):
    global rocks_fallen, tall
    for r in rng:
        for x in range(r[1][0], r[1][1]):
            chamber[r[0]][x] = "#"
    rocks_fallen += 1
    tall = max(tall, len(chamber) - 1 - rng[0][0])


def adjust(rng, new_rng):
    for r in rng:
        for x in range(r[1][0], r[1][1]):
            chamber[r[0]][x] = "."

    for r in new_rng:
        for x in range(r[1][0], r[1][1]):
            chamber[r[0]][x] = "@"

    return new_rng


def fall_step(rng, jet):
    mv = -1 if jet == "<" else 1
    movable = 0
    for r in rng:
        if r[1][0] + mv >= 0 and r[1][1] + mv <= 7:
            if (jet == "<" and chamber[r[0]][r[1][0] + mv] != "#") or (
                jet == ">" and chamber[r[0]][min(r[1][1], 6)] != "#"
            ):
                movable += 1
    if movable == len(rng):
        crng = deepcopy(rng)
        for r in rng:
            r[1][0] += mv
            r[1][1] += mv
        rng = adjust(crng, rng)
    # visualize()

    for r in rng[::-1]:
        for x in range(r[1][0], r[1][1]):
            if chamber[r[0] + 1][x] == "#":
                return set_rest(rng)

    new_rng = deepcopy(rng)
    for r in new_rng[::-1]:
        r[0] += 1

    a = adjust(rng, new_rng)
    # visualize()
    return a


PART = 2
if PART == 1:
    while rocks_fallen < 2022:
        print(rocks_fallen)
        rng = extend_chamber()
        rs = rocks_fallen
        # visualize()
        while rocks_fallen == rs:
            # visualize()
            rng = fall_step(rng, next(jets))

        shape = next(shapes)

    # visualize()
    print(tall)

if PART == 2:
    qty = len(inp)
    pattern_repeats_after = qty if qty % 4 == 0 else qty * 4

    rest = 1000000000000 % pattern_repeats_after
    pattern_repetition = 1000000000000 // pattern_repeats_after

    while rocks_fallen < pattern_repeats_after + 1000:
        rng = extend_chamber()
        rs = rocks_fallen
        # visualize()
        while rocks_fallen == rs:
            # visualize()
            rng = fall_step(rng, next(jets))

        shape = next(shapes)

    print(tall)
    tall *= pattern_repetition

    rocks_fallen = 0
    while rocks_fallen < rest:
        rng = extend_chamber()
        rs = rocks_fallen
        # visualize()
        while rocks_fallen == rs:
            # visualize()
            rng = fall_step(rng, next(jets))

        shape = next(shapes)

    print(rest)
    print(pattern_repetition)
    print(pattern_repeats_after)
    print(tall)

visualize(0.1)

1514285714288
1650000000000
