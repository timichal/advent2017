with open("day06") as file:
	state = [int(n) for n in file.read().strip().split()]

states = []
while True:
	selected = max(state)
	selidx = state.index(selected)
	state[selidx] = 0
	for i in range(selected):
		selidx += 1
		state[selidx % len(state)] += 1
	if state in states: 
		part2 = states.index(state)
		break
	states.append(state[:])
print(len(states)+1, len(states)-part2)