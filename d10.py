with open("d10.txt", "r") as f:
    inp = f.read().split("\n")[:-1]


class Clock:
    cycle = 1


class CPU:
    def __init__(self, clock):
        self.register = 1
        self.clock = clock
        self.in_progress = None
        self.i = 0
        self.check_points = []

    def execute(self, instruction):
        if self.in_progress:
            return

        if instruction == "noop":
            self.i += 1
        else:
            cmd, value = instruction.split(" ")
            self.in_progress = (self.clock.cycle, int(value))

    def next_cycle(self):
        self.clock.cycle += 1
        if self.in_progress and self.clock.cycle - self.in_progress[0] == 2:
            self.register += self.in_progress[1]
            self.i += 1
            self.in_progress = None

        if self.clock.cycle in [20, 60, 100, 140, 180, 220]:
            self.check_points.append(self.get_signal_strength())

    def get_signal_strength(self):
        return self.clock.cycle * self.register


class CRT:
    def __init__(self, clock, cpu):
        self.mtx = []
        for i in range(6):
            self.mtx.append([" "] * 40)

        self.clock = clock
        self.cpu = cpu

    def draw(self):
        sprite_pixels = (
            self.cpu.register - 1,
            self.cpu.register,
            self.cpu.register + 1,
        )

        if (self.clock.cycle - 1) % 40 in sprite_pixels:
            self.mtx[(self.clock.cycle - 1) // 40][(self.clock.cycle - 1) % 40] = "#"


clock = Clock()
cpu = CPU(clock)
crt = CRT(clock, cpu)

while cpu.i < len(inp):
    cpu.execute(inp[cpu.i])
    crt.draw()
    cpu.next_cycle()

print(sum(cpu.check_points))

for row in crt.mtx:
    print("".join(row))
