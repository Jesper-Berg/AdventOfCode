

def getSeat(lower, upper, values):
    if lower == upper:
        return upper
    current = values[0]
    if current == 'F' or current == 'L':
        return getSeat(lower, int((lower + upper)/2), values[1:])
    elif current == 'B' or current == 'R':
        return getSeat(int((lower + upper) / 2) + 1, upper, values[1:])

with open('input.txt') as input:
    allSeats = []
    for ticket in input.readlines():
        ticket = ticket[:-1]
        rowNumber = getSeat(0, 127, ticket[:-3])
        colNumber = getSeat(0, 7, ticket[-3:])
        seatID = rowNumber * 8 + colNumber
        allSeats.append(seatID)
for seat in allSeats:
    if seat + 1 not in allSeats and seat + 2 in allSeats:
        print(seat + 1)