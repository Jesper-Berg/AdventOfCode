buses = []
with open('input.txt') as input:
    for line in input.readlines():
        splitLine = line.strip().split(',')
        if len(splitLine) != 1:
            for i in range(len(splitLine)):
                if splitLine[i] != 'x':
                    buses.append((int(splitLine[i]), i))

current = 0
interval = buses[0][0]
for bus in buses[1:]:
    while (current + bus[1]) % bus[0] != 0:
        current += interval
    interval *= bus[0]

print(current)