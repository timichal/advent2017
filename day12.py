rels = []
with open("day12") as file:
    for line in file:
        rels.append([line.strip().split(" <-> ")[0], line.strip().split(" <-> ")[1].split(", ")])

def findgroup(programs, rels):
    for program in programs:
        for rel in rels:
            if program in rel[1] and rel[0] not in programs:
                programs.append(rel[0])
    return programs

#part 1
print(len(findgroup(["0"], rels)))

#part 2
found = []
groups = 0
for rel in rels:
    if rel[0] not in found:
        programs = findgroup([rel[0]], rels)
        groups += 1
        found.extend(programs)
print(groups)