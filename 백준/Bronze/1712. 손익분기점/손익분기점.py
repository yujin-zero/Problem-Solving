import sys

a, b, c = map(int, sys.stdin.readline().split())
if b < c:
    ans = a // (c-b)+1
    print(ans)
else:
    print(-1)
