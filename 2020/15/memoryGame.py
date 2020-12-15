numList = []
prev = {}
with open('input.txt') as input:
    for line in input.readlines():
        splitList = line.strip().split(',')
        for i in range(len(splitList)):
            numList.append(int(splitList[i]))
            prev[int(splitList[i])] = i

# Change 30000000 for 2020 to get first
for i in range(len(numList) - 1, 30000000 - 1):
    prevNum = numList[i]
    if prevNum in prev.keys():
        numList.append(i - prev[prevNum])
    else:
        numList.append(0)
    prev[prevNum] = i

print(numList[-1])