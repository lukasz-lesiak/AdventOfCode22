import math

import numpy as numpy

# f = open("../inputs/day9_test_input.txt", "r")
f = open("../inputs/day9_input.txt", "r")
motions = f.read().split('\n')

tailPositions = [[0,0]]
headPositions = [[0,0]]
for motion in motions:
    directionAndLenght = motion.split(" ")
    direction = directionAndLenght[0]
    length = directionAndLenght[1]

    print(f'direction:{direction} length: {length}')

    for i in range(int(length)):
        lastHeadPosition = headPositions[-1]
        lastTailPosition = tailPositions[-1]
        if direction == 'U':
            headPositions.append([lastHeadPosition[0],lastHeadPosition[1]+1])
        if direction == 'D':
            headPositions.append([lastHeadPosition[0],lastHeadPosition[1]-1])
        if direction == 'R':
            headPositions.append([lastHeadPosition[0]+1,lastHeadPosition[1]])
        if direction == 'L':
            headPositions.append([lastHeadPosition[0]-1,lastHeadPosition[1]])
        newHeadPosition=headPositions[-1]

        distance = math.dist(lastTailPosition, newHeadPosition)
        if distance > 1.5:
            x = newHeadPosition[0] - lastTailPosition[0]
            y= newHeadPosition[1] - lastTailPosition[1]
            newTailPositionX = lastTailPosition[0]
            newTailPositionY = lastTailPosition[1]
            if abs(x) > 0.0 and abs(y)>0.0:
                newTailPositionX = lastTailPosition[0]+numpy.sign(x)
                newTailPositionY = lastTailPosition[1]+numpy.sign(y)
            else:
                if abs(x)>1.0:
                    newTailPositionX = lastTailPosition[0]+numpy.sign(x)
                if abs(y)>1.0:
                    newTailPositionY = lastTailPosition[1]+numpy.sign(y)
            tailPositions.append([newTailPositionX, newTailPositionY])

        print(f'HEAD: {headPositions[-1]} TAIL: {tailPositions[-1]}')

uniquePositions = []
for x in tailPositions:
    if x not in uniquePositions:
        uniquePositions.append(x)

print(f'{len(uniquePositions)}')


