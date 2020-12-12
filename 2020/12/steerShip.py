instructions = []
with open('input.txt') as input:
    for line in input.readlines():
        instructions.append((line.strip()[0], int((line.strip()[1:]))))

x = 0
y = 0
angle = 0
for ins in instructions:
    if ins[0] == 'N':
        y += ins[1]
    elif ins[0] == 'S':
        y -= ins[1]
    elif ins[0] == 'E':
        x += ins[1]
    elif ins[0] == 'W':
        x -= ins[1]
    elif ins[0] == 'R':
        angle = (angle - ins[1]) % 360
    elif ins[0] == 'L':
        angle = (angle + ins[1]) % 360
    elif ins[0] == 'F':
        if angle == 0:
            x += ins[1]
        elif angle == 90:
            y += ins[1]
        elif angle == 180:
            x -= ins[1]
        elif angle == 270:
            y -= ins[1]
        else:
            print('ANGLE IS NOT STRAIGHT!')    
    else:
        print('SOMETHING IS WROOONG')

print(abs(x) + abs(y))
