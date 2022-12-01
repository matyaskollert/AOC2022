import sys

with open(sys.argv[1], "r") as f:
    inp = [x.strip() for x in f.readlines()]

max = 0
count = 0
for i in inp:
    if (i == ""):
        max = count if count > max else max 
        count = 0
    else:
        count += int(i)
print("part1: ",max)



count = 0
lst = []
for i in inp:
    if (i == ""):
        lst.append(count)
        count = 0
    else:
        count += int(i)
lst.sort(reverse=True)
print("part2:", sum(lst[0:3]))
