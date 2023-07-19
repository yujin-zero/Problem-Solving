import sys

n, m = map(int, sys.stdin.readline().split())
pocketmon1 = {}
pocketmon2 = {}
for i in range(n):
    name = sys.stdin.readline().strip()
    pocketmon1[i+1] = name
    pocketmon2[name] = i+1
for _ in range(m):
    x = sys.stdin.readline().strip()
    if x.isdigit():
        print(pocketmon1[int(x)])
    else:
        print(pocketmon2[x])
