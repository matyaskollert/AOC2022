import sys

with open(sys.argv[1], "r") as f:
    lst = f.readlines()

splitLine = lst.index("\n") - 2
num = len(lst[splitLine])//4
stacks = [[] for x in range(num)]
stacks2 = [[] for x in range(num)]
inp = True
for l in range(splitLine, -1, -1):
    line = lst[l]
    for i in range(0, len(line), 4):
        if line[i+1] != " ":
            stacks[i//4].append(line[i+1])
            stacks2[i//4].append(line[i+1])


for l in range(splitLine+3, len(lst)):
    line = lst[l].strip().split()
    for i in range(int(line[1])):
        stacks[int(line[5]) - 1].append(stacks[int(line[3]) - 1].pop())

for l in range(splitLine+3, len(lst)):
    line = lst[l].strip().split()
    crates = []
    for i in range(int(line[1])):
        crates.append(stacks2[int(line[3]) - 1].pop())
    crates.reverse()
    stacks2[int(line[5])-1].extend(crates)


part1 = '';
part2 = '';

for i in stacks:
    part1 += i.pop()

for i in stacks2:
    part2 += i.pop()

print("part1: " + part1)
print("part2: " + part2)
