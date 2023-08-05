import sys
import math

t = int(sys.stdin.readline())
for _ in range(t):
    x, y = map(int, sys.stdin.readline().split())
    print(math.lcm(x, y))
