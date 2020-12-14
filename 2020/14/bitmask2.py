from itertools import permutations, chain
import copy


def addToMem(address, val):
    totalX = 0
    for c in address:
        if c == 'X':
            totalX += 1
    oneList = []
    for i in range(totalX + 1):
        currList = [0] * totalX
        for j in range(i):
            currList[j] = 1
        oneList.append(currList)
    permList = []
    for one in oneList:
        permList.append(list(dict.fromkeys([p for p in permutations(one)])))
    permList = [y for x in permList for y in x]
    for perm in permList:
        permIndex = 0
        currAddress = copy.deepcopy(address)
        for i in range(len(address)):
            if currAddress[i] == 'X':
                currAddress[i] = str(perm[permIndex])
                permIndex += 1
        mem[int(''.join(currAddress),2)] = val


        

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
        num = list('{0:036b}'.format(int(splitLine[0][4:-1])))
        for i in range(len(currentMask)):
            if currentMask[i] != '0':
                num[i] = currentMask[i]
        addToMem(num, int(splitLine[1]))

total = 0
for key in mem.keys():
    total += mem[key]
print(total)
