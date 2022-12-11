import math
import time

def loadMonkeys(path):

    f = open(path, "r")
    notes = f.read().split('\n\n')
    monkeys = []

    for note in notes:
        monkeyNotes = note.split('\n')
        startingItems = []
        operation = lambda old: old
        test = 0
        positive = -1
        negative = -1
        for line in monkeyNotes:

            if line.startswith("  Starting items:"):
                itemLine = line.partition(': ')[2]
                # startingItems = itemLine.split(',')
                for si in  itemLine.split(','):
                    startingItems.append(int(si))
            if line.startswith("  Operation: "):
                operationLine = line.partition('new = ')[2]
                operation = eval('lambda old:' + operationLine)
            if line.startswith("  Test:"):
                test = line.partition('by ')[2]
            if line.startswith("    If true:"):
                positive = line.partition('monkey ')[2]
            if line.startswith("    If false:"):
                negative = line.partition('monkey ')[2]

        monkeys.append({
            'count': 0,
            'items': startingItems,
            'operation': operation,
            'test': int(test),
            'positive': positive,
            'negative': negative
        })
    return monkeys

def fMonkeyObserves(f, value, z):
    return f(value)%z

if __name__ == '__main__':
    start_time = time.time()
    # monkeys = loadMonkeys("../inputs/day11_test_input.txt")
    monkeys = loadMonkeys("../inputs/day11_input.txt")

    testValues = []
    for monkey in monkeys:
        testValues.append(monkey["test"])
    modulo = math.prod(testValues)
    # print(f'Modulo: {modulo}, based on {testValues}')
    for round in range(10000):
        print("Round: %s --- %s seconds ---" %(round,(time.time() - start_time)))

        for monkey in monkeys:
            monkey['count'] += len(monkey['items'])

            newItemValues = []
            for item in monkey['items']:
                newItemValues.append(fMonkeyObserves(monkey["operation"],item, modulo))

            for newItemValue in newItemValues:
                if newItemValue % monkey['test'] == 0:
                    monkeys[int(monkey["positive"])]["items"].append(newItemValue)
                else:
                    monkeys[int(monkey["negative"])]["items"].append(newItemValue)
            monkey["items"] = []


print("\n#######################################################\n")
monkeysCounts = []
for monkey in monkeys:
    monkeysCounts.append(monkey["count"])

monkeysCounts.sort(reverse=True)
print(monkeysCounts)
print(f'Result {monkeysCounts[0]*monkeysCounts[1]}')
