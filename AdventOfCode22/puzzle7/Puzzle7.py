# f = open("../inputs/day4_input.txt", "r")
f = open("../inputs/day4_test_input.txt", "r")
pairAssignments = f.read().split('\n')

duplicatedRanges = 0
for pairAssignment in pairAssignments:
    assignments = pairAssignment.split(',')
    e1 = assignments[0].split('-')
    e2 = assignments[1].split('-')
    elf1range = set(range(int(e1[0]), int(e1[1]) + 1))
    elf2range = set(range(int(e2[0]), int(e2[1]) + 1))
    print(f'E1: {elf1range} & E2: {elf2range}')
    if elf1range.issubset(elf2range) or elf2range.issubset(elf1range):
        duplicatedRanges += 1

print(f'Result: {duplicatedRanges}')
