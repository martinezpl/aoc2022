with open("d11.txt", "r") as f:
    inp = f.read().split("\n\n")

print(inp)

PART = 2

CYCLE_LENGTH = 13 * 11 * 5 * 2 * 3 * 7 * 17 * 19

print(CYCLE_LENGTH)


class Monkey:
    def __init__(self, items, op, test_div, true_m, false_m, gang):
        self.items = [int(it) for it in items]
        self.op = op
        self.test_div = int(test_div)
        self.true_m = int(true_m)
        self.false_m = int(false_m)
        self.gang = gang

        self.items_inspected = 0

    def throw(self):
        while (len(self.items)) > 0:
            it = self.items.pop(0)
            self.items_inspected += 1
            # print("  Monkey inspects item with a worry level of", it)
            it = self.op(it)
            # print(" .  Worry level increases to", it)
            if PART == 1:
                it = it // 3
                print(" .  Monke bored, worry divided by 3 to", it)
            else:
                it = it % CYCLE_LENGTH
            if it % self.test_div == 0:
                # print(
                #     f" .  Item divisible by {self.test_div}, thrown to monkey",
                #     self.true_m,
                # )
                self.gang[self.true_m].catch(it)
            else:
                # print(
                #     f" .  Item not divisible by {self.test_div}, thrown to monkey",
                #     self.false_m,
                # )
                self.gang[self.false_m].catch(it)

    def catch(self, it):
        self.items.append(it)


monkeys = []
for monkey_data in inp:
    lines = monkey_data.split("\n")
    op_lambda = None
    exec("op_lambda = lambda old: " + lines[2].split("= ")[1])
    monkeys.append(
        Monkey(
            items=lines[1].split(": ")[1].split(","),
            op=op_lambda,
            test_div=lines[3].split(" ")[-1],
            true_m=lines[4].split(" ")[-1],
            false_m=lines[5].split(" ")[-1],
            gang=monkeys,
        )
    )

round = 1
while round <= 10_000:
    print(round)
    for i, m in enumerate(monkeys):
        # print(f"Monkey {i}:")
        m.throw()
    round += 1

counts = [m.items_inspected for m in monkeys]
counts.sort(reverse=True)
print(counts)
print(counts[0] * counts[1])
