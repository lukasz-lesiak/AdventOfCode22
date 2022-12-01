f = open("../inputs/day1_input.txt", "r")
# f = open("../inputs/day1_test_input.txt", "r")
elfList = f.read().split('\n\n')
elfCalorieSumList = []
for elf in elfList:
    elfFoods = [int(x) for x in elf.split('\n')]
    elfCalorieSumList.append(sum(elfFoods))

elfCalorieSumList.sort(reverse=True)
print(sum(elfCalorieSumList[0:3]))

