import math

import numpy as numpy

# f = open("../inputs/day9_test_input.txt", "r")
# f = open("../inputs/day9_test_input2.txt", "r")
f = open("../inputs/day9_input.txt", "r")
motions = f.read().split('\n')
knotsCount=10
knots = []
for i in range(knotsCount):
    knots.append([[0,0]])

for motion in motions:
    directionAndLenght = motion.split(" ")
    direction = directionAndLenght[0]
    length = directionAndLenght[1]

    print(f'direction:{direction} length: {length}')

    for i in range(int(length)):
        for i in range(int(len(knots))):
            if i==0:
                headLastPosition = knots[0][-1]
                if direction == 'U':
                    knots[0].append([headLastPosition[0], headLastPosition[1] + 1])
                if direction == 'D':
                    knots[0].append([headLastPosition[0], headLastPosition[1] - 1])
                if direction == 'R':
                    knots[0].append([headLastPosition[0] + 1, headLastPosition[1]])
                if direction == 'L':
                    knots[0].append([headLastPosition[0] - 1, headLastPosition[1]])
            else:
                knotLastPosition = knots[i][-1]
                distance = math.dist(knotLastPosition, knots[i-1][-1])
                if distance > 1.5:
                    x = knots[i-1][-1][0] - knotLastPosition[0]
                    y= knots[i-1][-1][1] - knotLastPosition[1]
                    newTailPositionX = knotLastPosition[0]
                    newTailPositionY = knotLastPosition[1]
                    # print(f'distance: {distance} x:{x}  y:{y}')
                    if abs(x) > 0.0 and abs(y)>0.0:
                        newTailPositionX = knotLastPosition[0] + numpy.sign(x)
                        newTailPositionY = knotLastPosition[1] + numpy.sign(y)
                    else:
                        if abs(x)>1.0:
                            newTailPositionX = knotLastPosition[0] + numpy.sign(x)
                        if abs(y)>1.0:
                            newTailPositionY = knotLastPosition[1] + numpy.sign(y)
                    knots[i].append([newTailPositionX, newTailPositionY])

                # print(f'HEAD: {knots[0][-1]} TAIL: {knots[-1][-1]}')


uniquePositions = []
for x in knots[-1]:
    if x not in uniquePositions:
        uniquePositions.append(x)

print(f'{len(uniquePositions)}')


