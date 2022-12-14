def load(path):
    with open(path) as file:
        lines = file.read().split("\n")
        rocks = set()
        voidLevel = 0
        for line in lines:
            line = line.split(" -> ")
            for i in range(1, len(line)):
                x, y = line[i].split(",")
                x = int(x)
                y = int(y)
                previousX, previousY = line[i - 1].split(",")
                previousX = int(previousX)
                previousY = int(previousY)
                if y > voidLevel or previousY > voidLevel:
                    voidLevel = max(y, previousY)
                if x == previousX:
                    for verticalRock in range(min(y, previousY), max(y, previousY) + 1):
                        rocks.add((x, verticalRock))
                else:
                    for horizontalRock in range(min(x, previousX), max(x, previousX) + 1):
                        rocks.add((horizontalRock, y))
        return (rocks, voidLevel + 1)


def sandFalling(rocks, voidLevel, isVoid):
    rocksAndSand = rocks.copy()
    while True:
        sandX = 500
        sandY = 0
        if (500, 0) in rocksAndSand:
            return len(rocksAndSand) - len(rocks)
        while True:
            if sandY == voidLevel:
                if isVoid:
                    return len(rocksAndSand) - len(rocks)
                else:
                    rocksAndSand.add((sandX, sandY))
                    break
            if (sandX, sandY + 1) not in rocksAndSand:
                sandY += 1
            elif (sandX - 1, sandY + 1) not in rocksAndSand:
                sandY += 1
                sandX -= 1
            elif (sandX + 1, sandY + 1) not in rocksAndSand:
                sandY += 1
                sandX += 1
            else:
                rocksAndSand.add((sandX, sandY))
                break


if __name__ == '__main__':
    # rocks,voidLevel = load("test_input.txt")
    rocks, voidLevel = load("input.txt")
    # print(rocks)
    # print(floorLevel)
    print("Void", sandFalling(rocks, voidLevel, True))
    print("Floor", sandFalling(rocks, voidLevel, False))
