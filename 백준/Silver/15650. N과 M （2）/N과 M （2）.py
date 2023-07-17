import sys


def dfs():
    if len(num) == m:
        check = 0
        for i in range(len(num)-1):
            if num[i] > num[i+1]:
                check = 1
        if check == 0:
            print(' '.join(map(str, num)))
        return
    else:
        for i in range(1, n+1):
            if i not in num:
                num.append(i)
                dfs()
                num.pop()


n, m = map(int, sys.stdin.readline().split())
num = []

dfs()
