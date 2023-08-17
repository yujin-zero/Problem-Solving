import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
house = []
chicken = []
for i in range(1, n+1):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(1, n+1):
        if line[j-1] == 1:
            house.append([i, j])
        elif line[j-1] == 2:
            chicken.append([i, j])

dis = []
for h in house:
    temp = []
    for c in chicken:
        d = abs(h[0]-c[0]) + abs(h[1]-c[1])
        temp.append(d)
    dis.append(temp)

answer = float('inf')
select_chicken = list(combinations([i for i in range(len(chicken))], m))
for s in select_chicken:
    a = 0
    for d in dis:
        b = float('inf')
        for i in range(len(chicken)):
            if i in s:
                if d[i] < b:
                    b = d[i]
        a += b
    if a < answer:
        answer = a

print(answer)
