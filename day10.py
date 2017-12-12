from functools import reduce

def knothash(elements, lengths, repeat=1):
    elements = elements[:]
    skip_size = 0
    index = 0

    for i in range(repeat):
        for length in lengths:
            reversed_part = list(reversed((elements*2)[index:(index+length)]))

            hang = len(reversed_part) - len(elements[index:])
            if hang <= 0:
                elements[index:index+length] = reversed_part
            else:
                elements[index:] = reversed_part[:-hang]
                elements[:hang] = reversed_part[-hang:]
            index = (index + length + skip_size) % len(elements)
            skip_size += 1
    return elements


elements = list(range(256))
lengths = [102,255,99,252,200,24,219,57,103,2,226,254,1,0,69,216]

# part 1
part_1 = knothash(elements, lengths)
print(part_1[0] * part_1[1])

# part 2
lengths = [ord(element) for element in str(lengths)[1:-1] if element != " "] + [17, 31, 73, 47, 23]
elements = knothash(elements, lengths, 64)

hash = list(reduce((lambda x, y: x^y), elements[index:index+16]) for index in range(0, len(elements), 16))
for n in hash:
    print(hex(n)[2:], end="")
print()