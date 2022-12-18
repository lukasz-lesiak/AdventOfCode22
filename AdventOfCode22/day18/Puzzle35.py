from __future__ import print_function
from itertools import combinations


def load(path):
    cubes = set()
    with open(path) as file:
        lines = file.read().split("\n")
        for cube in lines:
            xyz = cube.split(',')
            cubes.add((int(xyz[0]), int(xyz[1]), int(xyz[2])))
    return cubes


def is_connected(point1, point2):
    distance = 0
    for d1, d2 in zip(point1, point2):
        # print(f'd1:{d1}; d2:{d2};')
        distance += abs(d1 - d2)
    return distance == 1


if __name__ == '__main__':
    # cubes = load('test.in')
    cubes = load('input.in')
    result = 0
    result += len(cubes) * 6

    for p1, p2 in combinations(cubes, 2):
        if not is_connected(p1, p2):
            continue
        else:
            result -= 2

    # print(*cubes, sep='\n')
    print(result)
