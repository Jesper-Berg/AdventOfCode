from itertools import permutations
import copy


def walk(x, y, z, dx, dy, dz, space):
    try:
        if space[(x + dx, y + dy, z + dz)] == '.':
            return 0
        elif space[(x + dx, y + dy, z + dz)] == '#':
            return 1
        else:
            print('SOMETHING WENT WRONG!!')
            return 99999999
    except KeyError:
        return 0


def neighbours(x, y, z, space):
    nei = 0
    for dx, dy, dz in perms:
        nei += walk(x, y, z, dx, dy, dz, space)
    return nei


space = {}
with open('input.txt') as input:
    z = 0
    y = 0
    x = 0
    for line in input.readlines():
        for c in line.strip():
            space[(x, y, z)] = c
            x += 1
        y += 1
        x = 0

perms = []
deltas = [[1, 1, 1], [-1, -1, -1], [0, 0, 1], [0, 0, -1], [0, 1, 1],
            [0, -1, 1], [0, -1, -1], [-1, -1, 1], [-1, 1, 1]]

for d in deltas:
    perms.extend(permutations(d))
perms = list(dict.fromkeys(perms))

for _ in range(6):
    mini = (min([x for (x, _, _) in space.keys()]),
            min([y for (_, y, _) in space.keys()]),
            min([z for (_, _, z) in space.keys()]))

    maxi = (max([x for (x, _, _) in space.keys()]),
            max([y for (_, y, _) in space.keys()]),
            max([z for (_, _, z) in space.keys()]))

    coords = []
    preCoords = list(space.keys())
    coords.extend(([(mini[0] - 1, y, z) for (x, y, z) in preCoords + coords]))
    coords.extend(([(maxi[0] + 1, y, z) for (x, y, z) in preCoords + coords]))
    coords.extend(([(x, mini[1] - 1, z) for (x, y, z) in preCoords + coords]))
    coords.extend(([(x, maxi[1] + 1, z) for (x, y, z) in preCoords + coords]))
    coords.extend(([(x, y, mini[2] - 1) for (x, y, z) in preCoords + coords]))
    coords.extend(([(x, y, maxi[2] + 1) for (x, y, z) in preCoords + coords]))
    coords.append((mini[0] - 1, mini[1] - 1, mini[2] - 1))
    coords.append((maxi[0] + 1, mini[1] - 1, mini[2] - 1))
    coords.append((mini[0] - 1, maxi[1] + 1, mini[2] - 1))
    coords.append((maxi[0] + 1, maxi[1] + 1, mini[2] - 1))
    coords.append((mini[0] - 1, mini[1] - 1, maxi[2] + 1))
    coords.append((maxi[0] + 1, mini[1] - 1, maxi[2] + 1))
    coords.append((mini[0] - 1, maxi[1] + 1, maxi[2] + 1))
    coords.append((maxi[0] + 1, maxi[1] + 1, maxi[2] + 1))
    for coord in coords:
        space[coord] = '.'

    newSpace = copy.deepcopy(space)

    for coord in space.keys():
        nei = neighbours(coord[0], coord[1], coord[2], space)
        if nei != 3:
            if nei != 2:
                newSpace[coord] = '.'
        else:
            newSpace[coord] = '#'
    space = newSpace

total = 0
for key in space.keys():
    if space[key] == '#':
        total += 1

print(total)