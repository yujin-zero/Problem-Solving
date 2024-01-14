import sys
n, m = map(int, sys.stdin.readline().split())
a = []
for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))
n2, m2 = map(int, sys.stdin.readline().split())
b = []
for _ in range(n2):
    b.append(list(map(int, sys.stdin.readline().split())))
result = [[0 for _ in range(m2)] for _ in range(n)]

for i in range(n):
    for j in range(m2):
        for k in range(m):
            result[i][j] += a[i][k] * b[k][j]
for i in range(n):
    for j in range(m2):
        print(result[i][j], end=' ')
    print()
