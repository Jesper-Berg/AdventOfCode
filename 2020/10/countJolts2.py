def connectAdapters(currJolt):
    global deviceJoltage
    global joltList
    if currJolt not in joltList:
        return 0
    if currJolt == deviceJoltage:
        return 1 
    return (checkValue(currJolt + 1) 
            + checkValue(currJolt + 2)
            + checkValue(currJolt + 3))

def checkValue(currJolt):
    global wayDict
    if currJolt not in wayDict.keys():
        wayDict[currJolt] = connectAdapters(currJolt)
    return wayDict[currJolt]

joltList = []
wayDict = {}
with open('input.txt') as input:
    for line in input.readlines():
        joltList.append(int(line.strip()))

deviceJoltage = max(joltList) + 3
joltList.append(deviceJoltage)
joltList.append(0)
print(connectAdapters(0))
