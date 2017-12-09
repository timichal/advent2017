from collections import Counter

class Node(object):
	def __init__(self, name, weight, children):
		self.name = name
		self.weight = weight
		self.children = children
		self.parent = None
		
	def total_weight(node):
		if node.children == []:
			return node.weight
		else:
			part = 0
			for child in node.children:
				part += nodes[child].total_weight()
			return node.weight + part

nodes = {}
with open("day07") as file:
	for line in file:
		line = line.split()
		nodes[line[0]] = Node(name=line[0], weight=int(line[1][1:-1]), children=[entry.replace(",", "") for entry in line[3:]])


for unsorted_node in nodes.values():
	for node in nodes.values():
		if unsorted_node.name in node.children:
			unsorted_node.parent = node.name

for node in nodes.values():
	if node.parent == None:
		root = node.name
		print("Part 1: " + root)

while True:
	try:
		odd_weight = Counter(nodes[child].total_weight() for child in nodes[root].children).most_common()[1][0]
	except:
		print("Part 2:", nodes[root].weight - (odd_weight - Counter(nodes[child].total_weight() for child in nodes[nodes[root].parent].children).most_common()[0][0]))
		break
	for child in nodes[root].children:
		if nodes[child].total_weight() == odd_weight:
			root = child