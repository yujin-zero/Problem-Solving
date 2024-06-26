import sys

n = int(sys.stdin.readline())
if n == 1:
    print(0)
    sys.exit()
matrix = [(0,0)]
for _ in range(n) :
    x, y = map(int,sys.stdin.readline().split())
    matrix.append((x,y))
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for j in range(2,n+1) : # col
    for i in range(1, n-j + 2) :
        # dp[i][j+i-1] 이 값을 정해야함
        tmp = float('inf')
        for k in range(i,j+i-1) : # col
            value = dp[i][k] + dp[k+1][j+i-1] + matrix[i][0] * matrix[j+i-1][1] * matrix[k][1]
            if value < tmp :
                tmp = value
        dp[i][j+i-1] = tmp


# for d in dp :
#     print(d)

print(dp[1][n])