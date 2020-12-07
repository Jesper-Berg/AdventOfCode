import re

def findBag(bagRules, current, find):
    bagList = []
    for inside in bagRules[current]:
        bagList.append(inside[1])
    if find in bagList:
        return 1
    else:
        for bag in bagList:
            if findBag(bagRules, bag, find):
                return 1
        return 0
                
with open('input.txt') as input:
    bagRules = {}
    for line in input.readlines():
        result = re.search(r'(.*) bags contain (.*[^,|.])\.', line)
        secondSplit = result.group(2).split()
        bagRules[result.group(1)] = []
        i = 0
        while(i < len(secondSplit)):
            if secondSplit[i] != 'no':
                bagRules[result.group(1)].append((int(secondSplit[i]), secondSplit[i + 1] + " " +  secondSplit[i + 2]))
            i = i + 4    

total = 0
for bag in bagRules.keys():
    total += findBag(bagRules, bag, 'shiny gold')
print(total)