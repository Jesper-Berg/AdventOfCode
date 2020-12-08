instructions = []
with open('input.txt') as input:
    for line in input.readlines():
        instructions.append(line.strip())

prevInstructions = []
acc = 0
i = 0
while(i < len(instructions)):
    curr = instructions[i].split()
    if i in prevInstructions:
        print(acc)
        break
    prevInstructions.append(i)
    if curr[0] == 'jmp':
        i += int(curr[1])
    else:
        if curr[0] == 'acc':
            acc += int(curr[1])
        i += 1