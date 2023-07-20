import sys

n, m = map(int, sys.stdin.readline().split())
name = {}
sum = 0
for _ in range(n):
    x = sys.stdin.readline().rstrip()
    name[x] = 1
for _ in range(m):
    x = sys.stdin.readline().rstrip()
    if x in name:
        sum += 1
        name[x] += 1

a = dict(sorted(name.items()))
print(sum)
for v in a:
    if a[v] == 2:
        print(v)
