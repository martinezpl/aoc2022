with open("d14.txt", "r") as f:
    inp = f.read().split("\n")

PART = 2
mtx = []
for i in range(200):
    mtx.append(["."] * 1200)

max_bottom = 0

for l in inp:
    points = l.split(" -> ")
    i = 0
    while i in range(len(points) - 1):
        _from = list(map(int, points[i].split(",")))
        _to = list(map(int, points[i + 1].split(",")))
        max_bottom = max(max_bottom, _to[1])
        while _from != _to:
            mtx[_from[1]][_from[0]] = "#"
            if _from[0] != _to[0]:
                _from[0] += 1 if _from[0] < _to[0] else -1
            elif _from[1] != _to[1]:
                _from[1] += 1 if _from[1] < _to[1] else -1
            print(_from, _to)
        mtx[_from[1]][_from[0]] = "#"
        i += 1

if PART == 1:
    score = 0
    while True:
        sand_pos = [0, 500]
        while True:
            if mtx[sand_pos[0] + 1][sand_pos[1]] == ".":
                sand_pos[0] += 1
            else:
                if mtx[sand_pos[0] + 1][sand_pos[1] - 1] == ".":
                    sand_pos[0] += 1
                    sand_pos[1] -= 1
                elif mtx[sand_pos[0] + 1][sand_pos[1] + 1] == ".":
                    sand_pos[0] += 1
                    sand_pos[1] += 1
                else:
                    mtx[sand_pos[0]][sand_pos[1]] = "o"
            print(sand_pos[0], max_bottom)
            if sand_pos[0] > max_bottom or mtx[sand_pos[0]][sand_pos[1]] == "o":
                break
        print(sand_pos)
        if sand_pos[0] > max_bottom:
            break
        score += 1

    print(score)

else:
    for i in range(len(mtx[0])):
        mtx[max_bottom + 2][i] = "#"

    score = 1
    while True:
        sand_pos = [0, 500]
        while True:
            if mtx[sand_pos[0] + 1][sand_pos[1]] == ".":
                sand_pos[0] += 1
            else:
                print(sand_pos)
                if mtx[sand_pos[0] + 1][sand_pos[1] - 1] == ".":
                    sand_pos[0] += 1
                    sand_pos[1] -= 1
                elif mtx[sand_pos[0] + 1][sand_pos[1] + 1] == ".":
                    sand_pos[0] += 1
                    sand_pos[1] += 1
                else:
                    mtx[sand_pos[0]][sand_pos[1]] = "o"
            if mtx[sand_pos[0]][sand_pos[1]] == "o":
                break
        print(sand_pos)
        if sand_pos == [0, 500]:
            break
        score += 1

    print(score)
