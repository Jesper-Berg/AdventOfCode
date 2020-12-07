with open('input.txt') as input:
    i = 0
    indivAnswers = []
    for line in input.readlines():
            if line == '\n':
                i += 1
            else:
                if i == len(indivAnswers):
                    indivAnswers.append([])
                indivAnswers[i].append(line.strip())
    groupAnswers = []
    for k in range(len(indivAnswers)):
        groupAnswers.append('')
    k = 0
    for group in indivAnswers:
        for indiv in group:
            for c in indiv:
                if c not in groupAnswers[k]:
                    groupAnswers[k] += c
        k += 1

    totalUnique = 0
    for group in groupAnswers:
        totalUnique += len(group)
print(totalUnique)

