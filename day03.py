from collections import defaultdict

# part 1
def grid_part1(target):
	grid = {}
	pos = [0, 0]
	number = 1
	grid[(0,0)] = number
	# right 1, up 1, left 2, down 2, right 3, up 3...
	counter = 1
	# 1: right, 2: up, 3: left, 4: down, 5: right...
	direction = 1
	while True:
		for times in range(counter):
			number += 1
			if direction % 4 == 1: pos[1] += 1
			elif direction % 4 == 2: pos[0] -= 1
			elif direction % 4 == 3: pos[1] -= 1
			elif direction % 4 == 0: pos[0] += 1

			grid[(pos[0], pos[1])] = number
			if number == target:
				return abs(pos[0]) + abs(pos[1])

		if direction % 2 == 0: counter += 1
		direction += 1

# part 2
def grid_part2(target):
	def getvalue(pos):
		return grid[(pos[0]+1, pos[1])] +\
			   grid[(pos[0]-1, pos[1])] +\
			   grid[(pos[0], pos[1]+1)] +\
			   grid[(pos[0], pos[1]-1)] +\
			   grid[(pos[0]+1, pos[1]+1)] +\
			   grid[(pos[0]+1, pos[1]-1)] +\
			   grid[(pos[0]-1, pos[1]+1)] +\
			   grid[(pos[0]-1, pos[1]-1)]

	grid = defaultdict(int)
	pos = [0, 0]
	grid[(0, 0)] = 1
	# right 1, up 1, left 2, down 2, right 3, up 3...
	counter = 1
	# 1: right, 2: up, 3: left, 4: down, 5: right...
	direction = 1
	while True:
		for times in range(counter):
			if direction % 4 == 1: pos[1] += 1
			elif direction % 4 == 2: pos[0] -= 1
			elif direction % 4 == 3: pos[1] -= 1
			elif direction % 4 == 0: pos[0] += 1

			if getvalue(pos) > target: return getvalue(pos)
			grid[(pos[0],pos[1])] = getvalue(pos)	

		if direction % 2 == 0: counter += 1
		direction += 1

n = 312051
print("Part 1:", grid_part1(n))
print("Part 2:", grid_part2(n))