import sys


def next(num, a):
    if a == 1:
        num[1] += 1
        return
    if num[a] < n:
        num[a] += 1
        return
    else:
        num[a] = 1
        next(num, a-1)


n, m = map(int, sys.stdin.readline().split())
num = [1]*(m+1)

while (num[1] <= n):

    for i in range(1, m+1):
        print(num[i], end=' ')
    print()
    next(num, m)
