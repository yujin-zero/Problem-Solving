import sys

n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

count = 0
i, j = 0, 0
while i < n and j < n:
    x = sum(lst[i:j+1])
    if x == m:
        count += 1
        i += 1
        j += 1
    elif x < m:
        j += 1
    else:
        i += 1

print(count)
