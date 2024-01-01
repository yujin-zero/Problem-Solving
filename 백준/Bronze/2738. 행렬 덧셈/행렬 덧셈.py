import sys

n, m = map(int, sys.stdin.readline().split())
a = [[0 for _ in range(m)] for _ in range(n)]
b = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    x = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        a[i][j] = x[j]

for i in range(n):
    x = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        b[i][j] = x[j]

for i in range(n):
    for j in range(m):
        x = a[i][j] + b[i][j]
        print(x, end=' ')
    print()
