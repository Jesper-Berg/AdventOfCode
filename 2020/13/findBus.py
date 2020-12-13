buses = []
departTime = 0
with open('input.txt') as input:
    for line in input.readlines():
        splitLine = line.strip().split(',')
        if len(splitLine) == 1:
            departTime = int(splitLine[0])
        else:
            for time in splitLine:
                if time != 'x':
                    buses.append([int(time), 0])

lowest = [0, 9999999999]
for time in buses:
    time[1] = time[0] - departTime % time[0]
    if lowest[1] > time[1]:
        lowest = time
print(lowest[1] * lowest[0])