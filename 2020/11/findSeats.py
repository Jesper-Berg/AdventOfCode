import copy

def prettyfy(seats):
    for row in seats:
        print(''.join(row))
    print('\n')

def walk(row, col, rW, cW, seats):
    origrW = rW
    origcW = cW
    if (row + rW > len(seats) - 1 or
            row + rW < 0 or
            col + cW > len(seats[0]) - 1 or
            col + cW < 0):
        return 0
    while(seats[row + rW][col + cW] == '.'):
        rW += origrW
        cW += origcW
        if (row + rW > len(seats) - 1 or
            row + rW < 0 or
            col + cW > len(seats[0]) - 1 or
            col + cW < 0):
            return 0
    if seats[row + rW][col + cW] == 'L':
        return 0
    elif seats[row + rW][col + cW] == '#':
        return 1
    else:
        print('SOMETHING WENT WRONG!!')
        return 99999999

def neighbours2(row, col, seats):
    nei = 0
    nei += walk(row, col, 1, 0, seats)
    nei += walk(row, col, 1, 1, seats)
    nei += walk(row, col, 1, -1, seats)
    nei += walk(row, col, -1, 0, seats)
    nei += walk(row, col, -1, 1, seats)
    nei += walk(row, col, -1, -1, seats)
    nei += walk(row, col, 0, 1, seats)
    nei += walk(row, col, 0, -1, seats)
    return nei

def neighbours(row, col, seats):
    nei = 0
    if row + 1 < len(seats):
        if seats[row + 1][col] == '#':
            nei += 1
        if col + 1 < len(seats[0]):
            if seats[row + 1][col + 1] == '#':
                nei += 1 
        if col - 1 > -1:
            if seats[row + 1][col - 1] == '#':
                nei += 1 
    if row - 1 > -1:
        if seats[row - 1][col] == '#':
            nei += 1 
        if col + 1 < len(seats[0]):
            if seats[row - 1][col + 1] == '#':
                nei += 1 
        if col - 1 > -1:
            if seats[row - 1][col - 1] == '#':
                nei += 1 
    if col + 1 < len(seats[0]):
        if seats[row][col + 1] == '#':
            nei += 1
    if col - 1 > -1:
        if seats[row][col - 1] == '#':
            nei += 1
    return nei

seats = []
with open('input.txt') as input:
    for line in input.readlines():
        seats.append([])
        for c in line.strip():
            seats[-1].append(c)

newSeats = []
while(seats != newSeats):
    if len(newSeats) != 0:
        seats = copy.deepcopy(newSeats)
    newSeats = copy.deepcopy(seats)
    for row in range(len(seats)):
        for col in range(len(seats[row])):
            if seats[row][col] != '.':
                nei = neighbours2(row, col, seats)
                if nei == 0:
                    newSeats[row][col] = '#'
                elif nei >= 5:
                    newSeats[row][col] = 'L'

count = 0
for row in seats:
    for col in row:
        if col == '#':
            count += 1
print(count)