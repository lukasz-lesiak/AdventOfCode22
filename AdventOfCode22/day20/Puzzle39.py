def load(path):
    with open(path) as file:
        numbers = []
        lines = file.read().split("\n")
        for line in lines:
            numbers.append(int(line))

        return numbers

if __name__ == "__main__":
    input_numbers = load('input.in')
    # print(input_numbers)

    buffer = [(id_, i) for id_, i in enumerate(input_numbers)]
    # print(buffer)

    for id_, i in enumerate(input_numbers):
        current_index = buffer.index((id_, i))
        buffer.remove((id_, i))
        new_index = (current_index + i + len(input_numbers) - 1) % (len(input_numbers) - 1)
        buffer.insert(new_index, (-1, i))

    zero_idx = buffer.index((-1, 0))

    thousand_numbers = []
    for i in range(3):
        index = (zero_idx+ (i+1) * 1000) %len(buffer)
        thousand_numbers.append(buffer[index][1])
    print(sum(thousand_numbers))
