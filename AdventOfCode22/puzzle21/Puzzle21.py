import re

# f = open("../inputs/day11_test_input.txt", "r")
f = open("../inputs/day11_input.txt", "r")
notes = f.read().split('\n\n')

monkeys = []
for note in notes:
    monkeyNotes = note.split('\n')
    inspectCount = 0
    startingItems = []
    operation = lambda old: old
    test = 0
    positive = -1
    negative = -1
    for line in monkeyNotes:

        if line.startswith("  Starting items:"):
            itemLine = line.partition(': ')[2]
            startingItems = itemLine.split(',')
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

for monkey in monkeys:
    print(f'Monkey: {monkey}')

for round in range(20):
# for r in range(1):
    for monkey in monkeys:
        print(monkey)
        for item in monkey['items']:
            monkey['count'] +=1
            # print(f'old = {int(item)} new = {monkey["operation"](int(item))}')
            newItemValue = monkey["operation"](int(item)) // 3
            print(f'item: {item} with new value {newItemValue} divided by {monkey["test"]} is {monkey["operation"](int(item)) % monkey["test"]}')
            if newItemValue % monkey['test'] == 0:
                print(f'positive: {monkeys[int(monkey["positive"])]}')
                monkeys[int(monkey["positive"])]["items"].append(newItemValue)
            else:
                print(f'negative: {monkeys[int(monkey["negative"])]}')
                monkeys[int(monkey["negative"])]["items"].append(newItemValue)
        monkey["items"] = []



print("\n#######################################################\n")
monkeysCounts = []
for monkey in monkeys:
    print(monkey)
    monkeysCounts.append(monkey["count"])


monkeysCounts.sort(reverse=True)
print(monkeysCounts)
print(f'Result {monkeysCounts[0]*monkeysCounts[1]}')