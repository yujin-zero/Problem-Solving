import sys

m, n = map(int, sys.stdin.readline().split())

chess = []
for i in range(m):
    x = sys.stdin.readline()
    x2 = []
    for j in range(n):
        x2.append(x[j])
    chess.append(x2)


min = 64
for a in range(0, m-7):
    for b in range(0, n-7):
        result1 = 0
        result2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if chess[i][j] != 'W':
                        result1 += 1
                    elif chess[i][j] != 'B':
                        result2 += 1
                else:
                    if chess[i][j] != 'B':
                        result1 += 1
                    elif chess[i][j] != 'W':
                        result2 += 1
        if min > result1:
            min = result1
        if min > result2:
            min = result2

print(min)
