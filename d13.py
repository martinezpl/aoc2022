PART = 2


def compare(p1, p2):
    print("Compare", p1, "vs", p2)
    if type(p1) == list and type(p2) != list:
        print("Mixed types; convert right and retry comparison")
        p2 = [p2]
    elif type(p1) != list and type(p2) == list:
        print("Mixed types; convert left and retry comparison")
        p1 = [p1]
    if type(p1) == int and type(p2) == int:
        if p1 < p2:
            print("Left side is smaller, so inputs are in the right order")
            return True
        elif p1 > p2:
            print("Right side is smaller, so inputs are not in the right order")
            return False
        elif p1 == p2:
            return "continue"

    for i in range(max(len(p1), len(p2))):
        if i == len(p1):
            print("Left side ran out of items, so inputs are in the right order")
            return True
        elif i == len(p2):
            print("Right side ran out of items, so inputs are not in the right order")
            return False
        state = compare(p1[i], p2[i])
        if state == "continue":
            continue
        else:
            return state

    return "continue"


if PART == 1:
    with open("d13.txt", "r") as f:
        inp = f.read().split("\n\n")

    pairs = []
    for p in inp:
        p = p.split("\n")
        exec(f"pairs.append([{p[0]}, {p[1]}])")

    right_order_idx = []
    for i, p in enumerate(pairs):
        print(
            "==============================================================================="
        )
        if compare(p[0], p[1]):
            right_order_idx.append(i + 1)

    print(sum(right_order_idx))

else:
    import json

    with open("d13.txt", "r") as f:
        inp = [l for l in f.read().split("\n") if l]

    packets = {}
    for idx, p in enumerate(inp + ["[[2]]", "[[6]]"]):
        print(p)
        packets[idx] = json.loads(p)

    i = 0
    while True:
        changed = False
        i = 0
        while i < len(packets) - 1:
            print(
                "==============================================================================="
            )
            if not compare(packets[i], packets[i + 1]):
                packets[i], packets[i + 1] = packets[i + 1], packets[i]
                changed = True

            i += 1

        if not changed:
            break

    decoder_key = 1
    for idx in packets:
        if packets[idx] == [[2]] or packets[idx] == [[6]]:
            decoder_key *= idx + 1

    print(decoder_key)
