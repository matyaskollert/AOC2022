import sys

with open(sys.argv[1], "r") as f:
    inp = [x.strip() for x in f.readlines()]


T = [[0,0] for x in range(9)]
H = [0,0]
D = {'R': [1,0], 'L': [-1,0], 'U': [0,1], 'D': [0,-1]}

part1 = []
part2 = []

for l in inp:
    d, n = l.split()
    for i in range(int(n)):
        dX = D[d][0]
        dY = D[d][1]
        H[0] += dX 
        H[1] += dY
        tempX = H[0]
        tempY = H[1]
        prevX = H[0] - dX
        prevY = H[1] - dY
        for j in range(len(T)):
            diffX = tempX * dX - T[j][0] * dX 
            diffY = tempY * dY - T[j][1] * dY 
            oldX = T[j][0]
            oldY = T[j][1]
            if diffX <= 1 and diffY <= 1:
                g = 0
            else:
                if j == 0 or ((abs(dX) == 1 and dY == 0) or (dX == 0 and abs(dY) == 1)):
                    T[j][0] = prevX 
                    T[j][1] = prevY 
                else:
                    T[j][0] += dX
                    T[j][1] += dY
            tempX = T[j][0]
            tempY = T[j][1]
            dX = tempX - oldX
            dY = tempY - oldY
            prevX = oldX
            prevY = oldY
        part1.append((T[0][0], T[0][1]))
        part2.append((T[8][0], T[8][1]))
    print(H, T[0], T[8])

print(len(set(part1)))
print(len(set(part2)))
