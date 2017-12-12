# this solution doesn't work for e.g. se,ne,se; cba though
with open("day11") as file:
    dirs = file.readline().split(",")
pos = {"x": 0, "y": 0}

furthest = 0
for dir in dirs:
    if dir == "ne":
        pos["x"] += 1
        pos["y"] += 1
    if dir == "nw":
        pos["x"] -= 1
        pos["y"] += 1
    if dir == "se":
        pos["x"] += 1
        pos["y"] -= 1
    if dir == "sw":
        pos["x"] -= 1
        pos["y"] -= 1        
    if dir == "s":
        pos["y"] -= 2
    if dir == "n":
        pos["y"] += 2
    furthest = max((abs(pos["x"]) + abs(pos["y"])), furthest)
print("Part 1:", (abs(pos["x"]) + abs(pos["y"]))//2, "\nPart 2:", furthest//2)