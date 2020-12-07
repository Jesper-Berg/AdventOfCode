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
        for c in 'abcdefghijklmnopqrstuwvxyz':
            if all(c in indiv for indiv in group):
                groupAnswers[k] += c
        k += 1

    totalUnique = 0
    for group in groupAnswers:
        totalUnique += len(group)
print(totalUnique)

