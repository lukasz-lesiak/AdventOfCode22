from __future__ import print_function
import re
import time


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def load(path):
    with open(path) as file:
        lines = file.read().split("\n")
        sensorsSet = set()
        beaconsSet = set()
        for line in lines:
            coordinates = re.findall(r'-?\d+', line)
            sensorCoordinate = (int(coordinates[0]), int(coordinates[1]))
            beaconCoordinate = (int(coordinates[2]), int(coordinates[3]))
            dist = manhattan((sensorCoordinate[0], sensorCoordinate[1]), (beaconCoordinate[0], beaconCoordinate[1]))
            beaconsSet.add(beaconCoordinate)
            sensorsSet.add((sensorCoordinate[0], sensorCoordinate[1], dist))
            # print(f'sensor {sensorCoordinate} has distance {manhatan} to beacon {beaconCoordinate}')
        return sensorsSet, beaconsSet


def brute_force(limit, sensors):
    for x in range(limit + 1):
        for y in range(limit + 1):
            print("crd: %s --- %s seconds ---" % ((x, y), (time.time() - start_time)))
            found = False
            for sensor in sensors:
                if manhattan(sensor, (x, y)) <= sensor[2]:
                    found = True
                    break
            if not found:
                return (x, y)


def crdOutOfRange(limit, sensor):
    points = set()
    left = (sensor[0] - sensor[2] - 1, sensor[1])
    right = (sensor[0] + sensor[2] + 1, sensor[1])
    up = (sensor[0], sensor[1] + sensor[2] + 1)
    down = (sensor[0], sensor[1] - sensor[2] - 1)
    # print(f'L {left}')
    # print(f'U {up}')
    # print(f'R {right}')
    # print(f'D {down}')

    lu = lineLU(left, up)
    ur = lineUR(up, right)
    rd = lineRD(right, down)
    dl = lineDL(down, left)
    points.update(lu)
    points.update(ur)
    points.update(rd)
    points.update(dl)
    # print(f'Points size: {len(points)} - {points}')
    # print(f'LU {lu}')
    # print(f'UR {ur}')
    # print(f'RD {rd}')
    # print(f'DL {dl}')
    result = set()
    for point in points:
        if point[0] <= limit and point[0] > 0 and point[1] <= limit and point[1] > 0:
            result.add(point)
    return result


def lineLU(p1, p2):
    x_list = []
    y_list = []
    for x in range(p1[0], p2[0] + 1):
        x_list.append(x)
    for y in range(p1[1], p2[1] + 1):
        y_list.append(y)
    return set(zip(x_list, y_list))


def lineUR(p1, p2):
    x_list = []
    y_list = []
    for x in range(p1[0], p2[0] + 1):
        x_list.append(x)
    for y in range(p2[1], p1[1] + 1):
        y_list.append(y)
    return set(zip(x_list, reversed(y_list)))


def lineRD(p1, p2):
    x_list = []
    y_list = []
    for x in range(p2[0], p1[0] + 1):
        x_list.append(x)
    for y in range(p1[1], p2[1] + 1):
        y_list.append(y)
    return list(zip(reversed(x_list), y_list))


def lineDL(p1, p2):
    x_list = []
    y_list = []
    for x in range(p2[0], p1[0] + 1):
        x_list.append(x)
    for y in range(p2[1], p1[1] + 1):
        y_list.append(y)
    return list(zip(reversed(x_list), reversed(y_list)))


def sophisticated(limit, sensors):
    points = set()
    for sensor in sensors:
        points.update(crdOutOfRange(limit, sensor))

    for point in points:
        x = point[0]
        y = point[1]
        print("crd: %s --- %s seconds ---" % ((x, y), (time.time() - start_time)))
        found = False
        for sensor in sensors:
            if manhattan(sensor, (x, y)) <= sensor[2]:
                found = True
                break
        if not found:
            return (x, y)

    return 0, 0


if __name__ == '__main__':
    start_time = time.time()

    # sensors, beacons = load("test_input.txt")
    sensors,beacons = load("input.txt")
    # limit = 20
    limit = 4000000
    # beacon = brute_force(limit,sensors)
    beacon = sophisticated(limit, sensors)

    print(f'x = {beacon[0]} y = {beacon[1]}')
    print(f'result: {beacon[0] * 4000000 + beacon[1]}')
