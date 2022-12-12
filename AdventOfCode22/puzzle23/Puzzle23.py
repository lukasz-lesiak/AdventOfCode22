from __future__ import print_function
from collections import deque


def load(path):
    f = open(path, "r")
    rows = f.read().split('\n')
    grid = []
    start = []
    end = []
    for i in range(len(rows)):
        gridRow = []
        for j in range(len(rows[i])):
            point = rows[i][j]
            if point == 'S':
                start = (i, j)
                gridRow.append('a')
                continue
            if point == 'E':
                end = (i, j)
                gridRow.append('z')
                continue
            gridRow.append(point)
        grid.append(gridRow)
    return [grid, start, end]


def bfs(grid, start, end):
    visited = set()
    queue = deque([(start, 0)])
    while queue:
        position, distance = queue.popleft()
        if position == end:
            return distance
        if position in visited:
            continue
        visited.add(position)
        x, y = position
        for neighbourX, neighbourY in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            if (0 <= y + neighbourY < len(grid[0]) and
                    0 <= x + neighbourX < len(grid) and
                    ord(grid[x + neighbourX][y + neighbourY]) - ord(grid[x][y]) <= 1
            ):
                queue.append(((x + neighbourX, y + neighbourY), distance + 1))


if __name__ == '__main__':
    # inputData = load("../inputs/day12_test_input.txt")
    inputData = load("../inputs/day12_input.txt")
    grid = inputData[0]
    start = inputData[1]
    end = inputData[2]
    print(*grid, sep='\n')
    print(f'Start {start}')
    print(f'End {end}')
    print(bfs(grid, start, end))
