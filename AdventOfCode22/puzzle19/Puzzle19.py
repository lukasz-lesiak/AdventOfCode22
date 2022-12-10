# f = open("../inputs/day10_test_input.txt", "r")
# f = open("../inputs/day10_test_input2.txt", "r")
f = open("../inputs/day10_input.txt", "r")
instructions = f.read().split('\n')

x = 1
cycles = []
instructionsDuration = {"noop": 1, "addx": 2}

for instruction in instructions:
    commandAndArg = instruction.split(" ")
    if "noop" == commandAndArg[0]:
        cycles.append(x)
    if "addx" == commandAndArg[0]:
        cycles.append(x)
        cycles.append(x)
        x += int(commandAndArg[1])

print(cycles)

multiplicationCycles = [20,60,100,140,180,220]

xValues = []
signalValues = []
signalSum = 0
for multiplicationCycle in multiplicationCycles:
    xValue=cycles[multiplicationCycle-1]
    xValues.append(xValue)
    signalValue = xValue*multiplicationCycle
    signalValues.append(signalValue)
    signalSum +=signalValue

print(f'xValues: {xValues}')
print(f'signalValues: {signalValues}')
print(f'signalSum: {signalSum}')
