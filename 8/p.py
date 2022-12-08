import sys

with open(sys.argv[1], "r") as f:
    inp = [x.strip() for x in f.readlines()]

x = [-1, 0, 0,  1]
y = [ 0, 1, -1, 0] 
part2 = 1

def check(i,j):
    global x, y, inp, part2
    biggest = int(inp[i][j])
    part1ret = 0
    part2ret = 1
    for d in range(len(x)):
        dx = x[d] + i
        dy = y[d] + j
        flag = False
        while dx < len(inp) and dx > -1 and dy < len(inp[0]) and dy > -1:
            if int(inp[dx][dy]) >= biggest:
                flag = True
                break
            dx += x[d]
            dy += y[d]
        if not flag:
            dx -= x[d]
            dy -= y[d]
            part1ret =  1
            diff = abs(dx - i) if abs(dx - i) > abs(dy - j) else abs(dy - j)
            part2ret *= diff 
        else:
            diff = abs(dx - i) if abs(dx - i) > abs(dy - j) else abs(dy - j)
            part2ret *= diff 


    part2 = part2 if part2 > part2ret else part2ret
    return part1ret 
            
part1 = len(inp) + len(inp[0]) 
part1 *= 2
part1 -= 4
for i in range(1, len(inp) - 1):
    for j in range(1, len(inp[0]) - 1):
        part1 += check(i,j)
    

print(part1)
print(part2)
