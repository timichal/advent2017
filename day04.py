valid_phrases_1 = 0
valid_phrases_2 = 0

with open("day04") as file:
	for line in file:
		phrase = line.strip().split()
		if len(phrase) == len(set(phrase)):
			valid_phrases_1 += 1
		sorted_phrase = [''.join(sorted(list(word))) for word in phrase]
		if len(sorted_phrase) == len(set(sorted_phrase)):
			valid_phrases_2 += 1
	print(valid_phrases_1, valid_phrases_2)