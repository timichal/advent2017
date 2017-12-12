from collections import defaultdict
register = defaultdict(int)

max_overall = 0
with open("day08") as file:
    for line in file:
        instruction = line.split("if")
        operation = instruction[0].split()
        condition = instruction[1].split()
        if eval("register['" + condition[0] + "']" + condition[1] + condition[2]):
            if operation[1] == "inc":
                register[operation[0]] += int(operation[2])
            elif operation[1] == "dec":
                register[operation[0]] -= int(operation[2])
        max_overall = max(max_overall, register[operation[0]])

#part 1
print(max(register.values()))

#part 2
print(max_overall)