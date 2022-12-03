import string

f = open("../inputs/day3_input.txt", "r")
# f = open("../inputs/day3_test_input.txt", "r")
rucksacks = f.read().split('\n')
sum = 0

for i in range(int(len(rucksacks)/3)):
    badge = set(rucksacks.pop()).intersection(rucksacks.pop(),rucksacks.pop()).pop()
    badgePriority = string.ascii_letters.index(badge) + 1
    sum += badgePriority

print(f'result: {sum}')