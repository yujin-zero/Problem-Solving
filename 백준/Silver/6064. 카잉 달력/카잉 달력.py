import sys
import math

t = int(sys.stdin.readline())
for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().split())

    max_year = math.lcm(m, n)

    temp = 0
    while x <= max_year:
        if x % n == y % n:
            print(x)
            temp = 1
            break
        x += m

    if temp == 0:
        print(-1)
