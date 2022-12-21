import sympy

def load(path):
    with open(path) as file:
        monkeys = []
        lines = file.read().split("\n")
        for line in lines:
            monkey_name, expression = line.split(': ')
            # print(f'{monkey_name}   {expression}')
            monkeys.append((monkey_name, expression))
        return monkeys


if __name__ == "__main__":
    queue = load('input.in')
    monkeys_calculated = {"humn": sympy.Symbol("x")}

    ops = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    # print(queue)
    for monkey in queue:
        # print(monkey[0] + " = " + monkey[1])
        # print(f'{len(queue)} - {len(monkeys_calculated)}')
        if monkey[0] in monkeys_calculated:
            continue
        if str(monkey[1]).isnumeric():
            # print(monkey[1])
            monkeys_calculated[monkey[0]] = int(monkey[1])
        else:
            left,operator,right = monkey[1].split()
            # print(left,operator,right)
            if left in monkeys_calculated and right in monkeys_calculated:
                if monkey[0] == "root":
                    print(sympy.solve(monkeys_calculated[left] - monkeys_calculated[right]))
                    break
                monkeys_calculated[monkey[0]] = ops[operator](monkeys_calculated[left], monkeys_calculated[right])
            else:
                queue.append((monkey[0], monkey[1]))
