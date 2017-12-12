with open("day09") as file:
    stream = file.readline()
garbage = False
ignorenext = False
grp = 0
grp_depth = 0
garbage_count = 0
for char in stream:
        if garbage == True and char != "!" and char != ">" and not ignorenext:
            garbage_count += 1
        if ignorenext:
            ignorenext = False
        elif char == "<":
            garbage = True
        elif char == ">":
            garbage = False
        elif garbage == True and char == "!":
            ignorenext = True
        elif char == "{" and garbage == False:
            grp_depth += 1
        elif char == "}" and garbage == False:
            grp += grp_depth
            grp_depth -= 1
# Part 1
print(grp)

# Part 2
print(garbage_count)