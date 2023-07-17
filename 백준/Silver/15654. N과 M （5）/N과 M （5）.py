import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num.sort()
lst = []


def dfs():
    if len(lst) == m:
        print(*lst)
        return
    else:
        for i in num:
            if i not in lst:
                lst.append(i)
                dfs()
                lst.pop()


dfs()
