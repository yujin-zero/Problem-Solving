import sys

def multi(aa,bb) :
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n) :
        for j in range(n) :
            tmp = 0
            for k in range(n) :
                tmp += aa[i][k] * bb[k][j]
            result[i][j] = tmp % 1000
    
    return result

def power(xx, yy) :
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n) :
        result[i][i] = 1

    while yy > 0 :
        if yy % 2 == 1 :
            result = multi(result,xx)
        xx = multi(xx,xx)
        yy //= 2

    return result


n, b = map(int,sys.stdin.readline().split())
matrixA = []
for _ in range(n) :
    x = list(map(int,sys.stdin.readline().split()))
    matrixA.append(x)

answer = power(matrixA, b)

for m in answer :
    print(*m)