import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
num = []
for _ in range(n):
    x = sys.stdin.readline()
    lst = []
    for i in range(m):
        lst.append(int(x[i]))
    num.append(lst)
answer = 0

for x in range(10):
    num_x = [[] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if num[i][j] == x:
                num_x[i].append(j)

    for k in range(n):
        if len(num_x) > 1:
            a = list(combinations(num_x[k], 2))
            for value in a:
                dis = value[1] - value[0]
                if k+dis < n:
                    if value[0] in num_x[k+dis] and value[1] in num_x[k+dis]:
                        if answer < dis:
                            answer = dis

print((answer+1)**2)
