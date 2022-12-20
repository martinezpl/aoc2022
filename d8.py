with open("d8.txt", "r") as f:
    inp = f.read().split("\n")[:-1]

PART = 2


left_side = [
    [f"{row}-{col}-{inp[row][col]}" for col in range(len(inp[row]))]
    for row in range(len(inp))
]
right_side = [row[::-1] for row in left_side]
top_side = [[left_side[j][i] for j in range(len(inp))] for i in range(len(inp[0]))]
bottom_side = [row[::-1] for row in top_side]

if PART == 1:
    is_visible = {}
    for mtx in [left_side, right_side, top_side, bottom_side]:
        for row in mtx:
            last_max = -1
            for col in row:
                height = int(col.split("-")[-1])
                if height > last_max:
                    is_visible[col] = True
                    last_max = height
                if last_max == 9:
                    break

    print(len(is_visible))

else:
    from collections import defaultdict
    import math

    scenic_score = defaultdict(list)
    for mtx in [left_side, right_side, top_side, bottom_side]:
        for j, row in enumerate(mtx):
            for i, col in enumerate(row):
                ref_height = int(col.split("-")[-1])
                score = 0
                for next_col in row[i + 1 :]:
                    score += 1
                    height = int(next_col.split("-")[-1])
                    if height >= ref_height:
                        break
                    last_height = height
                scenic_score[col].append(score)

    print(max([math.prod(v) for k, v in scenic_score.items()]))
