with open('input.txt') as input:
    passList = []
    necValues = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    i = 0
    totalValid = 0
    for line in input.readlines():
        if line == '\n':
            i += 1
        else:
            if i == len(passList):
                passList.append({})
            lineSplit = line.split(' ')
            for entry in lineSplit:
                entrySplit = entry.split(':')
                if '\n' in entrySplit[1]:
                    entrySplit[1] = entrySplit[1][:-1]
                passList[i][entrySplit[0]] = entrySplit[1]
    for indivPass in passList:
        valid = True
        for value in necValues:
            if value not in list(indivPass.keys()):
                valid = False
                break
            else:
                passVal = indivPass[value]
                if value == 'byr':
                    if int(passVal) < 1920 or int(passVal) > 2002:
                        valid = False
                        break
                elif value == 'iyr':
                    if int(passVal) < 2010 or int(passVal) > 2020:
                        valid = False
                        break
                elif value == 'eyr':
                    if int(passVal) < 2020 or int(passVal) > 2030:
                        valid = False
                        break
                elif value == 'hgt':
                    if passVal[-2:] == 'cm':
                        if int(passVal[:-2]) < 150 or int(passVal[:-2]) > 193:
                            valid = False
                            break
                    elif passVal[-2:] == 'in':
                        if int(passVal[:-2]) < 59 or int(passVal[:-2]) > 76:
                            valid = False
                            break
                    else:
                        valid = False
                        break
                elif value == 'hcl':
                    if passVal[0] != '#':
                        valid = False
                        break
                    elif len(passVal[1:]) != 6:
                        valid = False
                        break
                    else:
                        for c in passVal[1:]:
                            if c not in 'abcdef0123456789':
                                valid = False
                                break
                        if not valid:
                            break
                elif value == 'ecl':
                    eyeVals = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                    if passVal not in eyeVals:
                        valid = False
                        break
                elif value == 'pid':
                    if len(passVal) != 9:
                        valid = False
                        break
                    else:
                        for c in passVal:
                            if c not in '0123456789':
                                valid = False
                                break
                        if not valid:
                            break
        if valid:
            totalValid +=1
    print(totalValid)
