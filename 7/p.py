import sys


part1 = 0
part2 = []

def search(tree):
    global part1
    global part2
    value = tree.value
    for i in tree.children:
        value += search(i)
    if value <= 100000:
        part1 += value
    part2.append(value)
    return value

with open(sys.argv[1], "r") as f:
    inp = [x.strip() for x in f.readlines()]

class Tree:
    def __init__(self, value, name, parent):
        self.value = value
        self.name = name
        self.children = []
        self.parent = parent

root = Tree(0, "/", None)
current = root



for i in inp:
    if i == "$ cd /":
        current = root
    elif i == "$ cd ..":
        current = current.parent
    elif i.startswith("$ cd "):
        current = next((x for x in current.children if x.name == i.replace("$ cd ", "")), None)
    elif i == "$ ls":
        continue
    elif i.startswith("dir"):
        current.children.append(Tree(0, i.replace("dir ", ""), current))
    else:
        current.value += int(i.split()[0])

need = 30000000 - (70000000 - search(root))  
print("part1:", part1)

part2.sort()
for i in part2:
    if i > need:
        print("part2:", i)
        break

        




