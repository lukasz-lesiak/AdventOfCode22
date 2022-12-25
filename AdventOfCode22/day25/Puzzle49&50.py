def encode(digit):
    if digit == -1:
        return '-'
    if digit == -2:
        return  '='
    return str(digit)

def decimal2snafu(decimal):
    if decimal == 0:
        return ''
    r = (decimal + 2) % 5 - 2
    q = (decimal + 2) // 5
    return decimal2snafu(q) + encode(r)

if __name__ == "__main__":
    result = 0
    # with open('test.in') as f:
    with open('input.in') as f:
        lines = f.read().split("\n")
        for line in lines:
            # print(line)
            snafu_number_in_decimal = 0
            for i in reversed(range(len(line))):
                # print(f'{i} = {5**i}')
                digit_index = len(line)-i-1
                digit = line[digit_index]
                # print(f'{i} = {digit}')
                if digit == '-':
                    converted_digit = -1
                elif digit == '=':
                    converted_digit = -2
                else:
                    converted_digit = int(digit)
                # print(f'{i} = {converted_digit}')
                snafu_number_in_decimal += converted_digit*5**i
            # print(snafu_number_in_decimal)
            result+=snafu_number_in_decimal
    print(result)
    print(decimal2snafu(result))
