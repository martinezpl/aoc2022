with open("d19.txt", "r") as f:
    inp = f.read().split("\n")[:-1]

import re
from dataclasses import dataclass
from collections import deque


@dataclass
class Blueprint:
    id: int
    ore_robot_cost: int
    clay_robot_cost: int
    obsidian_robot_cost: tuple[int, int]  # ore, clay
    geode_robot_cost: tuple[int, int]  # ore, obsidian


class Resources:
    ore = 0
    clay = 0
    obsidian = 0
    geodes = 0


class State:
    def __init__(self, blueprint):
        self.ore_robots = 1
        self.clay_robots = 0
        self.obsidian_robots = 0
        self.geode_robots = 0

        self.resources = Resources()
        self.factory = Factory(self, blueprint, self.resources)

    def dig(self):
        self.resources.ore += self.ore_robots
        self.resources.clay += self.clay_robots
        self.resources.obsidian += self.obsidian_robots
        self.resources.geodes += self.geode_robots
        print(f"{self.ore_robots} ore robots collect.")
        print(f"{self.clay_robots} clay robots collect.")
        print(f"{self.obsidian_robots} obsidian robots collect.")
        print(f"{self.geode_robots} geode robots collect.")
        print(vars(self.resources))

    def tick(self):
        self.factory.prod_check()
        self.dig()
        self.factory.create()


class Factory:
    def __init__(self, state, blueprint, resources):
        self.state: State = state
        self.bl: Blueprint = blueprint
        self.rsc: Resources = resources
        self.queue = deque([])

    def prod_check(self):
        if (
            self.rsc.ore >= self.bl.geode_robot_cost[0]
            and self.rsc.obsidian >= self.bl.geode_robot_cost[1]
        ):
            print(
                f"Spend {self.bl.geode_robot_cost[0]} ore and {self.bl.geode_robot_cost[1]} obsidian to build geode robot."
            )
            self.queue.append("gr")

        if (
            self.rsc.ore >= self.bl.obsidian_robot_cost[0]
            and self.rsc.clay >= self.bl.obsidian_robot_cost[1]
        ):
            print(
                f"Spend {self.bl.obsidian_robot_cost[0]} ore and {self.bl.obsidian_robot_cost[1]} clay to build obsidian robot."
            )
            self.queue.append("obr")

        if self.rsc.ore >= self.bl.clay_robot_cost:
            print(f"Spend {self.bl.clay_robot_cost} clay to build clay robot.")
            self.queue.append("cr")

        # if self.rsc.ore >= self.bl.ore_robot_cost:
        #     self.queue.append("or")

    def create(self):
        if self.queue:
            t = self.queue.popleft()

            match t:
                case "or":
                    self.state.ore_robots += 1
                case "cr":
                    self.state.clay_robots += 1
                case "obr":
                    self.state.obsidian_robots += 1
                case "gr":
                    self.state.geode_robots += 1

            print(f"New {t} robot is ready.")


blueprints = []
for i in inp:
    m = re.match(r".+\s(\d+).+\s(\d+).+\s(\d+).+\s(\d+).+\s(\d+).+\s(\d+).+\s(\d+)", i)
    print(m.groups())
    a, b, c, d, e, f, g = list(map(int, m.groups()))
    blueprints.append(Blueprint(a, b, c, (d, e), (f, g)))

table = {}
for b in blueprints:
    s = State(b)
    for i in range(1, 25):
        print(f"== Minute {i} ==")
        s.tick()

    table[b.id] = s.resources.geodes

print(table)
