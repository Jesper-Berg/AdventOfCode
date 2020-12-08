instructions = []
with open('input.txt') as input:
    for line in input.readlines():
        instructions.append(line.strip())

for index, ins in enumerate(instructions):
    if ins[:3] != 'acc':
        tempIns = ins
        if ins[:3] == 'nop':
            ins = 'jmp' + ins[3:]
            instructions[index] = ins
        else:
            ins = 'nop' + ins[3:]
            instructions[index] = ins
        prevInstructions = []
        acc = 0
        i = 0
        while(i < len(instructions)):
            curr = instructions[i].split()
            if i in prevInstructions:
                break
            prevInstructions.append(i)
            if curr[0] == 'jmp':
                i += int(curr[1])
            else:
                if curr[0] == 'acc':
                    acc += int(curr[1])
                i += 1
        if i == len(instructions):        
            print(f'finished: {acc}')
            break
        instructions[index] = tempIns