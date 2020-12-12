instructions = []
with open('input.txt') as input:
    for line in input.readlines():
        instructions.append((line.strip()[0], int((line.strip()[1:]))))

wayX = 10
wayY = 1
boatX = 0
boatY = 0
for ins in instructions:
    if ins[0] == 'N':
        wayY += ins[1]
    elif ins[0] == 'S':
        wayY -= ins[1]
    elif ins[0] == 'E':
        wayX += ins[1]
    elif ins[0] == 'W':
        wayX -= ins[1]
    elif ins[0] == 'R':
        for _ in range(int(ins[1] / 90)):
            tempX = wayX
            wayX = wayY
            wayY = -tempX
    elif ins[0] == 'L':
        for _ in range(int(ins[1] / 90)):
            tempX = wayX
            wayX = -wayY
            wayY = tempX
    elif ins[0] == 'F':
        boatX += wayX * ins[1]
        boatY += wayY * ins[1]
    else:
        print('SOMETHING IS WROOONG')

print(abs(boatX) + abs(boatY))
