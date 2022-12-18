from __future__ import print_function

def load(path):
    cubes = set()
    with open(path) as file:
        lines = file.read().split("\n")
        for cube in lines:
            xyz = cube.split(',')
            cubes.add((int(xyz[0]), int(xyz[1]), int(xyz[2])))
    return cubes

def neighbours(point, min, max):
    candidates = set()
    for delta in [(-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0,0,1)]:
        new = (point[0]+delta[0],point[1]+delta[1],point[2]+delta[2] )
        if not all([min <= p <= max for p in new]):
            continue
        else:
            candidates.add(new)
    return candidates


if __name__ == '__main__':
    # cubes = load('test.in')
    cubes = load('input.in')
    # print(*cubes, sep='\n')
    result = 0
    # Imagine a box around the droplet that leaves a small gap at each edge.
    # Put some steam in one corner of the box and keep trying to expand it.
    # Whenever the steam tries to expand into a point covered by the droplet, add 1 to area.

    min_value = min(min(point) for point in cubes) -1
    max_value = max(max(point) for point in cubes) +1
    # print(f'min_value: {min_value}; max_value: {max_value}')

    nodes = [(min_value, min_value, min_value)]
    visited = {nodes[0]}

    while nodes:
        node = nodes.pop()
        for neighbor in neighbours(node, min_value, max_value):
            if neighbor in visited:
                continue
            if neighbor in cubes:
                result += 1
            else:
                visited.add(neighbor)
                nodes.append(neighbor)

print(result)
