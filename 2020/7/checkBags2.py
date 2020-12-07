import re

def findBag(bagRules, current):
    totalCurr = 0
    for inside in bagRules[current]:
        totalCurr += inside[0] + inside[0]*findBag(bagRules, inside[1])
    return totalCurr 
                
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

print(findBag(bagRules, 'shiny gold'))