import sys
sys.setrecursionlimit(10**6)

t = int(sys.stdin.readline())
answer = []


def explor(i, j):
    cabbage[i][j] = 0
    if i-1 >= 0:
        if cabbage[i-1][j] == 1:
            cabbage[i-1][j] = 0
            explor(i-1, j)
    if i+1 < m:
        if cabbage[i+1][j] == 1:
            cabbage[i+1][j] = 0
            explor(i+1, j)
    if j-1 >= 0:
        if cabbage[i][j-1] == 1:
            cabbage[i][j-1] = 0
            explor(i, j-1)
    if j+1 < n:
        if cabbage[i][j+1] == 1:
            cabbage[i][j+1] = 0
            explor(i, j+1)


for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    result = 0
    cabbage = [[0 for _ in range(n)] for _ in range(m)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        cabbage[x][y] = 1
    for i in range(m):
        for j in range(n):
            if cabbage[i][j] == 1:
                explor(i, j)
                result += 1
    answer.append(result)

for a in answer:
    print(a)
