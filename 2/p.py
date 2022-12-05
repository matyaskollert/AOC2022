import sys

with open(sys.argv[1], "r") as f:
    inp = [x for x in f.readlines()]

indScore = {
    'X' : 1,
    'Y' : 2,
    'Z' : 3
}
winScore = {
    'A' : 'Y',
    'B' : 'Z',
    'C' : 'X'
    }

drawScore = {
    'A' : 'X',
    'B' : 'Y',
    'C' : 'Z'
    }
loseScore = {
    'A' : 'Z',
    'B' : 'X',
    'C' : 'Y'
    }
score = 0
for i in inp:
    me = i[2]
    him = i[0]
    score += indScore[me]
    if me == winScore[him]:
        score += 6
    elif me == drawScore[him]:
        score += 3

print(score)


score = 0
for i in inp:
    ch = i[2]
    him = i[0]
    if ch == 'X':
        me = loseScore[him]
    elif ch == 'Y':
        me = drawScore[him]
    else:
        me = winScore[him]
    score += indScore[me]
    if me == winScore[him]:
        score += 6
    elif me == drawScore[him]:
        score += 3

print(score)
