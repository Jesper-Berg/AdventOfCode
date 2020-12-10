def connectAdapters(currJolt, joltList):
    global oneDiff, twoDiff, threeDiff
    if currJolt not in joltList:
        return False
    joltList.remove(currJolt)
    if len(joltList) == 0:
        return True
    if connectAdapters(currJolt + 1, joltList):
        oneDiff += 1
        return True
    elif connectAdapters(currJolt + 2, joltList):
        twoDiff += 1
        return True
    elif connectAdapters(currJolt + 3, joltList):
        threeDiff += 1
        return True
    return False


joltList = []
with open('input.txt') as input:
    for line in input.readlines():
        joltList.append(int(line.strip()))

deviceJoltage = max(joltList) + 3
joltList.append(deviceJoltage)
joltList.append(0)
oneDiff = 0
twoDiff = 0
threeDiff = 0
if(connectAdapters(0, joltList)):
    print(oneDiff*threeDiff)
else:
    print('REE')
