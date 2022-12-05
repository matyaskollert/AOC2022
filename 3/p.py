import sys

with open(sys.argv[1], "r") as f:
    lst = [x.strip() for x in f.readlines()]

score = 0
score2 = 0
count = 0
arr2 = list()
for i,l in enumerate(lst):
    if count == 0:
        arr2.append(set(l)&set(lst[i + 1])&set(lst[i+2]))
    count = (count + 1) % 3  
    arr = list()
    one = l[:len(l)//2:]
    two = l[len(l)//2::]
    for o in one:
        for t in two:
            if (o == t):
                arr.append(o)
    for o in set(arr):
        if (o.islower()):
            score += ord(o) - 96
        else:
            score += ord(o) - 64 + 26
print(score)


for s in arr2:
    o = next(iter(s)) 
    if (o.islower()):
        score2 += ord(o) - 96
    else:
        score2 += ord(o) - 64 + 26

print(score2)
