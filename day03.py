def init_grid(size):
	return [[0] * size for i in range(size)] 

# part 1
def fill_grid_part1(target):
	size = round(target**0.5)
	grid = init_grid(size)
	pos = [int(size/2), int(size/2)]
	center = pos
	number = 1
	grid[pos[0]][pos[1]] = number
	# right 1, up 1, left 2, down 2, right 3, up 3...
	counter = 1
	# 1: right, 2: up, 3: left, 4: down, 5: right...
	direction = 1
	while True:
		for times in range(counter):
			number += 1
			if direction % 4 == 1: pos = [pos[0], pos[1]+1]
			elif direction % 4 == 2: pos = [pos[0]-1, pos[1]]
			elif direction % 4 == 3: pos = [pos[0], pos[1]-1]
			elif direction % 4 == 0: pos = [pos[0]+1, pos[1]]

			grid[pos[0]][pos[1]] = number
			if number == target:
				return abs(pos[0]-center[0]) + abs(pos[1]-center[0])

		if direction % 2 == 0: counter += 1
		direction += 1

# part 2
def fill_grid_part2(size, target):
	def getvalue(pos):
		return grid[pos[0]+1][pos[1]] +\
			   grid[pos[0]-1][pos[1]] +\
			   grid[pos[0]][pos[1]+1] +\
			   grid[pos[0]][pos[1]-1] +\
			   grid[pos[0]+1][pos[1]+1] +\
			   grid[pos[0]+1][pos[1]-1] +\
			   grid[pos[0]-1][pos[1]+1] +\
			   grid[pos[0]-1][pos[1]-1]

	grid = init_grid(size)
	pos = [int(size/2), int(size/2)]
	center = pos
	grid[pos[0]][pos[1]] = 1
	# right 1, up 1, left 2, down 2, right 3, up 3...
	counter = 1
	# 1: right, 2: up, 3: left, 4: down, 5: right...
	direction = 1
	while True:
		for times in range(counter):
			if direction % 4 == 1: pos = [pos[0], pos[1]+1]
			elif direction % 4 == 2: pos = [pos[0]-1, pos[1]]
			elif direction % 4 == 3: pos = [pos[0], pos[1]-1]
			elif direction % 4 == 0: pos = [pos[0]+1, pos[1]]

			if getvalue(pos) > target: return getvalue(pos)
			grid[pos[0]][pos[1]] = getvalue(pos)	
			
		if direction % 2 == 0: counter += 1
		direction += 1

n = 312051
print("Part 1:", fill_grid_part1(n))
print("Part 2:", fill_grid_part2(11,n))