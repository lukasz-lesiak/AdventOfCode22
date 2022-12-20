def load(path):
    with open(path) as file:
        numbers = []
        decryption_key = 811589153
        lines = file.read().split("\n")
        for line in lines:
            numbers.append(int(line)*decryption_key)

        return numbers

if __name__ == "__main__":
    input_numbers = load('input.in')
    # print(input_numbers)
    buffer = [(id_, i) for id_, i in enumerate(input_numbers)]
    # print(buffer)

    for n in range(10):
        for id_, i in enumerate(input_numbers):
            current_index = buffer.index((id_, i))
            buffer.remove((id_, i))
            new_index = (current_index + i + len(input_numbers) - 1) % (len(input_numbers) - 1)
            buffer.insert(new_index, (id_, i))

    zero_idx = buffer.index((input_numbers.index(0), 0))

    thousand_numbers = []
    for i in range(3):
        index = (zero_idx+ (i+1) * 1000) %len(buffer)
        thousand_numbers.append(buffer[index][1])
    print(sum(thousand_numbers))
