import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
sum = [0]
for i in range(1, n+1):
    sum.append(sum[i-1]+num[i-1])

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(sum[j]-sum[i-1])
