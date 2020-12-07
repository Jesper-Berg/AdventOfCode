with open('input.txt') as input:
    totalValid = 0
    for line in input:
        splitLine = line.split(' ')
        positions = splitLine[0].split('-')
        lowerPosition = int(positions[0])
        upperPosition = int(positions[1])
        letter = splitLine[1][0]
        password = splitLine[-1][:-1]
        if (password[lowerPosition - 1] == letter) ^ (password[upperPosition - 1] == letter):
            totalValid += 1
    print(totalValid)
    