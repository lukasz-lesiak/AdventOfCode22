# f = open("../inputs/day8_test_input.txt", "r")
f = open("../inputs/day8_input.txt", "r")

rows = f.read().split('\n')
grid = []
for i in range(len(rows)):
    row = rows[i]
    treeRow = []
    for j in range(len(row)):
        treeRow.append([row[j]])
    print(treeRow)
    grid.append(treeRow)
visibleTreeCount = 2 * len(grid) + 2 * len(grid[0]) - 4
print(f'edge trees count: {visibleTreeCount}')

for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[i]) - 1):
        isVisible1 = True
        isVisible2 = True
        isVisible3 = True
        isVisible4 = True
        for k in reversed(range(0, i)):
            if grid[i][j] <= grid[k][j]:
                isVisible1 = False
                break

        for k in range(i+1, len(grid)):
            if grid[i][j] <= grid[k][j]:
                isVisible2 = False
                break

        for k in reversed(range(0, j)):
            if grid[i][j] <= grid[i][k]:
                isVisible3 = False
                break

        for k in range(j+1, len(grid[i])):
            if grid[i][j] <= grid[i][k]:
                isVisible4 = False
                break

        if isVisible1 or isVisible2 or isVisible3 or isVisible4:
            visibleTreeCount += 1

print(f'all visible trees: {visibleTreeCount}')
