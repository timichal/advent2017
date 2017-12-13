inp = {}
with open("day13") as file:
    for line in file:
        inp[int(line.split()[0][:-1])] = int(line.split()[1])

deffirewall = {}
for size in range(max(inp)+1):
    if size in inp:
        # pos, length
        deffirewall[size] = (1, inp[size])
    else:
        deffirewall[size] = 0

def move(firewall, steps):
    for i, layer in firewall.items():
        if layer != 0:
            pos = steps % (layer[1]*2-2)
            if pos < layer[1]:
                firewall[i] = (layer[0] + pos, layer[1])
            elif pos >= layer[1]:
                firewall[i] = (layer[1] - (pos - (layer[1] - 1)), layer[1])
    return firewall

i=0
while True:
        severity = 0
        passed = True
        for j in range(len(deffirewall)):
            firewall = move(deffirewall.copy(), i+j)
            if firewall[j] != 0:
                if firewall[j][0] == 1:
                    passed = False
                    if i == 0:
                        severity += j*firewall[j][1]
                    else:
                        break
                    
        
        if i == 0:
            print("Part 1: severity " + str(severity))
            pass
        

        if passed:
            print("Part 2: " + str(i))
            break
        i+=1