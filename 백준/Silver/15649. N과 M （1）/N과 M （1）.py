import sys

n, m = map(int, sys.stdin.readline().split())
lst = []


def dfs():
    if len(lst) == m:
        print(' '.join(map(str, lst)))
        return
    else:
        for i in range(1, n+1):
            if i not in lst:
                lst.append(i)
                dfs()
                lst.pop()


dfs()
