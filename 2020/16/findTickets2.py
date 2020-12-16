import copy

rules = {}
yourTicket = []
otherTickets = []
with open('input.txt') as input:
    section = 0
    for line in input.readlines():
        if section == 0:
            if line != '\n':
                splitLine = line.strip().split(':')
                bounds = splitLine[1].strip().split(' or ')
                ruleName = splitLine[0]
                rules[ruleName] = []
                for bound in bounds:
                    splitBounds = bound.split('-')
                    rules[ruleName].append((int(splitBounds[0]), int(splitBounds[1])))
            else:
                section += 1
        elif section == 1:
            if line != '\n':
                if len(line.split(',')) > 1:
                    yourTicket =  list(map(int, line.strip().split(',')))
            else:
                section += 1
        else:
            if len(line.split(',')) > 1:
                otherTickets.append(list(map(int, line.strip().split(','))))

invalidNums = list(range(1, 1000))
for num in range(1, 1000):
    for rule in rules.keys():
        if (rules[rule][0][0] <= num <= rules[rule][0][1] or
            rules[rule][1][0] <= num <= rules[rule][1][1]):
            invalidNums.remove(num)
            break

fixedTickets = copy.deepcopy(otherTickets)
for ticket in otherTickets:
    for invNum in invalidNums:
        if invNum in ticket:
            fixedTickets.remove(ticket)

fieldList = []
usedFields = []
for i in range(len(fixedTickets[0])):
    fields = list(rules.keys())
    for ticket in fixedTickets:
        for rule in rules.keys():
            if not (rules[rule][0][0] <= ticket[i] <= rules[rule][0][1] or
                rules[rule][1][0] <= ticket[i] <= rules[rule][1][1]):
                fields.remove(rule) if rule in fields else fields
                break
    fieldList.append(fields)

while(len([full for full in fieldList if len(full) > 1]) > 1):
    for possible in fieldList:
        if len(possible) == 1:
            remField = possible[0]
            for field in fieldList:
                if len(field) > 1:
                    field.remove(remField) if remField in field else field

fieldList = [field for sublist in fieldList for field in sublist]

totalProd = 1
for i in range(len(fieldList)):
    if 'departure' in fieldList[i]:
        totalProd *= yourTicket[i]

print(totalProd)
