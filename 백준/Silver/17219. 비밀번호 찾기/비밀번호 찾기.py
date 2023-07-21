import sys

n, m = map(int, sys.stdin.readline().split())
password = {}

for _ in range(n):
    x, y = sys.stdin.readline().split()
    password[x] = y

for _ in range(m):
    x = sys.stdin.readline().strip()
    print(password[x])
