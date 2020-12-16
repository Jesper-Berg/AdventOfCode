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

totalInvalid = 0
for ticket in otherTickets:
    for invNum in invalidNums:
        if invNum in ticket:
            totalInvalid += invNum

print(totalInvalid)