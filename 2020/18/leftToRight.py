import re

def handleExpression(expr):
    exprSplit = expr.split(' ')
    if len(exprSplit) == 3:
        return eval(expr)

    while '(' in expr:
        parens = re.compile(r'\(([^()]*)\)').findall(expr)
        for par in parens:
            expr = expr.replace(f'({par})', str(handleExpression(par)))
    while '+' in expr:
        adds = re.compile(r'[^* ]+ \+ [^* ]+').findall(expr)
        if adds[0]:
            add = adds[0]
            expr = expr.replace(add, str(handleExpression(add)))
    exprSplit = expr.split(' ')

    if len(exprSplit) == 1:
        return expr
    return handleExpression(str(handleExpression(' '.join(exprSplit[:-2]))) + ' ' + ' '.join(exprSplit[-2:]))

total = 0
with open('input.txt') as input:
    for line in input.readlines():
        total += int(handleExpression(line.strip()))
print(total)

#print(handleExpression('9 + 8 + 7 + 7 + 12 * 5'))