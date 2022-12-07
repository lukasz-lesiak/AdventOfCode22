from anytree import Node, RenderTree

# f = open("../inputs/day7_test_input.txt", "r")
f = open("../inputs/day7_input.txt", "r")

totalSpace = 70000000
requiredUnusedSpace = 30000000

logs = f.read().split('\n')
root = Node('', size=0)

currentDirectory = root

for log in logs:
    logAsList = log.split(' ')
    if logAsList[0] == '$':
        if logAsList[1] == 'cd':
            if logAsList[2] == '/':
                currentDirectory = root
                continue
            if logAsList[2] == '..':
                currentDirectory = currentDirectory.parent
                continue
            else:
                for node in currentDirectory.children:
                    if node.name == logAsList[2]:
                        currentDirectory = node
                continue
        if (logAsList[1] == 'ls'):
            continue
    if logAsList[0] == 'dir':
        Node(logAsList[1], currentDirectory, size=0)
        continue
    else:
        Node(logAsList[1], currentDirectory, size=logAsList[0])
        continue

print(RenderTree(root))

directories = set()

rootSize = 0
for node in root.descendants:
    if node.size == 0:
        descendantsSize = 0
        for child in node.descendants:
            descendantsSize += int(child.size)
        directories.add((node.name, descendantsSize))
    else:
        rootSize +=int(node.size)

spaceNeeded = abs(totalSpace - (requiredUnusedSpace+rootSize))

directoriesForDelete = set()
for d in directories:
    if d[1] > spaceNeeded:
        directoriesForDelete.add(d)

result = rootSize
for d in directoriesForDelete:
    if d[1] < result:
        result = d[1]

print(result)