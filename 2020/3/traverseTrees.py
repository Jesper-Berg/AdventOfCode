with open('input.txt') as input:
    land = []
    for line in input.readlines():
        land.append(list(line[:-1]))
    width = len(land[0])
    height = len(land)
    totalProduct = 1
    slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
    for slope in slopes:
        totalTrees = 0
        currentX = 0
        currentY = 0    
        while currentY < height:
            if currentX >= width:
                currentX = currentX - width
            if land[currentY][currentX] == '#':
                totalTrees += 1
            currentX += slope[0]
            currentY += slope[1]
        print(f'Total trees for this slope is {totalTrees}')
        totalProduct *= totalTrees    
    print(totalProduct)
