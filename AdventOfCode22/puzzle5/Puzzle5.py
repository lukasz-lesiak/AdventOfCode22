import string

f = open("../inputs/day3_input.txt", "r")
# f = open("../inputs/day3_test_input.txt", "r")
rucksacks = f.read().split('\n')
sum = 0
for rucksack in rucksacks:
    l = len(rucksack)
    bag1 = rucksack[0:int(l/2)]
    bag2 = rucksack[int(l/2):l]
    print(bag1 + '    ' + bag2)
    print(f'{len(bag1)} & {len(bag2)}')
    item = set(bag1).intersection(bag2)
    itemPriority = string.ascii_letters.index(item.pop()) + 1
    sum += itemPriority

print('result: {sum}')