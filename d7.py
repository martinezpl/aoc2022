import sys

with open("d7.txt", "r") as f:
    inp = f.read().split("\n")[:-1]


class Dir:
    def __init__(self, name, parent=None):
        self.files = {}
        self.directories = {}
        self.name = name
        self.parent = parent

    def add_file(self, name, size):
        if name not in self.files:
            self.files[name] = size

    def add_directory(self, obj):
        if obj.name not in self.directories:
            self.directories[obj.name] = obj

    def get_total_size(self, tracker=None, condition=None):
        ts = 0
        for f in self.files:
            ts += self.files[f]
        for dir in self.directories:
            ts += self.directories[dir].get_total_size(tracker, condition)
        if tracker != None and condition(ts):
            tracker.append(ts)
        return ts


main_dir = Dir("/", None)
current_dir = main_dir
for l in inp:
    if l.startswith("$ ls"):
        continue

    dir_name = l.split(" ")[-1]
    if l.startswith("$ cd"):
        if dir_name == "..":
            current_dir = current_dir.parent
        else:
            if dir_name in current_dir.directories:
                current_dir = current_dir.directories[dir_name]
        continue

    if l[:3] == "dir":
        current_dir.add_directory(Dir(dir_name, current_dir))
    else:
        size, name = l.split(" ")
        current_dir.add_file(name, int(size))


size_above_100000 = []

max_size = 70000000
size_necessary = 30000000
total_size = main_dir.get_total_size(size_above_100000, lambda x: x <= 100000)

dirs_to_remove = []
main_dir.get_total_size(
    dirs_to_remove, lambda x: max_size - (total_size - x) >= size_necessary
)

# PART1
print(sum(size_above_100000))

# PART2
print(min(dirs_to_remove))
