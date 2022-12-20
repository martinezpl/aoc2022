with open("d18.txt", "r") as f:
    inp = f.read().split("\n")

PART = 2


aircubes = {}


class AirCube:
    def __init__(self, x, y, z, blocks=None):
        self.pos = (int(x), int(y), int(z))
        self.neighbors = set()
        self.trapped = False
        self.blocks = blocks or set()

        if self.pos not in aircubes:
            aircubes[self.pos] = self


class Cube:
    def __init__(self, x, y, z):
        self.pos = (int(x), int(y), int(z))
        self.neighbors = set()

    def is_adjacent(self, c):
        sc = 0
        for i in range(len(self.pos)):
            sc += abs(self.pos[i] - c.pos[i])
        if sc == 1:
            print(self.pos, "is neighbor of", c.pos)
            return True
        return False

    def classify_neighbors(self):
        free_sides = 6 - len(self.neighbors)

        if PART == 2:
            n_pos = [list(c.pos) for c in self.neighbors]
            ref = list(self.pos)
            for i in [0, 1, 2]:
                ref[i] += 1
                if ref not in n_pos:
                    c = aircubes.get(tuple(ref))
                    if not c:
                        c = AirCube(*ref)
                    c.blocks.add(self)
                ref[i] -= 2
                if ref not in n_pos:
                    c = aircubes.get(tuple(ref))
                    if not c:
                        c = AirCube(*ref)
                    c.blocks.add(self)
                ref = list(self.pos)

        return free_sides


cubes = [Cube(*c.split(",")) for c in inp]
surface_area = 0

for c in cubes:
    for c2 in cubes:
        if c is c2:
            continue
        if c.is_adjacent(c2):
            c.neighbors.add(c2)

for c in cubes:
    surface_area += c.classify_neighbors()

if PART == 1:
    print(surface_area)
else:
    for pos, air_c in aircubes.items():
        if len(air_c.blocks) == 6:
            surface_area -= 6
            continue

        for c2 in aircubes:
            if air_c is aircubes[c2]:
                continue
            if air_c.is_adjacent(c2):
                air_c.neighbors.add(c2)

    print(surface_area)

# 2430 < x < 3498
