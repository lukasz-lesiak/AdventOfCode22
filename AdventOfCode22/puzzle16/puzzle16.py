# f = open("../inputs/day8_test_input.txt", "r")
f = open("../inputs/day8_input.txt", "r")

rows = f.read().split('\n')
grid = []
for i in range(len(rows)):
    row = rows[i]
    treeRow = []
    for j in range(len(row)):
        treeRow.append([row[j]])
    grid.append(treeRow)

maxScenicScore = 0
for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[i]) - 1):
        scenicScoreUp = 0
        scenicScoreDown = 0
        scenicScoreLeft = 0
        scenicScoreRight = 0
        for z in reversed(range(0, i)):
            if grid[i][j] > grid[z][j]:
                scenicScoreUp += 1
            else:
                scenicScoreUp += 1
                break

        for x in range(i+1, len(grid)):
            if grid[i][j] > grid[x][j]:
                scenicScoreDown += 1
            else:
                scenicScoreDown += 1
                break

        for c in reversed(range(0, j)):
            if grid[i][j] > grid[i][c]:
                scenicScoreLeft += 1
            else:
                scenicScoreLeft += 1
                break

        for v in range(j+1, len(grid[i])):
            if grid[i][j] > grid[i][v]:
                scenicScoreRight += 1
            else:
                scenicScoreRight += 1
                break

        currentScenicScore = scenicScoreUp * scenicScoreDown * scenicScoreLeft * scenicScoreRight
        if maxScenicScore < currentScenicScore:
            maxScenicScore = currentScenicScore

print(f'max {maxScenicScore}')