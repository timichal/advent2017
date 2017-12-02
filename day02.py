numbers = []
with open("day02") as file:
	for line in file:
		numbers.append([int(x) for x in line.strip().split()])

# part 1
print(sum([int(max(row)) - int(min(row)) for row in numbers]))

# part 2
result = 0
for row in numbers:
	for number in row:
		for number2 in row:
			if number % number2 == 0 and number/number2 > 1:
				result += int(number/number2)
print(result)