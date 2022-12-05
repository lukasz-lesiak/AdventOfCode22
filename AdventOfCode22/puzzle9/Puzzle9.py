import re

f = open("../inputs/day5_input.txt", "r")
crates = [
    ['F', 'C', 'J', 'P', 'H', 'T', 'W'],
    ['G', 'R', 'V', 'F', 'Z', 'J', 'B', 'H'],
    ['H', 'P', 'T', 'R'],
    ['Z', 'S', 'N', 'P', 'H', 'T'],
    ['N', 'V', 'F', 'Z', 'H', 'J', 'C', 'D'],
    ['P', 'M', 'G', 'F', 'W', 'D', 'Z'],
    ['M', 'V', 'Z', 'W', 'S', 'J', 'D', 'P'],
    ['N', 'D', 'S'],
    ['D', 'Z', 'S', 'F', 'M']]

# f = open("../inputs/day5_test_input.txt", "r")
# crates = [['Z', 'N'], ['M', 'C', 'D'], ['P']]
movements = f.read().split('\n')

for movement in movements:
    numbers = re.findall(r'\d+', movement)
    print(numbers)
    for i in range(int(numbers[0])):
        crates[int(numbers[2]) - 1].append(crates[int(numbers[1]) - 1].pop())

print(crates)
for i in range(len(crates)):
    print(crates[i][-1])
