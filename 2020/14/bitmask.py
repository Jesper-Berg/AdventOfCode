instructions = []
with open('input.txt') as input:
    for line in input.readlines():
        instructions.append(line.strip())

mem = {}
currentMask = []
for line in instructions:
    splitLine = line.split(' = ')
    if splitLine[0] == 'mask':
        currentMask = list(splitLine[1])
    else:
        num = list('{0:036b}'.format(int(splitLine[1])))
        for i in range(len(currentMask)):
            if currentMask[i] != 'X':
                num[i] = currentMask[i]
        address = splitLine[0][4:-1]
        mem[address] = int(''.join(num), 2)

total = 0
for key in mem.keys():
    total += mem[key]
print(total)