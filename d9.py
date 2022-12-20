with open("d9.txt", "r") as f:
    inp = f.read().split("\n")[:-1]

PART = 2

tail_positions = set()

knots = []
for i in range(2 if PART == 1 else 10):
    knots.append([0, 0])


def adjust_tail(head_pos, tail_pos):
    if head_pos[1] == tail_pos[1] or head_pos[0] == tail_pos[0]:
        if head_pos[1] - tail_pos[1] > 1:
            tail_pos[1] += 1
        elif head_pos[1] - tail_pos[1] < -1:
            tail_pos[1] -= 1
        if head_pos[0] - tail_pos[0] > 1:
            tail_pos[0] += 1
        elif head_pos[0] - tail_pos[0] < -1:
            tail_pos[0] -= 1
    else:
        if head_pos[1] - tail_pos[1] > 1:
            if tail_pos[0] < head_pos[0]:
                tail_pos[0] += 1
            else:
                tail_pos[0] -= 1
            tail_pos[1] += 1
        elif head_pos[1] - tail_pos[1] < -1:
            if tail_pos[0] < head_pos[0]:
                tail_pos[0] += 1
            else:
                tail_pos[0] -= 1
            tail_pos[1] -= 1
        if head_pos[0] - tail_pos[0] > 1:
            tail_pos[0] += 1
            if tail_pos[1] < head_pos[1]:
                tail_pos[1] += 1
            else:
                tail_pos[1] -= 1
        elif head_pos[0] - tail_pos[0] < -1:
            tail_pos[0] -= 1
            if tail_pos[1] < head_pos[1]:
                tail_pos[1] += 1
            else:
                tail_pos[1] -= 1


def move(head_pos, direction):
    if direction == "U":
        head_pos[1] += 1
    elif direction == "D":
        head_pos[1] -= 1
    elif direction == "R":
        head_pos[0] += 1
    elif direction == "L":
        head_pos[0] -= 1


for instruction in inp:
    direction, steps = instruction.split(" ")
    print(knots)
    print(direction, steps)
    for _ in range(int(steps)):
        move(knots[0], direction)
        for i in range(len(knots) - 1):
            adjust_tail(knots[i], knots[i + 1])

        tail_positions.add(tuple(knots[-1]))

print(len(tail_positions))
