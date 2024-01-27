import sys
n = int(sys.stdin.readline())
lst = [[' ' for _ in range(n)]for _ in range(n)]
now = 3
lst[0][0] = '*'
lst[0][1] = '*'
lst[0][2] = '*'
lst[1][0] = '*'
lst[1][2] = '*'
lst[2][0] = '*'
lst[2][1] = '*'
lst[2][2] = '*'

while now != n:
    for i in range(now):
        for j in range(now):
            lst[i+now][j] = lst[i][j]
            lst[i+now*2][j] = lst[i][j]
            lst[i][j+now] = lst[i][j]
            lst[i][j+now*2] = lst[i][j]
            lst[i+now][j+now*2] = lst[i][j]
            lst[i+now*2][j+now] = lst[i][j]
            lst[i+now*2][j+now*2] = lst[i][j]
    now *= 3


for a in lst:
    for b in a:
        print(b, end='')
    print()
