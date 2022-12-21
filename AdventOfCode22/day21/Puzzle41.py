
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
    monkeys_calculated = {}

    # print(queue)
    for monkey in queue:
        # print(monkey[0] + " = " + monkey[1])
        # print(f'{len(queue)} - {len(monkeys_calculated)}')
        if str(monkey[1]).isnumeric():
            # print(monkey[1])
            monkeys_calculated[monkey[0]] = int(monkey[1])
        else:
            left,operator,right = monkey[1].split()
            # print(left,operator,right)
            if left in monkeys_calculated and right in monkeys_calculated:
                monkeys_calculated[monkey[0]] = eval(f"{monkeys_calculated[left]} {operator} {monkeys_calculated[right]}")
            else:
                queue.append((monkey[0], monkey[1]))
    print(monkeys_calculated['root'])
