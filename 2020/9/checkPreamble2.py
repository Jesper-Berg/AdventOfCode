output = []
with open('input.txt') as input:
    for line in input.readlines():
        output.append(int(line.strip()))

for i in range(len(output) - 25):
    preamble = output[i:i+25]
    found = False
    for first in preamble:
        for second in preamble:
            if first != second:
                if first + second == output[i + 25]:
                    found = True
    if not found:
        weakness = output[i+25]

for i in range(len(output) - 1):
    conList = []
    first = output[i]
    conList.append(first)
    sum = first
    for j in range(i + 1, len(output) - 1):
        last = output[j]
        conList.append(last)
        sum += last
        if sum == weakness:
            print(f'max: {max(conList)}, min: {min(conList)}')
            print(max(conList) + min(conList))
