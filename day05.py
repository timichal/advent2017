with open("day05") as file:
	maze = [int(line.strip()) for line in file]

# part 2; only the else: for part 1
steps = 0
i = 0
while i < len(maze):
	steps += 1
	if maze[i] >= 3:
		maze[i] -= 1
		i += maze[i] + 1
	else:
		maze[i] += 1
		i += maze[i] - 1
print(steps) 