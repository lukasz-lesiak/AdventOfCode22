# f = open("../inputs/day10_test_input2.txt", "r")
f = open("../inputs/day10_input.txt", "r")
instructions = f.read().split('\n')

x = 1
cycles = []

for instruction in instructions:
    commandAndArg = instruction.split(" ")
    if "noop" == commandAndArg[0]:
        cycles.append(x)
    if "addx" == commandAndArg[0]:
        cycles.append(x)
        cycles.append(x)
        x += int(commandAndArg[1])

crt = []

for i in range(len(cycles)):
    x = cycles[(i)]
    if i%40==x-1 or i%40 ==x+1 or i%40==x:
        crt.append("#")
    else:
        crt.append(".")

print(len(crt))
print(''.join(crt[0:40]))
print(''.join(crt[40:80]))
print(''.join(crt[80:120]))
print(''.join(crt[120:160]))
print(''.join(crt[160:200]))
print(''.join(crt[200:240]))
