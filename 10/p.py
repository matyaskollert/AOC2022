import sys

with open(sys.argv[1], "r") as f:
    inp = [x.strip() for x in f.readlines()]

nums = [20, 60, 100, 140, 180, 220]
wait = 0
part1 = 0
X = 1
index = 0
temp = 0
part2 = [["" for x in range(40)] for x in range(6)]

for i in range(1,240):
    if wait > 0:
        wait -= 1
    else:
        if temp != 0:
            X += temp
            temp = 0
        if index < len(inp):
            x = inp[index].split()
            index += 1
            if x[0] == "addx":
                temp = int(x[1])
                wait = 1
    if i in nums:
        part1 += X * i
    col = (i - 1) % 40
    row = i // 40
    part2[row][col] = '#' if (col == X or col == X + 1 or col == X - 1) else '.'


print(part1)
for x in part2:
    print(''.join(x))

