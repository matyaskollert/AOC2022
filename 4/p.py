import sys

with open(sys.argv[1], "r") as f:
    inp = [x.split(",") for x in f.readlines()]


part1 = 0
part2 = 0
add1 = True
add2 = True
for i in inp:
    a1, a2 = i[0].strip().split("-")
    b1, b2 = i[1].strip().split("-")
    if int(a1) <= int(b1):
        if int(a2) >= int(b2):
            add1 = False
            add2 = False
            part1 += 1
            part2 += 1
        elif int(a2) >= int(b1):
            add2 = False
            part2 += 1
    if int(a1) >= int(b1):
        if int(a2) <= int(b2):
            part1 += 1 if add1 else 0 
            part2 += 1 if add2 else 0
        elif int(b2) >= int(a1):
            part2 += 1 if add2 else 0
    add1 = True
    add2 = True
print(part1)
print(part2)
