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
        print(output[i + 25])
