import sys

with open(sys.argv[1], "r") as f:
    inp = f.readlines()[0]


for i in range(3, len(inp)):
    if (len(set(inp[i-3: i + 1])) == 4):
        print("part1:",i+1)
        break


for i in range(13, len(inp)):
    if (len(set(inp[i-13: i + 1])) == 14):
        print("part2:",i+1)
        break
