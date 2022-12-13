from __future__ import print_function

def load(path):
    with open(path) as file:
        pairsOfPackets = file.read().split("\n\n")
    return [tuple(map(eval, pairOfPackets.splitlines())) for pairOfPackets in pairsOfPackets]


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return None
        return left < right
    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]
    for l, r in zip(left, right):
        sub = compare(l, r)
        if sub is not None:
            return sub
    if len(left) < len(right):
        return True
    if len(left) > len(right):
        return False
    return None


class Packet:
    def __init__(self, packet):
        self._packet = packet

    def __lt__(self, other):
        return compare(self._packet, other._packet)

    def __gt__(self, other):
        return not compare(self._packet, other._packet)

    def __eq__(self, other):
        return self._packet == other

if __name__ == '__main__':
    # inputData = load("test_input.txt")
    inputData = load("input.txt")
    print(*inputData, sep='\n')
    result = sum(i for i, p in enumerate(inputData, 1) if compare(*p))
    print(result)

    packet2, packet6 = Packet([[2]]), Packet([[6]])
    packets = [packet2, packet6]
    for pair in inputData:
        for pkt in pair:
            packets.append(Packet(pkt))
    packets.sort()
    result2 = (packets.index(packet2) + 1) * (packets.index(packet6) + 1)
    print(result2)
