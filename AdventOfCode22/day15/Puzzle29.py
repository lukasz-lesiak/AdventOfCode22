from __future__ import print_function
import re

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def load(path):
    with open(path) as file:
        lines = file.read().split("\n")
        sensorsSet=set()
        beaconsSet =set()
        for line in lines:
            coordinates = re.findall(r'-?\d+',line)
            sensorCoordinate= (int(coordinates[0]),int(coordinates[1]))
            beaconCoordinate = (int(coordinates[2]),int(coordinates[3]))
            dist = manhattan((sensorCoordinate[0],sensorCoordinate[1]),(beaconCoordinate[0],beaconCoordinate[1]))
            beaconsSet.add(beaconCoordinate)
            sensorsSet.add((sensorCoordinate[0], sensorCoordinate[1], dist))
            # print(f'sensor {sensorCoordinate} has distance {manhatan} to beacon {beaconCoordinate}')
        return sensorsSet,beaconsSet

if __name__ == '__main__':
    sensors,beacons = load("test_input.txt")
    # sensors,beacons = load("input.txt")
    checked = set()
    y=10
    # y = 2000000
    for sensor in sensors:
        for x in range(sensor[0] - sensor[2], sensor[0] + sensor[2] + 1):
            if manhattan(sensor, (x, y)) <= sensor[2]:
                checked.add((x, y))
    print(len(checked - beacons))
