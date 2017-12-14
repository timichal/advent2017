firewall = {}
with open("day13") as file:
    for line in file:
        firewall[int(line.split()[0][:-1])] = (1, int(line.split()[1]))

for position in range(max(firewall)):    
    if position not in firewall:
        firewall[position] = 0

def movelayer(layer, steps):
    pos = steps % (layer[1]*2-2)
    if pos < layer[1]:
        layer = (layer[0] + pos, layer[1])
    elif pos >= layer[1]:
        layer = (layer[1] - (pos - (layer[1] - 1)), layer[1])        
    return layer

# part 1
severity = 0
for i, layer in firewall.items():
    if layer != 0:
        layer = movelayer(layer, i)
        if layer[0] == 1:
                severity += i*layer[1]
print("Part 1: severity " + str(severity))

# part 2
i = 0
while True:
    passed = True
    for j, layer in firewall.items():
        if layer != 0:
            if movelayer(layer, i+j)[0] == 1:
                passed = False
                break
    if passed:
        print("Part 2: " + str(i))
        break
    i += 1