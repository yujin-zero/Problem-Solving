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
            if len(lst) >= 1:
                if lst[-1] < i:
                    lst.append(i)
                    dfs()
                    lst.pop()
            else:
                lst.append(i)
                dfs()
                lst.pop()


dfs()
